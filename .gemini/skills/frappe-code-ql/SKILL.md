---
name: frappe-code-ql
description: 'CodeQL static analysis and security scanning patterns tailored for Frappe and ERPNext codebases.'
---

# Frappe CodeQL Security Scanning

## Purpose
Detects security vulnerabilities and antipatterns in Frappe apps using semantic code queries.

## Key Vulnerability Patterns
1. **SQL Injection**: Detect raw string formatting in `frappe.db.sql()`. Enforce parameterized queries:
   `frappe.db.sql("SELECT name FROM tabItem WHERE item_code = %(code)s", {"code": code})`
2. **Cross-Site Scripting (XSS)**: Ensure unescaped user inputs are sanitized in Jinja and JS.
3. **Permission Bypasses**: Flag functions calling `frappe.get_doc` without `ignore_permissions=False` checks where required.
4. **Insecure Eval**: Ban usage of Python `eval()` in favor of safe expression parsers.
