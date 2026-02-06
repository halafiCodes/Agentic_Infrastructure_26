# Project Chimera

Spec-driven foundation for an autonomous influencer system. Implementation code is intentionally absent until specs are ratified.

## Overview
Project Chimera is a requirements-first repository that captures product, technical, and research specs for an autonomous influencer system. The codebase intentionally stays minimal until the specifications are approved.

## Repository Structure
- [chimera/](chimera/) Core package skeleton and interfaces.
- [docs/](docs/) Product artifacts, SRS, and submission materials.
- [research/](research/) Architecture and tooling research notes.
- [scripts/](scripts/) Developer utilities for spec and quality checks.
- [skills/](skills/) Skill definitions and documentation.
- [specs/](specs/) Functional and technical requirements.
- [tests/](tests/) Tests validating interface expectations.

## Key Specs
- [specs/functional.md](specs/functional.md) Functional requirements and acceptance criteria.
- [specs/technical.md](specs/technical.md) Data, backend, security, and MCP requirements.
- [docs/frontend_spec.md](docs/frontend_spec.md) UI screens, flows, and component contracts.
- [docs/mcp_configuration.md](docs/mcp_configuration.md) MCP server inventory and tool schemas.
- [docs/agentic_trajectory.md](docs/agentic_trajectory.md) Evidence checklist for workflow growth.
- [docs/adr/0001-spec-first-architecture.md](docs/adr/0001-spec-first-architecture.md) Architecture decision record.

## Getting Started
### Prerequisites
- Python 3.10+ recommended

### Install
Use your preferred environment manager, then install project dependencies:
- Install dependencies defined in [pyproject.toml](pyproject.toml).

## Setup Structure
Use this structure when adding new materials to keep the repository organized:
- Core package code in [chimera/](chimera/)
- Specifications in [specs/](specs/)
- Product documentation in [docs/](docs/)
- Research notes in [research/](research/)
- Utility scripts in [scripts/](scripts/)
- Skill definitions in [skills/](skills/)
- Tests in [tests/](tests/)

### Run Tests
- Execute the test suite defined under [tests/](tests/).

## Development Workflow
1. Update or propose changes to specs in [specs/](specs/).
2. Use [docs/SRS.md](docs/SRS.md) for system requirements.
3. Keep implementation minimal until specs are ratified.
4. Validate changes with tests and spec checks.

## Governance
All contributions must follow the policies in [AGENTS.md](AGENTS.md).

## Status
This repository is in the specification and research phase.
