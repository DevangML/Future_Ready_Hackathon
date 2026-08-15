---
name: frappe-platform-operations
description: 'Operations guide and automation patterns for Frappe Bench, site management, database, and background workers.'
---

# Frappe Platform Operations

## Purpose
Standardizes bench administration, multi-tenancy, migrations, and worker management for Frappe applications.

## Standard Operations
1. **Site Management**:
   ```bash
   bench new-site site1.local --admin-password admin --db-root-password root
   bench --site site1.local install-app custom_app
   bench --site site1.local migrate
   ```
2. **Background Workers & Scheduler**:
   - Enable scheduler: `bench --site site1.local enable-scheduler`
   - Monitor queues: `bench doctor`
3. **Database Maintenance**:
   - Backup: `bench --site site1.local backup --with-files`
   - Restore: `bench --site site1.local restore /path/to/database.sql.gz`
