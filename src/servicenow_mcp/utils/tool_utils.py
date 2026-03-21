from typing import Any, Callable, Dict, Tuple, Type

# Import all necessary tool implementation functions and params models
# (This list needs to be kept complete and up-to-date)
from servicenow_mcp.tools.catalog_optimization import (
    OptimizationRecommendationsParams,
    UpdateCatalogItemParams,
)
from servicenow_mcp.tools.catalog_optimization import (
    get_optimization_recommendations as get_optimization_recommendations_tool,
)
from servicenow_mcp.tools.catalog_optimization import (
    update_catalog_item as update_catalog_item_tool,
)
from servicenow_mcp.tools.catalog_tools import (
    CreateCatalogCategoryParams,
    GetCatalogItemParams,
    ListCatalogCategoriesParams,
    ListCatalogItemsParams,
    MoveCatalogItemsParams,
    UpdateCatalogCategoryParams,
)
from servicenow_mcp.tools.catalog_tools import (
    create_catalog_category as create_catalog_category_tool,
)
from servicenow_mcp.tools.catalog_tools import (
    get_catalog_item as get_catalog_item_tool,
)
from servicenow_mcp.tools.catalog_tools import (
    list_catalog_categories as list_catalog_categories_tool,
)
from servicenow_mcp.tools.catalog_tools import (
    list_catalog_items as list_catalog_items_tool,
)
from servicenow_mcp.tools.catalog_tools import (
    move_catalog_items as move_catalog_items_tool,
)
from servicenow_mcp.tools.catalog_tools import (
    update_catalog_category as update_catalog_category_tool,
)
from servicenow_mcp.tools.catalog_variables import (
    CreateCatalogItemVariableParams,
    ListCatalogItemVariablesParams,
    UpdateCatalogItemVariableParams,
)
from servicenow_mcp.tools.catalog_variables import (
    create_catalog_item_variable as create_catalog_item_variable_tool,
)
from servicenow_mcp.tools.catalog_variables import (
    list_catalog_item_variables as list_catalog_item_variables_tool,
)
from servicenow_mcp.tools.catalog_variables import (
    update_catalog_item_variable as update_catalog_item_variable_tool,
)
from servicenow_mcp.tools.change_tools import (
    AddChangeTaskParams,
    ApproveChangeParams,
    CreateChangeRequestParams,
    GetChangeRequestDetailsParams,
    ListChangeRequestsParams,
    RejectChangeParams,
    SubmitChangeForApprovalParams,
    UpdateChangeRequestParams,
)
from servicenow_mcp.tools.change_tools import (
    add_change_task as add_change_task_tool,
)
from servicenow_mcp.tools.change_tools import (
    approve_change as approve_change_tool,
)
from servicenow_mcp.tools.change_tools import (
    create_change_request as create_change_request_tool,
)
from servicenow_mcp.tools.change_tools import (
    get_change_request_details as get_change_request_details_tool,
)
from servicenow_mcp.tools.change_tools import (
    list_change_requests as list_change_requests_tool,
)
from servicenow_mcp.tools.change_tools import (
    reject_change as reject_change_tool,
)
from servicenow_mcp.tools.change_tools import (
    submit_change_for_approval as submit_change_for_approval_tool,
)
from servicenow_mcp.tools.change_tools import (
    update_change_request as update_change_request_tool,
)
from servicenow_mcp.tools.changeset_tools import (
    AddFileToChangesetParams,
    CommitChangesetParams,
    CreateChangesetParams,
    GetChangesetDetailsParams,
    ListChangesetsParams,
    PublishChangesetParams,
    UpdateChangesetParams,
)
from servicenow_mcp.tools.changeset_tools import (
    add_file_to_changeset as add_file_to_changeset_tool,
)
from servicenow_mcp.tools.changeset_tools import (
    commit_changeset as commit_changeset_tool,
)
from servicenow_mcp.tools.changeset_tools import (
    create_changeset as create_changeset_tool,
)
from servicenow_mcp.tools.changeset_tools import (
    get_changeset_details as get_changeset_details_tool,
)
from servicenow_mcp.tools.changeset_tools import (
    list_changesets as list_changesets_tool,
)
from servicenow_mcp.tools.changeset_tools import (
    publish_changeset as publish_changeset_tool,
)
from servicenow_mcp.tools.changeset_tools import (
    update_changeset as update_changeset_tool,
)
from servicenow_mcp.tools.incident_tools import (
    AddCommentParams,
    CreateIncidentParams,
    ListIncidentsParams,
    ResolveIncidentParams,
    UpdateIncidentParams,
    GetIncidentByNumberParams,
)
from servicenow_mcp.tools.incident_tools import (
    add_comment as add_comment_tool,
)
from servicenow_mcp.tools.incident_tools import (
    create_incident as create_incident_tool,
)
from servicenow_mcp.tools.incident_tools import (
    list_incidents as list_incidents_tool,
)
from servicenow_mcp.tools.incident_tools import (
    resolve_incident as resolve_incident_tool,
)
from servicenow_mcp.tools.incident_tools import (
    update_incident as update_incident_tool,
)
from servicenow_mcp.tools.incident_tools import (
    get_incident_by_number as get_incident_by_number_tool,
)
from servicenow_mcp.tools.knowledge_base import (
    CreateArticleParams,
    CreateKnowledgeBaseParams,
    GetArticleParams,
    ListArticlesParams,
    ListKnowledgeBasesParams,
    PublishArticleParams,
    UpdateArticleParams,
)
from servicenow_mcp.tools.knowledge_base import (
    CreateCategoryParams as CreateKBCategoryParams,  # Aliased
)
from servicenow_mcp.tools.knowledge_base import (
    ListCategoriesParams as ListKBCategoriesParams,  # Aliased
)
from servicenow_mcp.tools.knowledge_base import (
    create_article as create_article_tool,
)
from servicenow_mcp.tools.knowledge_base import (
    # create_category aliased in function call
    create_knowledge_base as create_knowledge_base_tool,
)
from servicenow_mcp.tools.knowledge_base import (
    get_article as get_article_tool,
)
from servicenow_mcp.tools.knowledge_base import (
    list_articles as list_articles_tool,
)
from servicenow_mcp.tools.knowledge_base import (
    # list_categories aliased in function call
    list_knowledge_bases as list_knowledge_bases_tool,
)
from servicenow_mcp.tools.knowledge_base import (
    publish_article as publish_article_tool,
)
from servicenow_mcp.tools.knowledge_base import (
    update_article as update_article_tool,
)
from servicenow_mcp.tools.script_include_tools import (
    CreateScriptIncludeParams,
    DeleteScriptIncludeParams,
    GetScriptIncludeParams,
    ListScriptIncludesParams,
    ScriptIncludeResponse,
    UpdateScriptIncludeParams,
)
from servicenow_mcp.tools.script_include_tools import (
    create_script_include as create_script_include_tool,
)
from servicenow_mcp.tools.script_include_tools import (
    delete_script_include as delete_script_include_tool,
)
from servicenow_mcp.tools.script_include_tools import (
    get_script_include as get_script_include_tool,
)
from servicenow_mcp.tools.script_include_tools import (
    list_script_includes as list_script_includes_tool,
)
from servicenow_mcp.tools.script_include_tools import (
    update_script_include as update_script_include_tool,
)
from servicenow_mcp.tools.user_tools import (
    AddGroupMembersParams,
    CreateGroupParams,
    CreateUserParams,
    GetUserParams,
    ListGroupsParams,
    ListUsersParams,
    RemoveGroupMembersParams,
    UpdateGroupParams,
    UpdateUserParams,
)
from servicenow_mcp.tools.user_tools import (
    add_group_members as add_group_members_tool,
)
from servicenow_mcp.tools.user_tools import (
    create_group as create_group_tool,
)
from servicenow_mcp.tools.user_tools import (
    create_user as create_user_tool,
)
from servicenow_mcp.tools.user_tools import (
    get_user as get_user_tool,
)
from servicenow_mcp.tools.user_tools import (
    list_groups as list_groups_tool,
)
from servicenow_mcp.tools.user_tools import (
    list_users as list_users_tool,
)
from servicenow_mcp.tools.user_tools import (
    remove_group_members as remove_group_members_tool,
)
from servicenow_mcp.tools.user_tools import (
    update_group as update_group_tool,
)
from servicenow_mcp.tools.user_tools import (
    update_user as update_user_tool,
)
from servicenow_mcp.tools.workflow_tools import (
    ActivateWorkflowParams,
    AddWorkflowActivityParams,
    CreateWorkflowParams,
    DeactivateWorkflowParams,
    DeleteWorkflowActivityParams,
    GetWorkflowActivitiesParams,
    GetWorkflowDetailsParams,
    ListWorkflowsParams,
    ListWorkflowVersionsParams,
    ReorderWorkflowActivitiesParams,
    UpdateWorkflowActivityParams,
    UpdateWorkflowParams,
)
from servicenow_mcp.tools.workflow_tools import (
    activate_workflow as activate_workflow_tool,
)
from servicenow_mcp.tools.workflow_tools import (
    add_workflow_activity as add_workflow_activity_tool,
)
from servicenow_mcp.tools.workflow_tools import (
    create_workflow as create_workflow_tool,
)
from servicenow_mcp.tools.workflow_tools import (
    deactivate_workflow as deactivate_workflow_tool,
)
from servicenow_mcp.tools.workflow_tools import (
    delete_workflow_activity as delete_workflow_activity_tool,
)
from servicenow_mcp.tools.workflow_tools import (
    get_workflow_activities as get_workflow_activities_tool,
)
from servicenow_mcp.tools.workflow_tools import (
    get_workflow_details as get_workflow_details_tool,
)
from servicenow_mcp.tools.workflow_tools import (
    list_workflow_versions as list_workflow_versions_tool,
)
from servicenow_mcp.tools.workflow_tools import (
    list_workflows as list_workflows_tool,
)
from servicenow_mcp.tools.workflow_tools import (
    reorder_workflow_activities as reorder_workflow_activities_tool,
)
from servicenow_mcp.tools.workflow_tools import (
    update_workflow as update_workflow_tool,
)
from servicenow_mcp.tools.workflow_tools import (
    update_workflow_activity as update_workflow_activity_tool,
)
from servicenow_mcp.tools.story_tools import (
    CreateStoryParams,
    UpdateStoryParams,
    ListStoriesParams,
    ListStoryDependenciesParams,
    CreateStoryDependencyParams,
    DeleteStoryDependencyParams,
)
from servicenow_mcp.tools.story_tools import (
    create_story as create_story_tool,
    update_story as update_story_tool,
    list_stories as list_stories_tool,
    list_story_dependencies as list_story_dependencies_tool,
    create_story_dependency as create_story_dependency_tool,
    delete_story_dependency as delete_story_dependency_tool,
)
from servicenow_mcp.tools.epic_tools import (
    CreateEpicParams,
    UpdateEpicParams,
    ListEpicsParams,
)
from servicenow_mcp.tools.epic_tools import (
    create_epic as create_epic_tool,
    update_epic as update_epic_tool,
    list_epics as list_epics_tool,
)
from servicenow_mcp.tools.scrum_task_tools import (
    CreateScrumTaskParams,
    UpdateScrumTaskParams,
    ListScrumTasksParams,
)
from servicenow_mcp.tools.scrum_task_tools import (
    create_scrum_task as create_scrum_task_tool,
    update_scrum_task as update_scrum_task_tool,
    list_scrum_tasks as list_scrum_tasks_tool,
)
from servicenow_mcp.tools.project_tools import (
    CreateProjectParams,
    UpdateProjectParams,
    ListProjectsParams,
)
from servicenow_mcp.tools.project_tools import (
    create_project as create_project_tool,
    update_project as update_project_tool,
    list_projects as list_projects_tool,
)

