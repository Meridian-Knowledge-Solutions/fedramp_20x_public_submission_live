# KSI-RPL-01: Define Recovery Time Objectives (RTO) and Recovery Point Objectives (RPO)

## Overview

**Category:** Recovery Planning
**Status:** PASS
**Last Check:** 2025-06-25 18:42

**What it validates:** Define Recovery Time Objectives (RTO) and Recovery Point Objectives (RPO)

**Why it matters:** Validates documented RTO/RPO definitions with technical infrastructure capability verification through RDS backup retention and point-in-time recovery settings

## Validation Method

1. `aws rds describe-db-instances --query 'DBInstances[*].[DBInstanceIdentifier,BackupRetentionPeriod,LatestRestorableTime,PreferredBackupWindow]' --output json`
   *Validate RDS backup retention (BackupRetentionPeriod > 0) and point-in-time recovery capability for RPO validation*

2. `aws backup list-backup-plans --output json`
   *Check backup plan frequency and retention alignment with documented RTO/RPO objectives*

3. **Manual Review:** Check evidence_v2/KSI-RPL-01/ for rto_rpo_definitions.pdf with actual infrastructure-validated objectives, business_impact_analysis.pdf, and recovery_objectives_matrix.xlsx

## Latest Results

WARNING Basic RTO/RPO definitions (expand technical validation): PASS Core RTO/RPO documentation: rto_rpo_definitions.pdf, combined_tabletop_test_report_template.pdf
- FAIL No RDS backup retention configured
- PASS Backup infrastructure supports RTO/RPO: 1 backup plans configured

---
*Generated 2025-06-25 18:42 UTC*