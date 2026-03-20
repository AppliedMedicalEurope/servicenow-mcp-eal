FROM python:3.11-slim

WORKDIR /app

# Copy project files
COPY pyproject.toml README.md LICENSE ./
COPY src/ ./src/
COPY config/ ./config/

# Install the package
RUN pip install -e .

# Expose the port the app runs on
EXPOSE 8080

# Railway deployment: OAuth-protected SSE server
CMD ["uvicorn", "servicenow_mcp.server_railway:app", "--host=0.0.0.0", "--port=8080"]