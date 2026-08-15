---
name: frappe-desk-js-quality
description: 'Frontend JavaScript quality standards and event patterns for Frappe Desk form controllers and views.'
---

# Frappe Desk JS Quality

## Purpose
Ensures clean, maintainable, high-performance client-side JavaScript for Frappe Desk.

## Controller Pattern
```javascript
frappe.ui.form.on('Sales Invoice', {
    refresh(frm) {
        if (!frm.is_new() && frm.doc.status === 'Draft') {
            frm.add_custom_button(__('Approve'), () => {
                frm.call('approve_invoice').then(r => {
                    if (!r.exc) frm.reload_doc();
                });
            }, __('Actions'));
        }
    },
    customer(frm) {
        if (frm.doc.customer) {
            frm.trigger('fetch_customer_details');
        }
    }
});
```
## Quality Rules
- Avoid global variable pollution.
- Use `frm.call()` instead of raw `frappe.call()` for automatic UI busy states.
- Clean up event listeners on page destroy.