# Define a type alias for the Pydantic models or dataclasses used for params
ParamsModel = Type[Any]  # Use Type[Any] for broader compatibility initially

# Define the structure of the tool definition tuple
ToolDefinition = Tuple[
    Callable,  # Implementation function
    ParamsModel,  # Pydantic model for parameters
    Type,  # Return type annotation (used for hints, not strictly enforced by low-level server)
    str,  # Description
    str,  # Serialization method ('str', 'json', 'dict', 'model_dump', etc.)
]


def get_tool_definitions(
    create_kb_category_tool_impl: Callable, list_kb_categories_tool_impl: Callable
) -> Dict[str, ToolDefinition]:
    """
    Returns a dictionary containing definitions for all available ServiceNow tools.

    This centralizes the tool definitions for use in the server implementation.
    Pass aliased functions for KB categories directly.

    Returns:
        Dict[str, ToolDefinition]: A dictionary mapping tool names to their definitions.
    """
    tool_definitions: Dict[str, ToolDefinition] = {
        # Incident Tools
        "create_incident": (
            create_incident_tool,
            CreateIncidentParams,
            str,
            "Create a new incident in ServiceNow. Pass assignment_group as a display name string (e.g. 'Network Support') — not a sys_id.",
            "str",
        ),
        "update_incident": (
            update_incident_tool,
            UpdateIncidentParams,
            str,
            "Update fields on an existing incident. incident_id accepts either an INC number (e.g. 'INC0012345') or a 32-char hex sys_id. Only pass fields that need to change.",
            "str",
        ),
        "add_comment": (
            add_comment_tool,
            AddCommentParams,
            str,
            "Add a comment or work note to an incident. Set is_work_note=true for internal work notes visible only to agents; false (default) for customer-visible comments.",
            "str",
        ),
        "resolve_incident": (
            resolve_incident_tool,
            ResolveIncidentParams,
            str,
            "Resolve an incident by setting its state to Resolved. Requires a resolution_code and resolution_notes. incident_id accepts an INC number or sys_id.",
            "str",
        ),
        "list_incidents": (
            list_incidents_tool,
            ListIncidentsParams,
            str,  # Expects JSON string
            (
                "List incidents from ServiceNow with optional filters. "
                "Use 'assignment_group' to filter by group name (partial match) or group sys_id — do NOT use 'query' for this. "
                "Use 'state', 'assigned_to', and 'category' for exact-match field filters. "
                "Use 'query' only for free-text search across short_description and description fields. "
                "Never put raw ServiceNow encoded query syntax into any parameter."
            ),
            "json",  # Tool returns list/dict, needs JSON dump
        ),
        "get_incident_by_number": (
            get_incident_by_number_tool,
            GetIncidentByNumberParams,
            str,
            "Fetch full details of a single incident by its INC number (e.g. 'INC0012345'). Use this when you have the exact number; use list_incidents to search.",
            "json_dict",
        ),
        # Catalog Tools
        "list_catalog_items": (
            list_catalog_items_tool,
            ListCatalogItemsParams,
            str,
            "List service catalog items. Use 'query' for free-text name search; use 'category' for exact category filter. Defaults to active items only.",
            "json",
        ),
        "get_catalog_item": (
            get_catalog_item_tool,
            GetCatalogItemParams,
            str,
            "Fetch full details of a single catalog item by its sys_id or catalog item ID. Use list_catalog_items to find the ID first.",
            "json_dict",
        ),
        "list_catalog_categories": (
            list_catalog_categories_tool,
            ListCatalogCategoriesParams,
            str,
            "List service catalog categories. Use 'query' for partial name search. Defaults to active categories only.",
            "json",
        ),
        "create_catalog_category": (
            create_catalog_category_tool,
            CreateCatalogCategoryParams,
            str,
            "Create a new category in the service catalog.",
            "json_dict",
        ),
        "update_catalog_category": (
            update_catalog_category_tool,
            UpdateCatalogCategoryParams,
            str,
            "Update an existing catalog category. Requires the category sys_id; use list_catalog_categories to find it.",
            "json_dict",
        ),
        "move_catalog_items": (
            move_catalog_items_tool,
            MoveCatalogItemsParams,
            str,
            "Move one or more catalog items to a different category. Provide item sys_ids and the target category sys_id.",
            "json_dict",
        ),
        "get_optimization_recommendations": (
            get_optimization_recommendations_tool,
            OptimizationRecommendationsParams,
            str,
            "Analyse the service catalog and return optimization recommendations (unused items, duplicates, missing descriptions, etc.).",
            "json",
        ),
        "update_catalog_item": (
            update_catalog_item_tool,
            UpdateCatalogItemParams,
            str,
            "Update fields on an existing catalog item. Requires the item sys_id; only pass fields that need to change.",
            "json",
        ),
        # Catalog Variables
        "create_catalog_item_variable": (
            create_catalog_item_variable_tool,
            CreateCatalogItemVariableParams,
            Dict[str, Any],
            "Add a new input variable (question) to a catalog item. Requires the catalog item sys_id.",
            "dict",
        ),
        "list_catalog_item_variables": (
            list_catalog_item_variables_tool,
            ListCatalogItemVariablesParams,
            Dict[str, Any],
            "List all input variables defined on a catalog item. Requires the catalog item sys_id.",
            "dict",
        ),
        "update_catalog_item_variable": (
            update_catalog_item_variable_tool,
            UpdateCatalogItemVariableParams,
            Dict[str, Any],
            "Update an existing catalog item variable. Requires both the catalog item sys_id and the variable sys_id.",
            "dict",
        ),
        # Change Management Tools
        "create_change_request": (
            create_change_request_tool,
            CreateChangeRequestParams,
            str,
            "Create a new change request (normal, standard, or emergency). Pass assignment_group as a display name string.",
            "str",
        ),
        "update_change_request": (
            update_change_request_tool,
            UpdateChangeRequestParams,
            str,
            "Update fields on an existing change request. change_id accepts a CHG number or sys_id. Only pass fields that need to change.",
            "str",
        ),
        "list_change_requests": (
            list_change_requests_tool,
            ListChangeRequestsParams,
            str,
            "List change requests with optional filters. Use 'state', 'type', 'category', 'assignment_group', or 'timeframe' for structured filters. Use 'query' only for raw ServiceNow encoded query strings.",
            "json",
        ),
        "get_change_request_details": (
            get_change_request_details_tool,
            GetChangeRequestDetailsParams,
            str,
            "Fetch full details of a single change request by its CHG number or sys_id.",
            "json",
        ),
        "add_change_task": (
            add_change_task_tool,
            AddChangeTaskParams,
            str,
            "Add a sub-task to an existing change request. change_id accepts a CHG number or sys_id.",
            "json_dict",
        ),
        "submit_change_for_approval": (
            submit_change_for_approval_tool,
            SubmitChangeForApprovalParams,
            str,
            "Move a change request into the approval workflow. change_id accepts a CHG number or sys_id.",
            "str",
        ),
        "approve_change": (
            approve_change_tool,
            ApproveChangeParams,
            str,
            "Record an approval decision on a change request. change_id accepts a CHG number or sys_id.",
            "str",
        ),
        "reject_change": (
            reject_change_tool,
            RejectChangeParams,
            str,
            "Reject a change request and record the reason. change_id accepts a CHG number or sys_id.",
            "str",
        ),
        # Workflow Management Tools
        "list_workflows": (
            list_workflows_tool,
            ListWorkflowsParams,
            str,
            "List ServiceNow workflows. Use 'query' for name search and 'active' to filter by status.",
            "json",
        ),
        "get_workflow_details": (
            get_workflow_details_tool,
            GetWorkflowDetailsParams,
            str,
            "Fetch full details of a single workflow by its sys_id.",
            "json",
        ),
        "list_workflow_versions": (
            list_workflow_versions_tool,
            ListWorkflowVersionsParams,
            str,
            "List all published versions of a workflow. Requires the workflow sys_id.",
            "json",
        ),
        "get_workflow_activities": (
            get_workflow_activities_tool,
            GetWorkflowActivitiesParams,
            str,
            "List all activities (steps) in a specific workflow version. Requires the workflow sys_id.",
            "json",
        ),
        "create_workflow": (
            create_workflow_tool,
            CreateWorkflowParams,
            str,
            "Create a new workflow in ServiceNow.",
            "json_dict",
        ),
        "update_workflow": (
            update_workflow_tool,
            UpdateWorkflowParams,
            str,
            "Update an existing workflow's metadata. Requires the workflow sys_id. To change activities use add/update/delete_workflow_activity.",
            "json_dict",
        ),
        "activate_workflow": (
            activate_workflow_tool,
            ActivateWorkflowParams,
            str,
            "Activate (publish) a workflow so it can be triggered. Requires the workflow sys_id.",
            "str",
        ),
        "deactivate_workflow": (
            deactivate_workflow_tool,
            DeactivateWorkflowParams,
            str,
            "Deactivate a workflow to prevent it from being triggered. Requires the workflow sys_id.",
            "str",
        ),
        "add_workflow_activity": (
            add_workflow_activity_tool,
            AddWorkflowActivityParams,
            str,
            "Add a new activity (step) to a workflow. Requires the workflow sys_id and activity type.",
            "json_dict",
        ),
        "update_workflow_activity": (
            update_workflow_activity_tool,
            UpdateWorkflowActivityParams,
            str,
            "Update an existing workflow activity. Requires both the workflow sys_id and the activity sys_id.",
            "json_dict",
        ),
        "delete_workflow_activity": (
            delete_workflow_activity_tool,
            DeleteWorkflowActivityParams,
            str,
            "Delete an activity from a workflow. Requires both the workflow sys_id and the activity sys_id.",
            "str",
        ),
        "reorder_workflow_activities": (
            reorder_workflow_activities_tool,
            ReorderWorkflowActivitiesParams,
            str,
            "Change the execution order of activities within a workflow. Requires the workflow sys_id and an ordered list of activity sys_ids.",
            "str",
        ),
        # Changeset Management Tools
        "list_changesets": (
            list_changesets_tool,
            ListChangesetsParams,
            str,
            "List developer changesets (source control batches) in ServiceNow. Filter by state or developer.",
            "json",
        ),
        "get_changeset_details": (
            get_changeset_details_tool,
            GetChangesetDetailsParams,
            str,
            "Fetch full details of a single changeset including all files it contains. Requires the changeset sys_id.",
            "json",
        ),
        "create_changeset": (
            create_changeset_tool,
            CreateChangesetParams,
            str,
            "Create a new developer changeset for grouping configuration changes before commit.",
            "json_dict",
        ),
        "update_changeset": (
            update_changeset_tool,
            UpdateChangesetParams,
            str,
            "Update an existing changeset's metadata. Requires the changeset sys_id.",
            "json_dict",
        ),
        "commit_changeset": (
            commit_changeset_tool,
            CommitChangesetParams,
            str,
            "Commit a changeset to the local update set. Requires the changeset sys_id.",
            "str",
        ),
        "publish_changeset": (
            publish_changeset_tool,
            PublishChangesetParams,
            str,
            "Publish a committed changeset to make it available for deployment. Requires the changeset sys_id.",
            "str",
        ),
        "add_file_to_changeset": (
            add_file_to_changeset_tool,
            AddFileToChangesetParams,
            str,
            "Add a configuration file/record to an existing changeset. Requires the changeset sys_id and the file sys_id.",
            "str",
        ),
        # Script Include Tools
        "list_script_includes": (
            list_script_includes_tool,
            ListScriptIncludesParams,
            Dict[str, Any],
            "List server-side Script Include records. Use 'query' to search by name.",
            "raw_dict",
        ),
        "get_script_include": (
            get_script_include_tool,
            GetScriptIncludeParams,
            Dict[str, Any],
            "Fetch the full script body of a specific Script Include by its sys_id or name.",
            "raw_dict",
        ),
        "create_script_include": (
            create_script_include_tool,
            CreateScriptIncludeParams,
            ScriptIncludeResponse,
            "Create a new server-side Script Include record with the provided JavaScript body.",
            "raw_pydantic",
        ),
        "update_script_include": (
            update_script_include_tool,
            UpdateScriptIncludeParams,
            ScriptIncludeResponse,
            "Update the script body or metadata of an existing Script Include. Requires the sys_id.",
            "raw_pydantic",
        ),
        "delete_script_include": (
            delete_script_include_tool,
            DeleteScriptIncludeParams,
            str,
            "Permanently delete a Script Include record. Requires the sys_id. This cannot be undone.",
            "json_dict",
        ),
        # Knowledge Base Tools
        "create_knowledge_base": (
            create_knowledge_base_tool,
            CreateKnowledgeBaseParams,
            str,
            "Create a new knowledge base in ServiceNow.",
            "json_dict",
        ),
        "list_knowledge_bases": (
            list_knowledge_bases_tool,
            ListKnowledgeBasesParams,
            Dict[str, Any],
            "List knowledge bases. Use 'query' for name search; use 'active' to filter by status.",
            "raw_dict",
        ),
        "create_category": (
            create_kb_category_tool_impl,
            CreateKBCategoryParams,
            str,
            "Create a new category inside a knowledge base. Requires the knowledge base sys_id.",
            "json_dict",
        ),
        "create_article": (
            create_article_tool,
            CreateArticleParams,
            str,
            "Create a new knowledge article in draft state. Requires the knowledge base sys_id. Use publish_article to make it live.",
            "json_dict",
        ),
        "update_article": (
            update_article_tool,
            UpdateArticleParams,
            str,
            "Update an existing knowledge article's content or metadata. Requires the article sys_id.",
            "json_dict",
        ),
        "publish_article": (
            publish_article_tool,
            PublishArticleParams,
            str,
            "Publish a knowledge article to make it visible to end users. Requires the article sys_id.",
            "json_dict",
        ),
        "list_articles": (
            list_articles_tool,
            ListArticlesParams,
            Dict[str, Any],
            "List knowledge articles. Filter by 'knowledge_base' sys_id, 'category' sys_id, 'workflow_state' (draft/published/retired), or free-text 'query'.",
            "raw_dict",
        ),
        "get_article": (
            get_article_tool,
            GetArticleParams,
            Dict[str, Any],
            "Fetch the full content of a specific knowledge article by its sys_id.",
            "raw_dict",
        ),
        "list_categories": (
            list_kb_categories_tool_impl,
            ListKBCategoriesParams,
            Dict[str, Any],
            "List categories within a knowledge base. Filter by 'knowledge_base' sys_id or 'parent_category' sys_id for sub-categories.",
            "raw_dict",
        ),
        # User Management Tools
        "create_user": (
            create_user_tool,
            CreateUserParams,
            Dict[str, Any],
            "Create a new user record in ServiceNow.",
            "raw_dict",
        ),
        "update_user": (
            update_user_tool,
            UpdateUserParams,
            Dict[str, Any],
            "Update an existing user record. Requires the user sys_id. Only pass fields that need to change.",
            "raw_dict",
        ),
        "get_user": (
            get_user_tool,
            GetUserParams,
            Dict[str, Any],
            "Fetch a specific user by sys_id, username, or email. Provide only one identifier.",
            "raw_dict",
        ),
        "list_users": (
            list_users_tool,
            ListUsersParams,
            Dict[str, Any],
            "List users with optional filters. Use 'query' for partial match on name, username, or email. Use 'department' or 'active' for exact filters.",
            "raw_dict",
        ),
        "create_group": (
            create_group_tool,
            CreateGroupParams,
            Dict[str, Any],
            "Create a new user group in ServiceNow.",
            "raw_dict",
        ),
        "update_group": (
            update_group_tool,
            UpdateGroupParams,
            Dict[str, Any],
            "Update an existing group's metadata. Requires the group sys_id.",
            "raw_dict",
        ),
        "add_group_members": (
            add_group_members_tool,
            AddGroupMembersParams,
            Dict[str, Any],
            "Add one or more users to a group. Requires the group sys_id and a list of user sys_ids.",
            "raw_dict",
        ),
        "remove_group_members": (
            remove_group_members_tool,
            RemoveGroupMembersParams,
            Dict[str, Any],
            "Remove one or more users from a group. Requires the group sys_id and a list of user sys_ids.",
            "raw_dict",
        ),
        "list_groups": (
            list_groups_tool,
            ListGroupsParams,
            Dict[str, Any],
            "List user groups. Use 'query' for partial match on group name or description. Use 'type' or 'active' for exact filters.",
            "raw_dict",
        ),
        # Story Management Tools
        "create_story": (
            create_story_tool,
            CreateStoryParams,
            str,
            "Create a new agile story in ServiceNow. Requires a parent epic sys_id.",
            "str",
        ),
        "update_story": (
            update_story_tool,
            UpdateStoryParams,
            str,
            "Update an existing story's fields. Requires the story sys_id. Only pass fields that need to change.",
            "str",
        ),
        "list_stories": (
            list_stories_tool,
            ListStoriesParams,
            str,
            "List agile stories. Filter by sprint, epic, state, or assigned user sys_id.",
            "json",
        ),
        "list_story_dependencies": (
            list_story_dependencies_tool,
            ListStoryDependenciesParams,
            str,
            "List dependencies (blockers/dependents) for a specific story. Requires the story sys_id.",
            "json",
        ),
        "create_story_dependency": (
            create_story_dependency_tool,
            CreateStoryDependencyParams,
            str,
            "Create a dependency link between two stories. Provide the sys_ids of both the dependent and blocking story.",
            "str",
        ),
        "delete_story_dependency": (
            delete_story_dependency_tool,
            DeleteStoryDependencyParams,
            str,
            "Remove a dependency link between two stories. Requires the dependency record sys_id.",
            "str",
        ),
        # Epic Management Tools
        "create_epic": (
            create_epic_tool,
            CreateEpicParams,
            str,
            "Create a new agile epic in ServiceNow.",
            "str",
        ),
        "update_epic": (
            update_epic_tool,
            UpdateEpicParams,
            str,
            "Update an existing epic's fields. Requires the epic sys_id. Only pass fields that need to change.",
            "str",
        ),
        "list_epics": (
            list_epics_tool,
            ListEpicsParams,
            str,
            "List agile epics. Filter by project, state, or assigned user.",
            "json",
        ),
        # Scrum Task Management Tools
        "create_scrum_task": (
            create_scrum_task_tool,
            CreateScrumTaskParams,
            str,
            "Create a new scrum task linked to a story. Requires the parent story sys_id.",
            "str",
        ),
        "update_scrum_task": (
            update_scrum_task_tool,
            UpdateScrumTaskParams,
            str,
            "Update an existing scrum task. Requires the task sys_id. Only pass fields that need to change.",
            "str",
        ),
        "list_scrum_tasks": (
            list_scrum_tasks_tool,
            ListScrumTasksParams,
            str,
            "List scrum tasks. Filter by parent story, sprint, state, or assigned user.",
            "json",
        ),
        # Project Management Tools
        "create_project": (
            create_project_tool,
            CreateProjectParams,
            str,
            "Create a new project in ServiceNow.",
            "str",
        ),
        "update_project": (
            update_project_tool,
            UpdateProjectParams,
            str,
            "Update an existing project's fields. Requires the project sys_id. Only pass fields that need to change.",
            "str",
        ),
        "list_projects": (
            list_projects_tool,
            ListProjectsParams,
            str,
            "List projects. Filter by state, manager, or use 'query' for name search.",
            "json",
        ),
    }
    return tool_definitions
