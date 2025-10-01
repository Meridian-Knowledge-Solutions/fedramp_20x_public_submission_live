# KSI-IAM-01: Implement phishing-resistant multi-factor authentication for all users

## Overview

**Category:** Identity and Access Management
**Status:** FAIL
**Last Check:** 2025-10-01 06:31

**What it validates:** Implement phishing-resistant multi-factor authentication for all users

**Why it matters:** Validates phishing-resistant MFA implementation from basic virtual MFA to enterprise-grade hardware tokens and passwordless authentication

## Validation Method

1. `aws iam list-users --output json`
   *Check IAM users for MFA configuration requirements*

2. `for user in $(aws iam list-users --query 'Users[].UserName' --output text); do echo "User: $user"; aws iam list-mfa-devices --user-name "$user" --output json; done`
   *List MFA devices for all IAM users to verify phishing-resistant MFA*

3. `aws identitystore list-users --identity-store-id d-9067ccc0fb --output json || echo '{"Users": []}'`
   *Check Identity Center users for centralized MFA enforcement*

## Latest Results

FAIL Insufficient phishing-resistant MFA (0%): INFO Traditional IAM: 2 human user(s)
- WARNING Traditional IAM users without MFA devices

---
*Generated 2025-10-01 06:31 UTC*