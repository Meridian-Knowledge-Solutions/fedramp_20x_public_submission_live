# KSI-IAM-03: Enforce appropriately secure authentication methods for non-user accounts and services

## Overview

**Category:** Identity and Access Management
**Status:** PASS
**Last Check:** 2025-09-16 00:12

**What it validates:** Enforce appropriately secure authentication methods for non-user accounts and services

**Why it matters:** Validates service accounts use appropriate authentication methods (roles, not long-term keys) and detects insecure patterns

## Validation Method

1. `aws iam list-roles --output json`
   *Check IAM roles for service authentication (primary secure method)*

2. `aws iam list-users --output json`
   *Identify potential service users who should be using roles instead*

3. `aws iam list-access-keys --output json`
   *Detect long-term access keys that may indicate insecure service authentication*

4. `aws ec2 describe-instances --query 'Reservations[*].Instances[*].IamInstanceProfile' --output json`
   *Validate EC2 instances use instance profiles for secure service authentication*

## Latest Results

WARNING Mostly secure service authentication (room for improvement): PASS 71 IAM roles available (33 service-oriented)
- PASS 2 users found, none appear to be service accounts
- PASS No access key information accessible
- INFO No EC2 instance profile information available

---
*Generated 2025-09-16 00:12 UTC*