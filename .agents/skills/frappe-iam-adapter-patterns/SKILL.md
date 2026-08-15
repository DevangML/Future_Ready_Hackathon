---
name: frappe-iam-adapter-patterns
description: 'Identity and Access Management integration patterns for OAuth2, SAML, LDAP, and Token authentication.'
---

# Frappe IAM Adapter Patterns

## Purpose
Integrates Frappe with enterprise Identity Providers (IdP) and single sign-on (SSO) systems.

## Protocols Supported
- **OAuth2 / OIDC**: Configure Social Login Keys with standard claims (email, sub, roles).
- **SAML 2.0**: Enterprise assertion consumer service with signature verification.
- **LDAP / Active Directory**: User sync hooks on login with TLS connection pooling.
- **API Token Auth**: Bearer token header parsing `Authorization: token api_key:api_secret`.
