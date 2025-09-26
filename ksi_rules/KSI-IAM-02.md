# KSI-IAM-02: Use secure passwordless methods for user authentication and authorization when feasible, otherwise enforce strong passwords with MFA

## Overview

**Category:** Identity and Access Management
**Status:** PASS
**Last Check:** 2025-09-26 17:30

**What it validates:** Use secure passwordless methods for user authentication and authorization when feasible, otherwise enforce strong passwords with MFA

**Why it matters:** Validates passwordless authentication (SSO/SAML/temporary credentials) where feasible, otherwise strong password policy with mandatory MFA enforcement

## Validation Method

1. `aws iam list-saml-providers --output json`
   *Check for federated authentication (passwordless method)*

2. `aws iam list-virtual-mfa-devices --output json`
   *Validate MFA device configuration and enforcement*

3. `aws iam get-account-password-policy --output json`
   *Check strong password policy enforcement when passwords are used*

4. `aws iam get-account-password-policy --output json || echo '{"PasswordPolicy": "No custom policy set, using AWS defaults."}'`
   *RESILIENT: Handles cases where no custom password policy exists by providing a default status.*

5. `aws sts get-caller-identity --output json`
   *Validate current authentication method (temporary vs permanent credentials)*

## Latest Results

PASS Excellent authentication security (passwordless methods): PASS 1 SAML providers configured (passwordless authentication)
- PASS Using temporary credentials (passwordless method)
- PASS Centralized MFA via SAML/IdP (traditional MFA not required)

---
*Generated 2025-09-26 17:30 UTC*