---
name: frappe-trishul-devops-patterns
description: 'DevOps automation, containerization, Helm charts, and CI/CD deployment pipelines for Frappe Bench.'
---

# Frappe Trishul DevOps Patterns

## Purpose
Enterprise CI/CD and Kubernetes deployment architectures for Frappe/ERPNext applications.

## Standards
1. **Container Builds**: Multi-stage Dockerfiles separating build assets from lean production runtime.
2. **Database Migration Locks**: Acquire distributed Redis locks during `bench migrate` to prevent race conditions.
3. **Zero-Downtime Rollouts**: Blue-Green and Canary deployments using Kubernetes Ingress routing.
4. **Health Checks**: Configure liveness and readiness probes on `/api/method/frappe.ping`.
