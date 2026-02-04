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

## skill_generate_content
**Input**
```json
{
  "trend_id": "string",
  "tone": "playful",
  "length": "short"
}
```
**Output**
```json
{
  "content_id": "string",
  "caption": "string",
  "hashtags": ["string"],
  "assets": [{"type": "image", "uri": "string"}]
}
```

## skill_publish_content
**Input**
```json
{
  "content_id": "string",
  "platform": "tiktok",
  "schedule_at": "2026-02-04T00:00:00Z"
}
```
**Output**
```json
{
  "publish_id": "string",
  "status": "scheduled",
  "platform": "tiktok"
}
```
