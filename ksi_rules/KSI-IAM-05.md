# KSI-IAM-05: Apply zero trust design principles

## Overview

**Category:** Identity and Access Management
**Status:** PASS
**Last Check:** 2025-09-25 20:43

**What it validates:** Apply zero trust design principles

**Why it matters:** Validates comprehensive zero trust implementation through Identity Center (modern approach), federated MFA detection (consistent with IAM-01), network security, continuous monitoring, conditional access, and secure communications patterns

## Validation Method

1. `aws sso-admin list-instances --output json`
   *Check IAM Identity Center for modern zero trust user access patterns*

2. `aws identitystore list-users --identity-store-id $(aws sso-admin list-instances --query 'Instances[0].IdentityStoreId' --output text) --output json 2>/dev/null || echo '{"Users":[]}'`
   *List Identity Center users to detect federated MFA enforcement patterns (external IdP integration via SCIM/Okta)*

3. `aws cloudtrail describe-trails --output json`
   *Validate continuous monitoring and verification logging (must be active)*

4. `aws cloudtrail get-trail-status --name arn:aws:cloudtrail:us-east-1:155765116562:trail/meridianks-Management-events --output json`
   *Verify CloudTrail is actively logging (zero trust requires continuous monitoring)*

5. `aws ec2 describe-security-groups --output json`
   *Analyze network micro-segmentation and least privilege network access*

6. `aws ec2 describe-vpc-endpoints --output json`
   *Validate secure private communications (VPC endpoints for AWS services)*

7. `aws iam list-virtual-mfa-devices --output json`
   *Check traditional IAM MFA devices (fallback for non-federated scenarios)*

8. `aws sts get-caller-identity --output json`
   *Validate current session type (temporary credentials indicate zero trust access)*

## Latest Results

PASS Good zero trust implementation (62%): WARNING No IAM Identity Center - missing modern zero trust identity platform
- PASS Excellent network micro-segmentation: 14/15 restrictive security groups (93%)
- PASS Role-based credentials: Using assumed role session
- PASS Comprehensive secure communications: 7 VPC endpoints configured
- PASS Active continuous monitoring: CloudTrail 'meridianks-Management-events' actively logging

---
*Generated 2025-09-25 20:43 UTC*