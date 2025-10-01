# KSI-SVC-06: Use centralized key management services

## Overview

**Category:** Service Configuration
**Status:** PASS
**Last Check:** 2025-10-01 08:13

**What it validates:** Use centralized key management services

**Why it matters:** Validates comprehensive key management from basic KMS to enterprise-grade certificate lifecycle, rotation, and cryptographic compliance

## Validation Method

1. `aws kms list-keys --output json`
   *Check KMS keys for centralized encryption key management*

2. `aws acm list-certificates --output json`
   *Validate ACM certificates for centralized certificate management*

3. `aws kms list-aliases --output json`
   *Check KMS key aliases for key organization and management*

4. `aws ssm describe-parameters --parameter-filters Key=Type,Values=SecureString --output json`
   *Validate SSM SecureString parameters using KMS encryption*

5. `aws secretsmanager list-secrets --output json`
   *Check Secrets Manager for KMS-encrypted secret storage*

6. `aws iam list-server-certificates --output json`
   *Validate IAM server certificates and migration to ACM*

7. `aws cloudformation list-stacks --stack-status-filter CREATE_COMPLETE UPDATE_COMPLETE --output json`
   *Check CloudFormation for infrastructure as code key management*

8. `aws cloudtrail lookup-events --lookup-attributes AttributeKey=ResourceType,AttributeValue=AWS::KMS::Key --max-items 20 --output json`
   *Validate CloudTrail audit logs for key usage and management*

9. `aws organizations describe-organization --output json`
   *Check organization-wide centralized key management policies*

## Latest Results

PASS Enterprise-grade comprehensive automated key management governance with rotation (90%): PASS Automated key management infrastructure: 17 KMS keys (0 customer-managed, 17 AWS-managed).
- PASS Automated certificate management: 1/2 ACM certificates are active.
- PASS Key governance structure: 6 customer-managed KMS aliases.
- PASS Automated encryption integration: 4 KMS-encrypted SecureString parameters.
- PASS Automated credential rotation: 1/1 secrets with automatic rotation (100%).
- PASS Modern certificate management: No legacy IAM certificates.
- PASS Infrastructure as Code key management: 12/12 successful CloudFormation stacks.
- PASS Key management audit trail: 20 recent key management events tracked.
- PASS Enterprise-wide key management governance: AWS Organizations enables centralized key policies.
- PASS Advanced organization features: SCPs for key management policy enforcement enabled.

---
*Generated 2025-10-01 08:13 UTC*