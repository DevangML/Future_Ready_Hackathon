---
name: platform-security-review
description: 'Comprehensive security review methodology, threat modeling (STRIDE), and OWASP validation.'
---

# Platform Security Review

## Purpose
Framework for conducting structured, adversarial security reviews prior to release.

## Review Methodology
1. **STRIDE Threat Modeling**: Evaluate Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, and Elevation of Privilege.
2. **OWASP Top 10 Audit**: Verify defenses against Injection, Broken Authentication, Sensitive Data Exposure, and Broken Access Control.
3. **Secrets Auditing**: Scan for hardcoded credentials, API keys, or unencrypted sensitive fields.
4. **Sign-Off Gate**: Produce a formal security assessment report with risk score and remediation plan.
