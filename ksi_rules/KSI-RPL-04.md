# KSI-RPL-04: Regularly test the capability to recover from incidents and contingencies

## Overview

**Category:** Recovery Planning
**Status:** PASS
**Last Check:** 2025-09-29 22:00

**What it validates:** Regularly test the capability to recover from incidents and contingencies

**Why it matters:** Validates recovery testing through historical restore operations, backup job performance metrics, and documented test procedures with actual results

## Validation Method

1. `aws backup list-restore-jobs --max-results 20 --output json`
   *Document historical restore operations proving actual recovery testing has been performed*

2. `aws backup list-backup-jobs --by-state COMPLETED --by-created-after 2024-05-01 --output json`
   *Show recent backup completions with timing data to validate recovery time objectives*

3. `aws rds describe-db-instances --query 'DBInstances[*].[DBInstanceIdentifier,LatestRestorableTime,PreferredBackupWindow]' --output json`
   *Verify point-in-time recovery capability and backup timing for recovery testing validation*

4. `aws backup describe-restore-job --restore-job-id $(aws backup list-restore-jobs --query 'RestoreJobs[0].RestoreJobId' --output text) --query '[Status,CreationDate,CompletionDate,RecoveryPointArn]' --output json 2>/dev/null || echo '{"RestoreJobStatus": "NOT_FOUND"}'`
   *Analyze most recent restore job performance for recovery testing validation*

5. `aws ssm describe-instance-associations --instance-id $(aws ec2 describe-instances --filters 'Name=tag:Environment,Values=test' --query 'Reservations[0].Instances[0].InstanceId' --output text) --query 'Associations[*].[Name,AssociationId,Status.Name,LastExecutionDate]' --output json 2>/dev/null || echo '{"Associations": []}'`
   *Check Systems Manager associations for automated recovery testing scripts*

6. `aws lambda invoke --function-name automated-recovery-test --payload '{"test_type":"backup_restore"}' /tmp/response.json --query 'StatusCode' --output text 2>/dev/null && cat /tmp/response.json 2>/dev/null || echo '{"error": "Recovery test function not configured"}'`
   *Execute automated recovery test function and retrieve results*

7. `aws ssm get-parameter --name '/recovery/last-test-date' --query 'Parameter.[Value,LastModifiedDate]' --output json 2>/dev/null || echo '{"LastTest": "No automated testing configured"}'`
   *Check last recovery test execution date for regular testing compliance*

## Latest Results

PASS Basic recovery testing infrastructure available (29%): PASS Backup infrastructure validation: 208 recent backup operations prove recovery foundation
- PASS Point-in-time recovery testing capability: 1/1 databases ready for RPO validation

---
*Generated 2025-09-29 22:00 UTC*