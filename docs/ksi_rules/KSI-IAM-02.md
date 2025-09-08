# KSI-IAM-02: Use secure passwordless methods for user authentication and authorization when feasible, otherwise enforce strong passwords with MFA

## Overview

**Category:** Identity and Access Management
**Status:** PASS
<<<<<<< Updated upstream
**Last Check:** 2025-09-08 18:55
=======
**Last Check:** 2025-09-08 19:00
>>>>>>> Stashed changes

**What it validates:** Use secure passwordless methods for user authentication and authorization when feasible, otherwise enforce strong passwords with MFA

**Why it matters:** Validates passwordless authentication (SSO/SAML/temporary credentials) where feasible, otherwise strong password policy with mandatory MFA enforcement

## Validation Method

1. `aws iam list-saml-providers --output json`
   *Check for federated authentication (passwordless method)*

2. `aws iam list-virtual-mfa-devices --output json`
   *Validate MFA device configuration and enforcement*

3. `aws iam get-account-password-policy --output json`
   *Check strong password policy enforcement when passwords are used*

4. `aws iam list-users --output json`
   *Analyze user authentication patterns and requirements*

5. `aws sts get-caller-identity --output json`
   *Validate current authentication method (temporary vs permanent credentials)*

## Latest Results

PASS Excellent authentication security (passwordless methods): PASS 1 SAML providers configured (passwordless authentication)
- PASS Using temporary credentials (passwordless method)
- INFO No traditional MFA devices (not needed with SAML authentication)
- PASS No password policy needed (passwordless authentication in use)

---
<<<<<<< Updated upstream
*Generated 2025-09-08 18:55 UTC*
=======
*Generated 2025-09-08 19:00 UTC*
>>>>>>> Stashed changes
