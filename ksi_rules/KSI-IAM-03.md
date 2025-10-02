# KSI-IAM-03: Implement least privilege access via role-based access control policies

## Overview

**Category:** Identity and Access Management
**Status:** PASS
**Last Check:** 2025-10-02 03:01

**What it validates:** Implement least privilege access via role-based access control policies

**Why it matters:** Validates comprehensive RBAC from basic IAM policies to enterprise-grade dynamic permissions and automated access reviews

## Validation Method

1. `aws iam list-roles --output json`
   *Check IAM roles for least privilege RBAC implementation*

2. `aws iam list-users --output json`
   *Validate IAM users have minimal direct permissions (prefer roles)*

3. `aws ec2 describe-instances --query 'Reservations[*].Instances[*].[InstanceId,IamInstanceProfile.Arn]' --output json`
   *Check EC2 instances using IAM roles for RBAC*

## Latest Results

WARNING Basic service authentication security (75%): PASS Secure foundation: 89 IAM roles available for service authentication (38 are service-linked).
- WARNING High Risk: 1 IAM user(s) found that appear to be service accounts (change_template_approver). These should be converted to IAM Roles.
- PASS Identity Best Practice: No human IAM users with console passwords detected.
- PASS EC2 Best Practice: All 6 instance(s) are correctly using IAM Instance Profiles.

---
*Generated 2025-10-02 03:01 UTC*