# KSI-RPL-01: Define Recovery Time Objectives (RTO) and Recovery Point Objectives (RPO)

## Overview

**Category:** Recovery Planning
**Status:** PASS
**Last Check:** 2025-06-26 03:40

**What it validates:** Define Recovery Time Objectives (RTO) and Recovery Point Objectives (RPO)

**Why it matters:** Validates documented RTO/RPO definitions with technical infrastructure capability verification through RDS backup retention, point-in-time recovery settings, and backup plan frequency alignment with recovery objectives

## Validation Method

1. `aws rds describe-db-instances --query 'DBInstances[*].[DBInstanceIdentifier,BackupRetentionPeriod,PreferredBackupWindow]' --output json`
   *Validate RDS backup retention (BackupRetentionPeriod > 0) and point-in-time recovery capability for RPO validation - critical for database recovery objectives*

2. `aws backup list-backup-plans --output json`
   *Check backup plan frequency and retention alignment with documented RTO/RPO objectives for infrastructure recovery planning*

3. **Manual Review:** Check evidence_v2/KSI-RPL-01/ for rto_rpo_definitions.pdf with actual infrastructure-validated objectives, business_impact_analysis.pdf, and recovery_objectives_matrix.xlsx

## Latest Results

PASS RTO/RPO objectives defined with technical validation: PASS Core RTO/RPO documentation: rto_rpo_definitions.pdf
- PASS RDS backup retention validated: 1/1 databases with BackupRetentionPeriod > 0
- PASS Point-in-time recovery capability: 1/1 databases support RPO objectives
- PASS Backup infrastructure supports RTO/RPO: 1 backup plans configured

---
*Generated 2025-06-26 03:40 UTC*