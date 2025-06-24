# KSI-RPL-01: Define Recovery Time Objectives (RTO) and Recovery Point Objectives (RPO)

## Overview

**Category:** Recovery Planning
**Status:** FAIL
**Last Check:** 2025-06-24 02:05

**What it validates:** Define Recovery Time Objectives (RTO) and Recovery Point Objectives (RPO)

**Why it matters:** Validates documented RTO/RPO definitions with technical infrastructure capability verification through RDS backup retention and point-in-time recovery settings

## Validation Method

1. `aws rds describe-db-instances --query 'DBInstances[*].[DBInstanceIdentifier,BackupRetentionPeriod,LatestRestorableTime,PreferredBackupWindow]' --output json`
   *Validate RDS backup retention (BackupRetentionPeriod > 0) and point-in-time recovery capability for RPO validation*

2. `aws backup list-backup-plans --output json`
   *Check backup plan frequency and retention alignment with documented RTO/RPO objectives*

3. **Manual Review:** Check evidence_v2/KSI-RPL-01/ for rto_rpo_definitions.pdf with actual infrastructure-validated objectives, business_impact_analysis.pdf, and recovery_objectives_matrix.xlsx

## Latest Results

- Exception during evaluation: 'list' object has no attribute 'get'

---
*Generated 2025-06-24 02:05 UTC*