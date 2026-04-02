"""
ServiceNow MCP Server — Railway deployment with OAuth-protected SSE.

Exposes an ASGI `app` variable consumed by uvicorn.
OAuth flow: authorization_code + PKCE (Claude Desktop compatible).
"""

import base64
import hashlib
import hmac
import json
import logging
import os
import secrets
import time
from urllib.parse import parse_qs

import requests
import uvicorn
from dotenv import load_dotenv

# ---------------------------------------------------------------------------
# Request logging — patch Session.send so every outbound HTTP call is logged
# to stdout (visible in Railway deploy logs) before tools are imported.
# ---------------------------------------------------------------------------

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
_log = logging.getLogger("servicenow_mcp.http")

_original_send = requests.Session.send


def _logged_send(self, request, **kwargs):
    _log.info("→ %s %s", request.method, request.url)
    response = _original_send(self, request, **kwargs)
    _log.info("← %s %s (%.3fs)", response.status_code, request.url, response.elapsed.total_seconds())
    return response


requests.Session.send = _logged_send

from servicenow_mcp.server_sse import create_servicenow_mcp, create_starlette_app


# ---------------------------------------------------------------------------
# Signed-token helpers
# ---------------------------------------------------------------------------

def _make_signed_token(client_id: str, signing_key: bytes, ttl: int = 86400) -> str:
    expiry = int(time.time()) + ttl
    payload = f"{client_id}:{expiry}".encode()
    sig = hmac.new(signing_key, payload, hashlib.sha256).digest()
    payload_enc = base64.urlsafe_b64encode(payload).rstrip(b"=").decode()
    sig_enc = base64.urlsafe_b64encode(sig).rstrip(b"=").decode()
    return f"{payload_enc}.{sig_enc}"


def _verify_signed_token(token: str, signing_key: bytes):
    try:
        payload_enc, sig_enc = token.rsplit(".", 1)
        payload = base64.urlsafe_b64decode(payload_enc + "==")
        sig = base64.urlsafe_b64decode(sig_enc + "==")
        expected = hmac.new(signing_key, payload, hashlib.sha256).digest()
        if not hmac.compare_digest(sig, expected):
            return None
        client_id, expiry_str = payload.decode().rsplit(":", 1)
        if int(time.time()) > int(expiry_str):
            return None
        return client_id
    except Exception:
        return None


# ---------------------------------------------------------------------------
# OAuth ASGI wrapper
# ---------------------------------------------------------------------------

