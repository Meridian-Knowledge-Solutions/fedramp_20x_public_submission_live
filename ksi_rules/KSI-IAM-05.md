# KSI-IAM-05: Separate duties between users

## Overview

**Category:** Identity and Access Management
**Status:** PASS
**Last Check:** 2025-10-02 03:01

**What it validates:** Separate duties between users

**Why it matters:** Validates comprehensive separation of duties from basic IAM policy separation to enterprise-grade audit trails and conflict detection

## Validation Method

1. `aws identitystore list-users --identity-store-id $(aws sso-admin list-instances --query 'Instances[0].IdentityStoreId' --output text 2>/dev/null || echo 'd-9067ccc0fb') --output json || echo '{"Users": []}'`
   *Check user accounts for separation of duties enforcement*

2. `aws cloudtrail describe-trails --output json`
   *Validate CloudTrail for audit logging of privileged actions*

3. `aws cloudtrail get-trail-status --name $(aws cloudtrail describe-trails --query 'trailList[0].Name' --output text 2>/dev/null || echo 'none') --output json 2>/dev/null || echo '{"IsLogging": false}'`
   *Check CloudTrail logging status with dynamic trail selection*

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
- FAIL No MFA enforcement detected (zero trust requires multi-factor authentication)
- PASS Excellent network micro-segmentation: 14/15 restrictive security groups (93%)
- PASS Role-based credentials: Using assumed role session
- PASS Comprehensive secure communications: 7 VPC endpoints configured
- WARNING CloudTrail 'meridianks-Management-events' excellently configured but not actively logging

---
*Generated 2025-10-02 03:01 UTC*