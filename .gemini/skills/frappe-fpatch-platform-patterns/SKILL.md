---
name: frappe-fpatch-platform-patterns
description: 'Hotfix and runtime monkey-patching patterns for safe, reversible extension of Frappe core methods.'
---

# Frappe FPatch Platform Patterns

## Purpose
Enables safe, non-destructive runtime patching of Frappe methods without modifying upstream core files.

## Pattern Architecture
```python
import functools
import frappe

def patch_method(target_module, method_name):
    def decorator(custom_fn):
        original_fn = getattr(target_module, method_name)
        @functools.wraps(original_fn)
        def wrapper(*args, **kwargs):
            return custom_fn(original_fn, *args, **kwargs)
        setattr(target_module, method_name, wrapper)
        return wrapper
    return decorator
```
## Rules
- Always preserve original function reference.
- Log all patch executions for debuggability.
- Provide reversible unpatch hooks.
