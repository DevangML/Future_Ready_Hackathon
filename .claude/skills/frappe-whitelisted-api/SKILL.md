---
name: frappe-whitelisted-api
description: 'Design and implementation patterns for secure, performant @frappe.whitelist() REST endpoints.'
---

# Frappe Whitelisted API Best Practices

## Purpose
Guidelines for developing robust, secure API endpoints using `@frappe.whitelist()`.

## Core Standards
1. **Permission Enforcement**:
   ```python
   @frappe.whitelist(methods=["POST"])
   def update_record(record_id: str, status: str):
       if not frappe.has_permission("CustomDoc", "write", record_id):
           frappe.throw(_("Not permitted"), frappe.PermissionError)
       doc = frappe.get_doc("CustomDoc", record_id)
       doc.status = status
       doc.save()
       return doc.as_dict()
   ```
2. **HTTP Method Restriction**: Always specify `methods=["GET"]` or `methods=["POST"]`.
3. **Input Validation**: Use type annotations and explicit validation.
4. **Rate Limiting**: Apply `@frappe.rate_limit(limit=100, seconds=60)` on public endpoints.
