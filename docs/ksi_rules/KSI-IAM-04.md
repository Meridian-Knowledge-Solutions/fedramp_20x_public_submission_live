# KSI-IAM-04: Use a least-privileged, role and attribute-based, and just-in-time security authorization model for all user and non-user accounts and services

## Overview

**Category:** Identity and Access Management
**Status:** PASS
**Last Check:** 2025-06-23 09:42

**What it validates:** Use a least-privileged, role and attribute-based, and just-in-time security authorization model for all user and non-user accounts and services

**Why it matters:** Validates comprehensive authorization through IAM Identity Center permission sets (modern approach) and traditional IAM patterns for complete coverage of least privilege, role-based, attribute-based, and just-in-time access

## Validation Method

1. `aws sso-admin list-instances --output json`
   *Check for AWS IAM Identity Center (modern permission set approach)*

2. `aws sso-admin list-permission-sets --instance-arn $(aws sso-admin list-instances --query 'Instances[0].InstanceArn' --output text) --output json 2>/dev/null || echo '{"PermissionSets":[]}'`
   *List permission sets for role-based and attribute-based access validation*

3. `aws iam list-roles --output json`
   *Analyze traditional IAM roles for service accounts and legacy access patterns*

4. `aws iam list-users --output json`
   *Check if users have direct policy attachments (anti-pattern for least privilege)*

5. `aws sts get-caller-identity --output json`
   *Validate current session type (permission set session vs traditional credentials)*

6. `aws iam get-account-summary --output json`
   *Get account-wide IAM usage patterns for authorization model assessment*

## Latest Results

PASS Good traditional authorization model (60%) - consider upgrading to IAM Identity Center: PASS IAM Identity Center configured: 1 instance(s)
- WARNING IAM Identity Center configured but no permission sets found
- PASS Traditional role-based access: 53 roles (31 service, 22 user-oriented) vs 2 users
- PASS Controlled user count: 2 users (appropriate for least privilege)
- PASS Controlled policy count: 2 custom policies
- WARNING Direct user session: Not using just-in-time access (consider SSO)

---
*Generated 2025-06-23 09:42 UTC*