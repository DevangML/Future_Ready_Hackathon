---
name: bmad-erpnext-expert
description: 'Expert guidance and development patterns for ERPNext and Frappe Framework applications.'
---

# BMad ERPNext Expert

## Purpose
Provides deep domain expertise and development patterns for Frappe Framework and ERPNext.

## Core Capabilities
1. **DocType Architecture**: Standard, Custom, Single, and Child Table design with proper schema normalization.
2. **Controller Hooks**: Lifecycle hooks (`before_insert`, `validate`, `on_submit`, `on_cancel`, `on_trash`).
3. **Database Operations**: Optimized query patterns using `frappe.get_doc`, `frappe.db.get_value`, `frappe.db.set_value`, `frappe.get_all`, and parameterized `frappe.db.sql`.
4. **Business Logic Modules**:
   - Accounts (General Ledger, Invoicing, Tax Templates, Payment Entries)
   - Stock (Item Master, Stock Ledger, Batches, Serial Numbers, Warehouses)
   - Buying & Selling (Purchase Orders, Quotations, Sales Orders, Pricing Rules)
   - HRMS & Payroll (Employees, Leaves, Salary Structures, Payroll Runs)
5. **Background Jobs**: Safe asynchronous execution with `frappe.enqueue(queue='default', timeout=300)`.
6. **Client Scripts & UI**: Desk form scripting (`frappe.ui.form.on`), List formatting, and Custom Pages.
