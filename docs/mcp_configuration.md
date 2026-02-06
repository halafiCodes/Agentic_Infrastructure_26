# MCP Configuration

## Source of Truth
- Primary config: .vscode/mcp.json
- Tenx MCP Sense setup: docs/tenx_mcp_setup.md

## Server Inventory
### tenxfeedbackanalytics
- Endpoint: https://mcppulse.10academy.org/proxy
- Transport: HTTP
- Headers:
  - X-Device: windows
  - X-Coding-Tool: vscode
- Auth:
  - If required, use environment-provided tokens and never commit secrets.

## Tool Schemas (Expected)
### fetch_trends
Input:
```json
{
  "source": "tiktok|instagram|twitter|youtube",
  "region": "string",
  "limit": 20
}
```
Output:
```json
{
  "source": "string",
  "region": "string",
  "as_of": "iso-8601",
  "trends": [
    {
      "trend_id": "string",
      "title": "string",
      "score": 0.0,
      "metadata": {"language": "string", "tags": ["string"]}
    }
  ]
}
```

### post_content
Input:
```json
{
  "platform": "twitter|instagram|threads",
  "text_content": "string",
  "media_urls": ["string"],
  "disclosure_level": "automated|assisted|none"
}
```
Output:
```json
{
  "publish_id": "string",
  "status": "scheduled|posted|failed"
}
```

## Governance
- All MCP calls must include a request_id and are logged in audit_log.
- Direct network calls are forbidden outside the MCP Gateway.
