# KSI-RPL-03: Perform system backups aligned with recovery objectives

## Overview

**Category:** Recovery Planning
**Status:** FAIL
**Last Check:** 2025-09-20 02:58

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

FAIL Insufficient backup implementation: FAIL No AWS Backup plans found
- WARNING No backup execution data available for validation
- INFO No EBS snapshots (acceptable if using AWS Backup exclusively)

---
*Generated 2025-09-20 02:58 UTC*