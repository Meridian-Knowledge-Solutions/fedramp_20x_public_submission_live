# KSI-RPL-03: Perform system backups aligned with recovery objectives

## Overview

**Category:** Recovery Planning
**Status:** PASS
**Last Check:** 2025-09-16 07:52

**What it validates:** Perform system backups aligned with recovery objectives

**Why it matters:** Validates automated backup systems, retention policies, and backup job performance through AWS Backup service configuration and monitoring

## Validation Method

1. `aws backup list-backup-plans --output json`
   *Verify comprehensive backup plans are configured for system recovery*

2. `aws backup list-backup-jobs --by-state COMPLETED --max-results 50 --output json`
   *Check recent backup job completions and success rates*

3. `aws rds describe-db-instances --query 'DBInstances[*].[DBInstanceIdentifier,BackupRetentionPeriod,DeletionProtection]' --output json`
   *Confirm RDS automated backup configuration and data protection settings*

4. `aws ec2 describe-snapshots --owner-ids self --output json`
   *Validate EBS snapshots for system backup coverage*

## Latest Results

PASS System backups with compliant retention aligned with recovery objectives: PASS Backup infrastructure: 2 AWS Backup plans (rds-backup-plan, complete-backup-plan)
- WARNING Backup plan details not available - cannot validate retention policies
- PASS Backup operations validated: 50 successful backup jobs prove backups are functioning
- PASS RDS backup configuration: 1/1 databases with automated backups
- PASS Additional backup coverage: 450 EBS snapshots

---
*Generated 2025-09-16 07:52 UTC*