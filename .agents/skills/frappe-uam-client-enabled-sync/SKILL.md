---
name: frappe-uam-client-enabled-sync
description: 'User Access Management client-enabled synchronization and permission cache invalidation in Frappe.'
---

# Frappe UAM Client Enabled Sync

## Purpose
Manages real-time synchronization of user permissions, role profiles, and client-side session state.

## Patterns
1. **Boot Info Sync**: Inject customized role and permission payloads during `boot_session`.
2. **Permission Invalidation**: Hook into `User Permission` changes to trigger `frappe.clear_user_permissions(user)`.
3. **Client Cache Reload**: Broadcast realtime socket events (`frappe.publish_realtime('permission_updated')`) to refresh desk views.
