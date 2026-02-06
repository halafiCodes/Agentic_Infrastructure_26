# Rule Creation Spec (Agent Intent)

## Purpose
Define the blueprint an AI agent uses to generate the executable rules file for Project Chimera.

## Project Context
- System: Autonomous influencer operations with MCP integration.
- Governance: Spec-first, traceable, HITL-enforced.
- Primary specs: specs/functional.md, specs/technical.md, docs/frontend_spec.md.

## Required Directives (Checklist)
- [ ] Spec-first: always read specs/ and docs/ before changes.
- [ ] Traceability: reference exact spec sections in changes.
- [ ] HITL: route sensitive topics to human approval.
- [ ] Audit: log every action and decision.
- [ ] Security: no secrets in code or logs.
- [ ] MCP-only egress: no direct network calls.

## Forbidden Actions
- [ ] Publish content without approval.
- [ ] Bypass policy checks.
- [ ] Modify specs without updating acceptance criteria.
- [ ] Access external APIs outside MCP Gateway.

## Ambiguity Handling
- [ ] If a requirement is missing, request clarification before implementation.
- [ ] If schemas conflict, defer to specs/technical.md and log the conflict.

## Escalation Rules
- [ ] Any sensitive content or low confidence (<0.70) triggers HITL.
- [ ] Missing schema fields or validation errors trigger escalation.
- [ ] Security or compliance concerns trigger human review.

## Versioning
- [ ] Rules file must include version, date, and spec references.
- [ ] Any change bumps the rules version and updates trace block.

## Testing the Rules
- [ ] Lint for forbidden actions and missing spec references.
- [ ] Validate required directives are present.
- [ ] Confirm MCP-only egress enforcement is stated.

## Output Targets
- .cursor/rules
- AGENTS.md (governance)
- .github/copilot-instructions.md (if added)
