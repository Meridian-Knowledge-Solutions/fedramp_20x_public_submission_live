# KSI-SVC-03: Encrypt all federal and sensitive information at rest

## Overview

**Category:** Service Configuration
**Status:** PASS
**Last Check:** 2025-09-16 04:08

**What it validates:** Encrypt all federal and sensitive information at rest

**Why it matters:** Validates comprehensive at-rest encryption from basic storage service availability to enterprise-grade multi-service encryption, covering object storage, block storage, databases, data lakes, backup systems, and managed services with automated key management and compliance monitoring

## Validation Method

1. `aws s3api list-buckets --output json`
   *Get S3 buckets for object storage encryption validation and federal data protection*

2. `aws ec2 describe-volumes --output json`
   *Check EBS volume encryption status for block storage and instance data protection*

3. `aws rds describe-db-instances --output json`
   *Validate RDS database encryption for structured data at rest and backup encryption*

4. `aws rds describe-db-snapshots --owner-type self --output json`
   *Check RDS snapshot encryption for database backup and recovery data protection*

5. `aws efs describe-file-systems --output json`
   *Check Elastic File System encryption for shared storage and distributed application data*

6. `aws backup list-backup-vaults --output json`
   *Validate AWS Backup vault encryption for centralized backup data protection and compliance*

7. `aws kms list-keys --output json`
   *Check KMS key management for enterprise encryption key governance and automated key rotation*

## Latest Results

PASS Advanced at-rest encryption across multiple storage services (45%): PASS Object storage encryption: 4 S3 buckets configured (encryption validation requires bucket-level check)
- PASS Block storage encryption: 10/10 EBS volumes encrypted (100%)
- PASS Database encryption: 1/1 RDS instances encrypted (100%)
- PASS Backup encryption: 3/3 backup vaults encrypted (100%)
- PASS Encryption key infrastructure: 14 KMS keys (0 customer-managed, 14 AWS-managed)
- INFO Single-account deployment (appropriate for pilot/development)

---
*Generated 2025-09-16 04:08 UTC*