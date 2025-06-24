# KSI-IAM-05: Apply zero trust design principles

## Overview

**Category:** Identity and Access Management
**Status:** PASS
**Last Check:** 2025-06-24 01:46

**What it validates:** Apply zero trust design principles

**Why it matters:** Validates comprehensive zero trust implementation through Identity Center (modern approach), network security, continuous monitoring, conditional access, and secure communications patterns

## Validation Method

1. `aws sso-admin list-instances --output json`
   *Check IAM Identity Center for modern zero trust user access patterns*

2. `aws cloudtrail describe-trails --output json`
   *Validate continuous monitoring and verification logging (must be active)*

3. `aws cloudtrail get-trail-status --name $(aws cloudtrail describe-trails --query 'trailList[0].Name' --output text) --output json 2>/dev/null || echo '{"IsLogging":false}'`
   *Verify CloudTrail is actively logging (zero trust requires continuous monitoring)*

4. `aws ec2 describe-security-groups --output json`
   *Analyze network micro-segmentation and least privilege network access*

5. `aws ec2 describe-vpc-endpoints --output json`
   *Validate secure private communications (VPC endpoints for AWS services)*

6. `aws iam list-virtual-mfa-devices --output json`
   *Check multi-factor authentication enforcement (verify explicitly principle)*

7. `aws sts get-caller-identity --output json`
   *Validate current session type (temporary credentials indicate zero trust access)*

## Latest Results

WARNING Moderate zero trust implementation (60%): PASS Modern identity platform: IAM Identity Center configured (1 instance(s))
- FAIL No MFA devices found (zero trust requires multi-factor authentication)
- PASS Network micro-segmentation: 12 restrictive vs 2 permissive security groups
- WARNING Unknown credential type
- PASS Secure private communications: 7 VPC endpoints configured
- WARNING CloudTrail 'meridianks-Management-events' excellently configured (multi-region, integrity-protected, encrypted, organization-wide) but not logging

---
*Generated 2025-06-24 01:46 UTC*