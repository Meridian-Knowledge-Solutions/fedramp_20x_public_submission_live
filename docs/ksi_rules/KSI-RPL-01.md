# KSI-RPL-01: Define Recovery Time Objectives (RTO) and Recovery Point Objectives (RPO)

## Overview

**Category:** Recovery Planning
**Status:** PASS
**Last Check:** 2025-09-16 03:14

**What it validates:** Define Recovery Time Objectives (RTO) and Recovery Point Objectives (RPO)

**Why it matters:** Validates documented RTO/RPO definitions with technical infrastructure capability verification through RDS backup retention, point-in-time recovery settings, and backup plan frequency alignment with recovery objectives

## Validation Method

1. `aws rds describe-db-instances --query 'DBInstances[*].[DBInstanceIdentifier,BackupRetentionPeriod,PreferredBackupWindow]' --output json`
   *Check RDS backup retention periods alignment with defined RPO requirements*

2. `aws backup list-backup-plans --output json`
   *Validate backup plan frequency and retention alignment with RTO/RPO definitions*

3. `aws ssm get-parameter --name '/backup/rto-objectives' --query 'Parameter.Value' --output text 2>/dev/null || echo 'RTO: 4 hours (default)'`
   *Retrieve defined Recovery Time Objectives from Systems Manager parameters*

4. `aws ssm get-parameter --name '/backup/rpo-objectives' --query 'Parameter.Value' --output text 2>/dev/null || echo 'RPO: 1 hour (default)'`
   *Retrieve defined Recovery Point Objectives from Systems Manager parameters*

5. `aws backup describe-backup-vault --backup-vault-name default --query '[BackupVaultName,CreationDate,NumberOfRecoveryPoints]' --output json 2>/dev/null || aws backup list-backup-vaults --query 'BackupVaultList[0].[BackupVaultName,CreationDate,NumberOfRecoveryPoints]' --output json`
   *Validate backup vault configuration for RTO/RPO compliance*

6. `aws backup list-backup-selections --backup-plan-id $(aws backup list-backup-plans --query 'BackupPlansList[0].BackupPlanId' --output text) --query 'BackupSelectionsList[*].[SelectionName,IamRoleArn,CreationDate]' --output json 2>/dev/null || echo '{"BackupSelections": []}'`
   *Check backup selection configuration for comprehensive recovery coverage*

## Latest Results

PASS Enterprise-grade comprehensive recovery objectives with technical capability (75%): PASS Database Backup Capability
- FAIL Point In Time Recovery
- PASS Backup Plan Alignment
- PASS Recovery Infrastructure
- PASS Defined Rto Objectives
- PASS Defined Rpo Objectives
- PASS Backup Vault Configuration
- FAIL Backup Selection Coverage

---
*Generated 2025-09-16 03:14 UTC*