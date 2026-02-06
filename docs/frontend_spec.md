# Frontend Specification

## Screen Inventory
1) Dashboard
   - Fleet health, task queue depth, and alert banners.
2) Trends Explorer
   - Trend list, filters, and trend detail panel.
3) Draft Composer
   - Draft preview, hashtags, assets, and metadata editor.
4) Review Queue
   - Pending approvals with side-by-side comparison.
5) Publish Scheduler
   - Calendar view with platform status.
6) Audit Log Viewer
   - Searchable timeline of actions.
7) Settings
   - MCP status, secrets status (masked), and policies summary.

## Core User Flows
- Trend -> Draft -> Review -> Publish
- Audit trace for every action
- Manual override and re-queue

## Component Hierarchy
- AppShell
  - TopNav
  - SideNav
  - ContentArea
- Dashboard
  - FleetStatusCards
  - QueueHealthChart
  - AlertsPanel
- TrendsExplorer
  - TrendFilters
  - TrendTable
  - TrendDetail
- DraftComposer
  - DraftPreview
  - MetadataForm
  - AssetManager
  - ValidationSummary
- ReviewQueue
  - ReviewList
  - ReviewDetail
  - DecisionPanel
- PublishScheduler
  - Calendar
  - PublishDetail
- AuditLog
  - LogFilters
  - LogTable

## Wireframes (Text)
Dashboard
+--------------------------------------------------+
| TopNav                                           |
+------+-------------------------+-----------------+
| Side | Fleet Cards             | Alerts Panel    |
| Nav  | Queue Chart             |                 |
+------+-------------------------+-----------------+

Trends Explorer
+--------------------------------------------------+
| Filters                                          |
+----------------------+---------------------------+
| Trend Table          | Trend Detail              |
+----------------------+---------------------------+

Draft Composer
+----------------------+---------------------------+
| Draft Preview        | Metadata Form             |
| Assets               | Validation Summary        |
+----------------------+---------------------------+

## Accessibility
- WCAG 2.1 AA compliance.
- Keyboard navigation for all form controls.
- Color contrast ratio >= 4.5:1.
- ARIA labels on interactive elements.

## API Mappings
- Trends Explorer uses Trend Fetcher response in specs/technical.md.
- Draft Composer uses Content Draft response in specs/technical.md.
- Review Queue uses Review Decision response in specs/technical.md.
- Publish Scheduler uses Publish Request response in specs/technical.md.
- Audit Log Viewer reads audit_log entries from Data Management section.

## Error States
- Network error: inline banner with retry.
- Validation error: field-level messages tied to API schema.
- Permission error: redirect to Settings with guidance.
