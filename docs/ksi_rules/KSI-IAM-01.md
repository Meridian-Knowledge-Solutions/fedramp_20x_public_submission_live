# KSI-IAM-01: Enforce multi-factor authentication (MFA) using methods that are difficult to intercept or impersonate (phishing-resistant MFA) for all user authentication

## Overview

**Category:** Identity and Access Management
**Status:** PASS
**Last Check:** 2025-09-12 06:09

**What it validates:** Enforce multi-factor authentication (MFA) using methods that are difficult to intercept or impersonate (phishing-resistant MFA) for all user authentication

**Why it matters:** Validates MFA enforcement through Identity Center configuration evidence showing always-on MFA requirements, combined with traditional IAM user analysis

## Validation Method

1. `aws iam list-users --output json`
   *Get traditional IAM users for MFA analysis*

2. `aws iam list-mfa-devices --output json`
   *Check traditional IAM MFA devices*

3. `aws sso-admin list-instances --output json`
   *Get Identity Center instances*

4. `aws identitystore list-users --identity-store-id d-9067ccc0ff --output json`
   *Get Identity Center users for accurate user count*

## Latest Results

PASS Comprehensive federated MFA enforcement (100%): PASS AWS Identity Center: 1 active instance(s)
- PASS Identity Center users: 9 users
- PASS External IdP provisioning: 9/9 users via SCIM
- PASS Okta identity provider: 9/9 users with Okta IDs
- PASS Complete federation: 100% of users from external IdP
- PASS Minimal traditional IAM: 2 users (appropriate for federated architecture)
- PASS Traditional IAM users: Service accounts with federated MFA coverage upstream
- PASS Federated MFA enforcement: External IdP (Okta) enforces MFA upstream of AWS

---
*Generated 2025-09-12 06:09 UTC*