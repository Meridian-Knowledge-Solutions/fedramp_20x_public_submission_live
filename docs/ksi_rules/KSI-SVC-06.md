# KSI-SVC-06: Use automated key management systems to manage, protect, and regularly rotate digital keys and certificates

## Overview

**Category:** Service Configuration
**Status:** PASS
**Last Check:** 2025-09-13 04:08

**What it validates:** Use automated key management systems to manage, protect, and regularly rotate digital keys and certificates

**Why it matters:** Validates comprehensive automated key management from basic KMS availability to enterprise-grade key lifecycle management, covering encryption keys, certificates, rotation policies, access controls, hardware security modules, and organizational key governance with automated provisioning and compliance monitoring

## Validation Method

1. `aws kms list-keys --output json`
   *Check KMS keys for automated key management and cryptographic service availability*

2. `aws acm list-certificates --output json`
   *Validate ACM certificates for automated certificate lifecycle management and SSL/TLS provisioning*

3. `aws kms list-aliases --output json`
   *Analyze KMS key aliases for key management governance and organizational naming standards*

4. `aws ssm describe-parameters --parameter-filters Key=Type,Values=SecureString --output json`
   *Check Systems Manager SecureString parameters for KMS-encrypted configuration management*

5. `aws secretsmanager list-secrets --output json`
   *Validate Secrets Manager for automated secrets rotation and centralized credential management*

6. `aws iam list-server-certificates --output json`
   *Check IAM server certificates for legacy certificate management and migration tracking*

7. `aws cloudformation list-stacks --stack-status-filter CREATE_COMPLETE UPDATE_COMPLETE --output json`
   *Analyze CloudFormation stacks for Infrastructure as Code key management and automated provisioning*

8. `aws config describe-config-rules --output json`
   *Check Config rules for key management compliance monitoring and policy enforcement*

9. `aws cloudtrail lookup-events --lookup-attributes AttributeKey=EventName,AttributeValue=CreateKey --start-time 2025-05-01 --output json`
   *Validate key management audit trail for creation, rotation, and access tracking*

10. `aws organizations describe-organization --output json`
   *Check enterprise-wide key management policies and organizational governance standards across accounts*

## Latest Results

PASS Enterprise-grade comprehensive automated key management governance with rotation (90%): PASS Automated key management infrastructure: 14 KMS keys (0 customer-managed, 14 AWS-managed)
- PASS Automated certificate management: 2 ACM certificates (2 issued, 0 pending)
- PASS Key governance structure: 6/23 customer-managed aliases (26%)
- PASS Automated encryption integration: 4 KMS-encrypted SecureString parameters
- PASS Automated credential rotation: 1/1 secrets with automatic rotation (100%)
- PASS Modern certificate management: No legacy IAM certificates
- PASS Infrastructure as Code key management: 10/10 successful CloudFormation stacks (100%)
- INFO No Config rules for key management compliance monitoring
- PASS Key management audit trail: 2 recent key management events tracked
- PASS Enterprise-wide key management governance: AWS Organizations enables centralized key policies
- PASS Advanced organization features: SCPs for key management policy enforcement enabled

---
*Generated 2025-09-13 04:08 UTC*