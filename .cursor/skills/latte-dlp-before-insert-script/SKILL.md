---
name: latte-dlp-before-insert-script
description: 'Data Loss Prevention (DLP) hooks for Frappe to detect, mask, and encrypt sensitive PII/PHI data.'
---

# Latte DLP Before Insert Script

## Purpose
Inspects incoming document fields during `before_insert` and `before_save` hooks to safeguard sensitive data.

## Pattern Implementation
```python
import re
import frappe

PII_PATTERNS = {
    'credit_card': r'(?:\d{4}[ -]?){3}\d{4}',
    'ssn_aadhaar': r'\d{4}\s\d{4}\s\d{4}',
    'email': r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
}

def scan_and_mask_pii(doc, method=None):
    for field, val in doc.as_dict().items():
        if isinstance(val, str):
            for pii_type, regex in PII_PATTERNS.items():
                if re.search(regex, val):
                    frappe.log_error(f"DLP Alert: {pii_type} detected in {doc.doctype}.{field}", "DLP Event")
                    # Apply masking or encryption as configured
```
