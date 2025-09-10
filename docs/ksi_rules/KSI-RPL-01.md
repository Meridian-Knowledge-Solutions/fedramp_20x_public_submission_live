# KSI-RPL-01: Define Recovery Time Objectives (RTO) and Recovery Point Objectives (RPO)

## Overview

**Category:** Recovery Planning
**Status:** PASS
**Last Check:** 2025-09-10 02:36

**What it validates:** Define Recovery Time Objectives (RTO) and Recovery Point Objectives (RPO)

**Why it matters:** Validates documented RTO/RPO definitions with technical infrastructure capability verification through RDS backup retention, point-in-time recovery settings, and backup plan frequency alignment with recovery objectives

## Validation Method

1. `aws rds describe-db-instances --query 'DBInstances[*].[DBInstanceIdentifier,BackupRetentionPeriod,PreferredBackupWindow]' --output json`
   *Check RDS backup retention periods alignment with defined RPO requirements*

2. `aws backup list-backup-plans --output json`
   *Validate backup plan frequency and retention alignment with RTO/RPO definitions*

3. **Manual Review:** Check evidence_v2/KSI-RPL-01/ for rto_rpo_definitions.pdf, business_impact_analysis.xlsx, recovery_objectives_policy.pdf, and stakeholder_approved_recovery_targets.pdf

## Latest Results

PASS RTO/RPO objectives defined with technical validation: PASS Core RTO/RPO documentation: rto_rpo_definitions.pdf
- PASS RDS backup retention validated: 1/1 databases with BackupRetentionPeriod > 0
- PASS Point-in-time recovery capability: 1/1 databases support RPO objectives
- PASS Backup infrastructure supports RTO/RPO: 2 backup plans configured

---
*Generated 2025-09-10 02:36 UTC*