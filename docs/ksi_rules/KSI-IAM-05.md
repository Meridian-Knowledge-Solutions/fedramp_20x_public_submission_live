# KSI-IAM-05: Apply zero trust design principles

## Overview

**Category:** Identity and Access Management
**Status:** PASS
**Last Check:** 2025-06-25 09:11

**What it validates:** Apply zero trust design principles

**Why it matters:** Validates comprehensive zero trust implementation through Identity Center (modern approach), federated MFA detection (consistent with IAM-01), network security, continuous monitoring, conditional access, and secure communications patterns

## Validation Method

1. `aws sso-admin list-instances --output json`
   *Check IAM Identity Center for modern zero trust user access patterns*

2. `aws identitystore list-users --identity-store-id $(aws sso-admin list-instances --query 'Instances[0].IdentityStoreId' --output text) --output json 2>/dev/null || echo '{"Users":[]}'`
   *List Identity Center users to detect federated MFA enforcement patterns (external IdP integration via SCIM/Okta)*

3. `aws cloudtrail describe-trails --output json`
   *Validate continuous monitoring and verification logging (must be active)*

4. `aws cloudtrail get-trail-status --name $(aws cloudtrail describe-trails --query 'trailList[0].Name' --output text) --output json 2>/dev/null || echo '{"IsLogging":false}'`
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

WARNING Basic zero trust elements (33%): WARNING No IAM Identity Center - missing modern zero trust identity platform
- FAIL No MFA enforcement detected (zero trust requires multi-factor authentication)
- PASS Network micro-segmentation: 13 restrictive vs 1 permissive security groups
- WARNING Unknown credential type
- PASS Secure private communications: 7 VPC endpoints configured
- FAIL No CloudTrail monitoring configured

---
*Generated 2025-06-25 09:11 UTC*