# KSI-RPL-03: Back up information regularly per the recovery point objective

## Overview

**Category:** Recovery Planning
**Status:** FAIL
**Last Check:** 2025-10-01 06:31

**What it validates:** Back up information regularly per the recovery point objective

**Why it matters:** Validates comprehensive backup execution from basic scheduled backups to enterprise-grade continuous data protection and multi-region replication

## Validation Method

1. `aws backup list-backup-plans --output json`
   *Check AWS Backup plans for regular backup schedules*

2. `PLAN_ID=$(aws backup list-backup-plans --query 'BackupPlansList[0].BackupPlanId' --output text 2>/dev/null || echo 'none'); if [ "$PLAN_ID" != "none" ]; then aws backup get-backup-plan --backup-plan-id "$PLAN_ID" --output json; else echo '{"BackupPlan": null}'; fi`
   *Validate backup plan schedules and retention policies*

3. `aws backup list-backup-jobs --by-state COMPLETED --max-results 50 --output json`
   *Check recent completed backup jobs for RPO compliance*

4. `aws rds describe-db-instances --query 'DBInstances[*].[DBInstanceIdentifier,PreferredBackupWindow,BackupRetentionPeriod]' --output json`
   *Validate RDS automated backup configurations*

5. `aws ec2 describe-snapshots --owner-ids self --output json`
   *Check EBS snapshots for volume backup coverage*

## Latest Results

- Exception during evaluation: '>' not supported between instances of 'str' and 'int'

---
*Generated 2025-10-01 06:31 UTC*