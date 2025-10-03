# KSI-IAM-04: Clearly define user roles and implement user-to-role mapping

## Overview

**Category:** Identity and Access Management
**Status:** PASS
**Last Check:** 2025-10-03 22:39

**What it validates:** Clearly define user roles and implement user-to-role mapping

**Why it matters:** Validates comprehensive user role mapping from basic IAM groups to enterprise-grade permission sets and centralized access management

## Validation Method

1. `INSTANCE_ARN=$(aws sso-admin list-instances --query 'Instances[0].InstanceArn' --output text 2>/dev/null || echo 'none'); if [ "$INSTANCE_ARN" != "none" ]; then aws sso-admin list-permission-sets --instance-arn "$INSTANCE_ARN" --output json; else echo '{"PermissionSets": []}'; fi`
   *Check SSO permission sets for role-based access mapping*

2. `aws iam list-roles --output json`
   *Validate IAM roles with clear purpose and user mapping*

3. `aws iam list-users --output json`
   *Check IAM users and their role assignments*

4. `aws sts get-caller-identity --output json`
   *Validate current identity and role assumption*

5. `aws iam get-account-summary --output json`
   *Check account-level role and user statistics*

## Latest Results

WARNING Partial traditional authorization model (50%): INFO IAM Identity Center not configured (using traditional IAM)
- PASS Role-based access pattern: 63 user-oriented roles vs 3 users (27 service roles)
- PASS Controlled user count: 3 users (excellent for least privilege)
- PASS Moderate policy count: 15 custom policies
- PASS Role-based session: Using temporary credentials (just-in-time access)

---
*Generated 2025-10-03 22:39 UTC*