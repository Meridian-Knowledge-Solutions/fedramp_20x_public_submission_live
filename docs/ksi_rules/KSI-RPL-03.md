# KSI-RPL-03: Perform system backups aligned with recovery objectives

## Overview

**Category:** Recovery Planning
**Status:** FAIL
**Last Check:** 2025-06-24 02:05

**What it validates:** Perform system backups aligned with recovery objectives

**Why it matters:** Validates comprehensive backup implementation through AWS Backup, EBS snapshots, and RDS backups with retention policies and operational evidence

## Validation Method

1. `aws backup list-backup-plans --output json`
   *Check AWS Backup plans for systematic backup implementation*

2. `aws backup get-backup-plan --backup-plan-id $(aws backup list-backup-plans --query 'BackupPlansList[0].BackupPlanId' --output text) --output json`
   *Get detailed backup plan configuration including retention policies*

3. `aws backup list-backup-jobs --by-state COMPLETED --max-results 20 --output json`
   *Validate recent successful backup operations and timing to prove backups are functioning*

4. `aws rds describe-db-instances --query 'DBInstances[*].[DBInstanceIdentifier,BackupRetentionPeriod,DeletionProtection]' --output json`
   *Confirm RDS automated backup configuration and data protection settings*

5. `aws ec2 describe-snapshots --owner-ids self --output json`
   *Validate EBS snapshots for system backup coverage*

## Latest Results

- Exception during evaluation: 'list' object has no attribute 'get'

---
*Generated 2025-06-24 02:05 UTC*