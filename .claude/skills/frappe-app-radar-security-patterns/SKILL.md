---
name: frappe-app-radar-security-patterns
description: 'Continuous vulnerability scanning, dependency checking, and security monitoring for Frappe apps.'
---

# Frappe App Radar Security Patterns

## Purpose
Automates real-time security monitoring, dependency auditing, and attack surface minimization.

## Capabilities
- **Dependency Audit**: Scan `requirements.txt` and `package.json` against CVE databases.
- **Hook Verification**: Detect unregistered or insecure doc_events in `hooks.py`.
- **Payload Inspection**: Validate file upload MIME types and prevent path traversal attacks.
- **Alert Dispatch**: Send webhook notifications upon detecting suspicious admin logins or brute force attempts.
