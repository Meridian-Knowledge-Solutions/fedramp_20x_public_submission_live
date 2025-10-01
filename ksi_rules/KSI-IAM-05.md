# KSI-IAM-05: Separate duties between users

## Overview

**Category:** Identity and Access Management
**Status:** PASS
**Last Check:** 2025-10-01 06:31

**What it validates:** Separate duties between users

**Why it matters:** Validates comprehensive separation of duties from basic IAM policy separation to enterprise-grade audit trails and conflict detection

## Validation Method

1. `aws identitystore list-users --identity-store-id $(aws sso-admin list-instances --query 'Instances[0].IdentityStoreId' --output text 2>/dev/null || echo 'd-9067ccc0fb') --output json || echo '{"Users": []}'`
   *Check user accounts for separation of duties enforcement*

2. `aws cloudtrail describe-trails --output json`
   *Validate CloudTrail for audit logging of privileged actions*

3. `aws cloudtrail get-trail-status --name arn:aws:cloudtrail:us-east-1:893894210484:trail/management-events --output json`
   *Check active CloudTrail monitoring for separation of duties violations*

4. `aws ec2 describe-security-groups --output json`
   *Validate network security separation and access controls*

5. `aws ec2 describe-vpc-endpoints --output json`
   *Check VPC endpoints for private service access separation*

6. `aws iam list-virtual-mfa-devices --output json`
   *Validate MFA enforcement for privileged user separation*

7. `aws sts get-caller-identity --output json`
   *Check current identity role and separation context*

## Latest Results

PASS Good zero trust implementation (58%): WARNING No IAM Identity Center - missing modern zero trust identity platform
- PASS Excellent network micro-segmentation: 14/15 restrictive security groups (93%)
- PASS Role-based credentials: Using assumed role session
- PASS Comprehensive secure communications: 7 VPC endpoints configured
- WARNING CloudTrail 'meridianks-Management-events' excellently configured but not actively logging

---
*Generated 2025-10-01 06:31 UTC*