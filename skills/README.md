# Chimera Skills

Skills are runtime capability packages invoked by the agent. These are contracts only (no implementation yet).

## skill_fetch_trends
**Input**
```json
{
  "source": "tiktok",
  "region": "US",
  "limit": 20
}
```
**Dependencies**
- MCP tool: fetch_trends
- Data store: trend_snapshots (MongoDB)

**Output**
```json
{
  "source": "tiktok",
  "region": "US",
  "as_of": "2026-02-04T00:00:00Z",
  "trends": [
    {
      "trend_id": "string",
      "title": "string",
      "score": 0.0,
      "metadata": {"language": "en", "tags": ["string"]}
    }
  ]
}
```
**Error Cases**
- invalid_source: unsupported platform
- rate_limited: upstream MCP rate limit
- schema_error: output missing required fields

## skill_generate_content
**Input**
```json
{
  "trend_id": "string",
  "tone": "playful",
  "length": "short"
}
```
**Pydantic Models**
- ContentGenerateInput
- ContentGenerateOutput

**Dependencies**
- MCP tool: generate_content
- Data store: content (PostgreSQL)

**Output**
```json
{
  "success": true,
  "content_id": "string",
  "caption": "string",
  "hashtags": ["string"],
  "assets": [{"type": "image", "uri": "string"}]
}
```
**Error Cases**
- missing_trend: trend_id not found
- policy_blocked: content failed safety checks
- validation_error: output missing caption or assets

## skill_publish_content
**Input**
```json
{
  "content_id": "string",
  "platform": "tiktok",
  "schedule_at": "2026-02-04T00:00:00Z"
}
```
**Pydantic Models**
- PublishContentInput
- PublishContentOutput

**Dependencies**
- MCP tool: post_content
- Data store: publish_status (PostgreSQL)

**Output**
```json
{
  "success": true,
  "publish_id": "string",
  "status": "scheduled",
  "platform": "tiktok"
}
```
**Error Cases**
- not_approved: content lacks HITL approval
- platform_error: upstream publish failed
- schedule_invalid: schedule_at in the past

## skill_review_decision
**Input**
```json
{
  "content_id": "string",
  "reviewer_id": "string",
  "decision": "approve|reject|needs_changes",
  "rationale": "string"
}
```
**Dependencies**
- Data store: review_decision (PostgreSQL)
- Policy engine: sensitive topic classifier

**Output**
```json
{
  "review_id": "string",
  "content_id": "string",
  "status": "recorded",
  "decided_at": "2026-02-04T00:00:00Z"
}
```
**Error Cases**
- content_missing: content_id not found
- decision_invalid: decision not in enum
- rationale_required: missing rationale for reject