def create_oauth_protected_app(mcp_app, client_id: str, client_secret: str, server_url: str):
    server_url = server_url.rstrip("/")
    signing_key = hashlib.sha256(f"mcp-token-signing:{client_secret}".encode()).digest()
    secret_digest = hashlib.sha256(client_secret.encode()).digest()
    _auth_codes: dict = {}

    async def _send_json(send, status: int, body: dict, extra_headers=None):
        data = json.dumps(body).encode()
        headers = [
            (b"content-type", b"application/json"),
            (b"content-length", str(len(data)).encode()),
            (b"access-control-allow-origin", b"*"),
        ]
        if extra_headers:
            headers.extend(extra_headers)
        await send({"type": "http.response.start", "status": status, "headers": headers})
        await send({"type": "http.response.body", "body": data, "more_body": False})

    async def _send_redirect(send, location: str):
        await send({
            "type": "http.response.start",
            "status": 302,
            "headers": [(b"location", location.encode()), (b"content-length", b"0")],
        })
        await send({"type": "http.response.body", "body": b"", "more_body": False})

    async def _read_body(receive) -> bytes:
        body = b""
        while True:
            msg = await receive()
            body += msg.get("body", b"")
            if not msg.get("more_body", False):
                return body

    def _qs(scope) -> dict:
        qs = scope.get("query_string", b"").decode()
        return {k: v[0] for k, v in parse_qs(qs).items()} if qs else {}

    def _pkce_verify(code_verifier: str, code_challenge: str) -> bool:
        digest = hashlib.sha256(code_verifier.encode("ascii")).digest()
        expected = base64.urlsafe_b64encode(digest).rstrip(b"=").decode()
        return hmac.compare_digest(expected, code_challenge)

    async def protected_app(scope, receive, send):
        # Lifespan must be handled before the HTTP try/except block.
        if scope["type"] == "lifespan":
            print("[MCP-Auth] lifespan delegating to mcp_app", flush=True)
            await mcp_app(scope, receive, send)
            return

        if scope["type"] != "http":
            await mcp_app(scope, receive, send)
            return

        path = scope.get("path", "")
        method = scope.get("method", "GET")
        print(f"[MCP-Auth] {method} {path}", flush=True)

        try:
            # OAuth discovery: resource metadata
            if path.startswith("/.well-known/oauth-protected-resource"):
                await _send_json(send, 200, {
                    "resource": server_url,
                    "authorization_servers": [server_url],
                })
                return

            # OAuth discovery: authorization server metadata
            if path == "/.well-known/oauth-authorization-server":
                await _send_json(send, 200, {
                    "issuer": server_url,
                    "authorization_endpoint": f"{server_url}/authorize",
                    "token_endpoint": f"{server_url}/token",
                    "grant_types_supported": ["authorization_code", "client_credentials"],
                    "response_types_supported": ["code"],
                    "code_challenge_methods_supported": ["S256"],
                    "token_endpoint_auth_methods_supported": ["none", "client_secret_post"],
                })
                return

            # Authorization endpoint — auto-approve, redirect with code
            if path == "/authorize" and method == "GET":
                params = _qs(scope)
                if params.get("response_type") != "code":
                    await _send_json(send, 400, {"error": "unsupported_response_type"})
                    return
                if not hmac.compare_digest(params.get("client_id", "").encode(), client_id.encode()):
                    await _send_json(send, 401, {"error": "invalid_client"})
                    return
                redirect_uri = params.get("redirect_uri", "")
                if not redirect_uri:
                    await _send_json(send, 400, {"error": "invalid_request"})
                    return

                code = secrets.token_urlsafe(32)
                _auth_codes[code] = {
                    "code_challenge": params.get("code_challenge", ""),
                    "redirect_uri": redirect_uri,
                    "expires_at": int(time.time()) + 300,
                }
                sep = "&" if "?" in redirect_uri else "?"
                location = f"{redirect_uri}{sep}code={code}"
                state = params.get("state", "")
                if state:
                    location += f"&state={state}"
                await _send_redirect(send, location)
                return

            # Token endpoint — exchange code or client_credentials
            if path in ("/token", "/oauth/token") and method == "POST":
                raw = await _read_body(receive)
                params = {k: v[0] for k, v in parse_qs(raw.decode()).items()}
                grant_type = params.get("grant_type", "")

                if grant_type == "authorization_code":
                    code = params.get("code", "")
                    entry = _auth_codes.pop(code, None)
                    if entry is None or int(time.time()) > entry["expires_at"]:
                        await _send_json(send, 400, {"error": "invalid_grant"})
                        return
                    if not hmac.compare_digest(params.get("client_id", "").encode(), client_id.encode()):
                        await _send_json(send, 401, {"error": "invalid_client"})
                        return
                    code_challenge = entry.get("code_challenge", "")
                    if code_challenge:
                        if not _pkce_verify(params.get("code_verifier", ""), code_challenge):
                            await _send_json(send, 400, {
                                "error": "invalid_grant",
                                "error_description": "PKCE failed",
                            })
                            return
                    token = _make_signed_token(client_id, signing_key)
                    await _send_json(send, 200, {
                        "access_token": token,
                        "token_type": "bearer",
                        "expires_in": 86400,
                    })
                    return

                if grant_type == "client_credentials":
                    id_ok = hmac.compare_digest(params.get("client_id", "").encode(), client_id.encode())
                    secret_ok = hmac.compare_digest(
                        hashlib.sha256(params.get("client_secret", "").encode()).digest(),
                        secret_digest,
                    )
                    if not (id_ok and secret_ok):
                        await _send_json(send, 401, {"error": "invalid_client"})
                        return
                    token = _make_signed_token(client_id, signing_key)
                    await _send_json(send, 200, {
                        "access_token": token,
                        "token_type": "bearer",
                        "expires_in": 86400,
                    })
                    return

                await _send_json(send, 400, {"error": "unsupported_grant_type"})
                return

            # Health check
            if path == "/health":
                await _send_json(send, 200, {"status": "ok"})
                return

            # All other paths — require Bearer token
            headers_dict = dict(scope.get("headers", []))
            auth = headers_dict.get(b"authorization", b"").decode()
            if not auth.startswith("Bearer "):
                await _send_json(send, 401, {"error": "unauthorized"}, [
                    (b"www-authenticate",
                     f'Bearer realm="{server_url}", resource_metadata="{server_url}/.well-known/oauth-protected-resource"'.encode()),
                ])
                return
            if _verify_signed_token(auth[len("Bearer "):], signing_key) is None:
                await _send_json(send, 401, {"error": "invalid_token"}, [
                    (b"www-authenticate",
                     f'Bearer error="invalid_token", realm="{server_url}", resource_metadata="{server_url}/.well-known/oauth-protected-resource"'.encode()),
                ])
                return

            await mcp_app(scope, receive, send)

        except Exception as exc:
            print(f"[MCP-Auth] EXCEPTION: {exc}", flush=True)
            import traceback
            traceback.print_exc()
            try:
                await _send_json(send, 500, {"error": "internal_server_error", "detail": str(exc)})
            except Exception:
                pass

    return protected_app


# ---------------------------------------------------------------------------
# Build the ASGI app (consumed by uvicorn / Railway)
# ---------------------------------------------------------------------------

load_dotenv()

_instance_url = os.environ["SERVICENOW_INSTANCE_URL"]
_username = os.environ["SERVICENOW_USERNAME"]
_password = os.environ["SERVICENOW_PASSWORD"]

_sn_server = create_servicenow_mcp(_instance_url, _username, _password)
_starlette_app = create_starlette_app(_sn_server.mcp_server, debug=False)

_CLIENT_ID = os.environ.get("MCP_SERVER_CLIENT_ID")
_CLIENT_SECRET = os.environ.get("MCP_SERVER_CLIENT_SECRET")
_SERVER_URL = os.environ.get("MCP_SERVER_URL", "")

if _CLIENT_ID and _CLIENT_SECRET:
    app = create_oauth_protected_app(_starlette_app, _CLIENT_ID, _CLIENT_SECRET, _SERVER_URL)
    print("✅ MCP app initialized with OAuth protection", flush=True)
else:
    app = _starlette_app
    print("⚠️  No OAuth credentials set — endpoint is public", flush=True)


# ---------------------------------------------------------------------------
# Local dev entry point
# ---------------------------------------------------------------------------

def main():
    port = int(os.environ.get("PORT", 8080))
    uvicorn.run(
        "servicenow_mcp.server_railway:app",
        host="0.0.0.0",
        port=port,
        reload=False,
    )


if __name__ == "__main__":
    main()
