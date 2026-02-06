# Chimera Governance (AGENTS)

## Purpose
Define fleet-wide governance rules and brand constraints for all Chimera agents.

## Global Directives
- Spec-first enforcement: read and cite relevant specs before changing code or tests.
- All content must pass policy checks before publication.
- Any sensitive topic triggers HITL review.
- Audit logs are mandatory for all actions.
- Traceability: every change must reference a spec section and acceptance criteria.

## Spec-First Workflow
- Always read specs/ and docs/ before implementing or editing.
- Reference the exact spec artifact in commit messages and PR descriptions.
- If a requirement is unclear, stop and request clarification.

## Change Trace Blocks
- Each change must include a short trace block in the PR/issue:
	- Spec reference: <file and section>
	- Acceptance criteria: <scenario id>
	- Risk: <low|medium|high>
	- Test: <test or command>

## Coding Standards (Chimera)
- Use explicit JSON schemas for all API and MCP tool contracts.
- Enforce pydantic model descriptions for all public inputs.
- Never bypass HITL logic in code paths.
- Prefer immutable audit logs; redact PII instead of deleting.

## Audit Log
- 2026-02-05: Routine maintenance update recorded for daily commit cadence.

## Brand Voice
- Tone: Positive, professional, and concise.
- Honesty Directive: Disclose AI identity on direct inquiry.
