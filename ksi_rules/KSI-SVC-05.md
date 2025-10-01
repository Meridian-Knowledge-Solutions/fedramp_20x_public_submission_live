# KSI-SVC-05: Use logging and monitoring to detect abnormal changes to configuration

## Overview

**Category:** Service Configuration
**Status:** PASS
**Last Check:** 2025-10-01 22:14

**What it validates:** Use logging and monitoring to detect abnormal changes to configuration

**Why it matters:** Validates comprehensive configuration monitoring from basic CloudTrail to enterprise-grade automated detection and response

## Validation Method

1. `aws cloudtrail describe-trails --output json`
   *Check CloudTrail for configuration change audit logging*

2. `aws kms list-keys --output json`
   *Validate KMS encryption for secure log storage*

3. `aws kms list-aliases --output json`
   *Check KMS key aliases for log encryption management*

4. `aws s3api list-buckets --output json`
   *Validate S3 buckets for CloudTrail log storage*

5. `aws rds describe-db-instances --output json`
   *Check RDS configuration change logging*

6. `aws configservice describe-configuration-recorders --output json`
   *Validate Config recorders for continuous configuration monitoring*

7. `aws cloudwatch describe-alarms --output json`
   *Check CloudWatch alarms for configuration change alerts*

8. `aws sns list-topics --output json`
   *Validate SNS topics for configuration change notifications*

9. `aws backup list-backup-vaults --output json`
   *Check backup configurations for disaster recovery*

10. `aws organizations describe-organization --output json`
   *Validate organization-wide configuration monitoring policies*

## Latest Results

PASS Enterprise-grade comprehensive cryptographic integrity governance with monitoring (95%): PASS Audit integrity foundation: 1/1 CloudTrail trails with log file validation.
- PASS Cryptographic infrastructure: 17 KMS keys available.
- PASS Key management governance: 6 customer-managed KMS aliases.
- PASS Object integrity capability: 7 S3 buckets available for versioning and integrity protection.
- PASS Database integrity: 1/1 RDS instances with encrypted storage.
- PASS Configuration integrity: 1 active Config recorders.
- PASS Backup integrity: 3/3 encrypted backup vaults.
- PASS Integrity monitoring: 1 CloudWatch alarms for integrity violations.
- PASS Integrity notification infrastructure: 9 SNS topics for event communication.
- PASS Enterprise-wide integrity governance: AWS Organizations enables centralized policies.
- PASS Advanced organization features: SCPs for integrity policy enforcement enabled.

---
*Generated 2025-10-01 22:14 UTC*