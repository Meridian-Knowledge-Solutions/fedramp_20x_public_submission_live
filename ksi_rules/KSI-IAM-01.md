# KSI-IAM-01: Enforce multi-factor authentication (MFA) using methods that are difficult to intercept or impersonate (phishing-resistant MFA) for all user authentication

## Overview

**Category:** Identity and Access Management
**Status:** FAIL
**Last Check:** 2025-09-26 05:07

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

- FAIL No centralized identity management detected: FAIL No active AWS Identity Center - MFA enforcement unclear

---
*Generated 2025-09-26 05:07 UTC*