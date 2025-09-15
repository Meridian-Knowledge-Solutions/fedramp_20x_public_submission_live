# KSI-RPL-04: Regularly test the capability to recover from incidents and contingencies

## Overview

**Category:** Recovery Planning
**Status:** PASS
**Last Check:** 2025-09-15 01:58

**What it validates:** Regularly test the capability to recover from incidents and contingencies

**Why it matters:** Validates recovery testing through historical restore operations, backup job performance metrics, and documented test procedures with actual results

## Validation Method

1. `aws backup list-restore-jobs --max-results 20 --output json`
   *Document historical restore operations proving actual recovery testing has been performed*

2. `aws backup list-backup-jobs --by-state COMPLETED --by-created-after 2024-05-01 --output json`
   *Show recent backup completions with timing data to validate recovery time objectives*

3. `aws rds describe-db-instances --query 'DBInstances[*].[DBInstanceIdentifier,LatestRestorableTime,PreferredBackupWindow]' --output json`
   *Verify point-in-time recovery capability and backup timing for recovery testing validation*

4. **Manual Review:** Check evidence_v2/KSI-RPL-04/ for recovery_testing_procedures.pdf, disaster_recovery_test_results.xlsx with actual restore times, tabletop_exercise_reports.pdf, and recovery_lessons_learned.pdf

## Latest Results

PASS Regular recovery testing capability validated with operational proof: PASS Core testing documentation: combined_tabletop_test_report_template.pdf
- PASS Recent testing: 2 test documents updated within last year
- PASS Recovery capability demonstrated through working backup infrastructure and documented procedures
- PASS Backup infrastructure validation: 194 recent backup operations prove recovery foundation
- PASS Point-in-time recovery testing capability: 1/1 databases ready for RPO validation

---
*Generated 2025-09-15 01:58 UTC*