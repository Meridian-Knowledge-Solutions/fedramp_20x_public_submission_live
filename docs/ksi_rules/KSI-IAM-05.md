# KSI-IAM-05: Apply zero trust design principles

## Overview

**Category:** Identity and Access Management
**Status:** PASS
**Last Check:** 2025-09-12 02:36

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

PASS Comprehensive zero trust implementation (88%): PASS Modern identity platform: IAM Identity Center configured (1 instance(s))
- PASS Federated MFA enforcement: External IdP (Okta) enforces MFA upstream of AWS
- PASS External IdP provisioning: 9/9 users via SCIM (100%)
- PASS Okta identity provider: 9/9 users with Okta IDs (100%)
- PASS Complete federation coverage: 100% of users from external IdP
- PASS Excellent network micro-segmentation: 13 restrictive vs 1 permissive security groups (93% restrictive)
- PASS Role-based credentials: Using assumed role session
- PASS Comprehensive secure communications: 7 VPC endpoints configured (4 interface, 1 gateway, 2 gateway-lb)
- PASS Active continuous monitoring: CloudTrail 'meridianks-Management-events' actively logging

---
*Generated 2025-09-12 02:36 UTC*