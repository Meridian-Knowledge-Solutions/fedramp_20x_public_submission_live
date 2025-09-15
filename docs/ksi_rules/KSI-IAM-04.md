# KSI-IAM-04: Use a least-privileged, role and attribute-based, and just-in-time security authorization model for all user and non-user accounts and services

## Overview

**Category:** Identity and Access Management
**Status:** PASS
**Last Check:** 2025-09-15 04:13

**What it validates:** Use a least-privileged, role and attribute-based, and just-in-time security authorization model for all user and non-user accounts and services

**Why it matters:** Validates comprehensive authorization through IAM Identity Center permission sets (modern approach) and traditional IAM patterns for complete coverage of least privilege, role-based, attribute-based, and just-in-time access

## Validation Method

1. `aws sso-admin list-instances --output json`
   *Check for AWS IAM Identity Center (modern permission set approach)*

2. `INSTANCE_ARN=$(aws sso-admin list-instances --query 'Instances[0].InstanceArn' --output text 2>/dev/null) && aws sso-admin list-permission-sets --instance-arn "$INSTANCE_ARN" --output json 2>/dev/null || echo '{"PermissionSets":[]}'`
   *ROBUST: Get instance ARN first, then list permission sets with proper error handling*

3. `aws iam list-roles --output json`
   *Analyze traditional IAM roles for service accounts and legacy access patterns*

4. `aws iam list-users --output json`
   *Check if users have direct policy attachments (anti-pattern for least privilege)*

5. `aws sts get-caller-identity --output json`
   *Validate current session type (permission set session vs traditional credentials)*

6. `aws iam get-account-summary --output json`
   *Get account-wide IAM usage patterns for authorization model assessment*

## Latest Results

PASS Excellent modern authorization model (95%): PASS IAM Identity Center configured: 1 active instance(s)
- PASS Permission sets deployed: 2 sets (modern role-based access)
- PASS Modern authorization model: Permission sets provide role-based, attribute-based, and just-in-time access
- PASS Active permission sets: AdministratorAccess, ReadOnlyAccess
- PASS Role-based access pattern: 46 user-oriented roles vs 2 users (25 service roles)
- PASS Controlled user count: 2 users (excellent for least privilege)
- PASS Controlled policy count: 5 custom policies (good least privilege)
- PASS Role-based session: Using temporary credentials (just-in-time access)

---
*Generated 2025-09-15 04:13 UTC*