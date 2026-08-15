---
name: frappe-iam-audit-program
description: 'Security audit program and compliance checklists for Frappe User and Role permissions.'
---

# Frappe IAM Audit Program

## Purpose
Automated and manual audit workflows to verify least-privilege access in Frappe installations.

## Audit Checkpoints
1. **Privileged Roles**: Audit all users assigned `System Manager` and `Administrator`.
2. **Dormant Accounts**: Identify users inactive > 90 days and auto-disable.
3. **Permission Matrix Review**: Validate DocPerm table for unauthorized `create`, `write`, `delete`, or `submit` rights.
4. **Audit Trail**: Ensure `Activity Log` and version tracking are enabled for financial and PII DocTypes.
