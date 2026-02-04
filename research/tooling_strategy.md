# Tooling Strategy

## Developer Tools (MCP)
These MCP servers assist development and governance workflows.
- **git-mcp:** Version control operations, branch management, commit telemetry.
- **filesystem-mcp:** Safe file reads/writes with audit trails.
- **spec-mcp (optional):** Spec validation and traceability checks.

## Runtime Skills (Agent)
Skills are reusable capability packages the Chimera agent invokes at runtime.
- **skill_fetch_trends:** Pulls platform trend data and normalizes it.
- **skill_generate_content:** Produces draft copy, captions, and hashtags.
- **skill_publish_content:** Schedules or posts content to target platforms.

## Separation of Concerns
- **MCP Servers:** External bridges for development-time tasks and auditing.
- **Skills:** Runtime capabilities invoked by the agent in production.
