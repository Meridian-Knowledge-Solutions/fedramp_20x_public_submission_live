# KSI-IAM-03: Enforce appropriately secure authentication methods for non-user accounts and services

## Overview

**Category:** Identity and Access Management
**Status:** PASS
**Last Check:** 2025-09-23 20:55

**What it validates:** Enforce appropriately secure authentication methods for non-user accounts and services

**Why it matters:** Validates service accounts use appropriate authentication methods (roles, not long-term keys) and detects insecure patterns

## Validation Method

1. `aws iam list-roles --output json`
   *Check IAM roles for service authentication (primary secure method)*

2. `aws iam list-users --output json`
   *Identify users to check for insecure patterns (service user names, long-term keys)*

3. `aws ec2 describe-instances --query 'Reservations[*].Instances[*].IamInstanceProfile' --output json`
   *Validate EC2 instances use instance profiles for secure service authentication*

## Latest Results

WARNING Basic service authentication security (75%): PASS Secure foundation: 81 IAM roles available for service authentication (36 are service-linked).
- WARNING High Risk: 1 IAM user(s) found that appear to be service accounts (change_template_approver). These should be converted to IAM Roles.
- PASS Identity Best Practice: No human IAM users with console passwords detected.
- PASS EC2 Best Practice: All 6 instance(s) are correctly using IAM Instance Profiles.

---
*Generated 2025-09-23 20:55 UTC*