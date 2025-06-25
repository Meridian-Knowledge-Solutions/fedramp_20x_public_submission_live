# KSI-RPL-02: Develop and maintain a recovery plan that aligns with defined recovery objectives

## Overview

**Category:** Recovery Planning
**Status:** PASS
**Last Check:** 2025-06-25 22:12

**What it validates:** Develop and maintain a recovery plan that aligns with defined recovery objectives

**Why it matters:** Validates recovery plans with technical implementation evidence through backup configurations and recovery automation capabilities

## Validation Method

1. `aws rds describe-db-instances --query 'DBInstances[*].[DBInstanceIdentifier,DeletionProtection,BackupRetentionPeriod,PreferredMaintenanceWindow]' --output json`
   *Verify RDS recovery configuration aligns with documented recovery procedures*

2. `aws backup describe-backup-plans --output json`
   *Validate backup plan configuration supports documented recovery procedures*

3. **Manual Review:** Check evidence_v2/KSI-RPL-02/ for disaster_recovery_plan.pdf (updated with technical validation), incident_response_plan.pdf, recovery_procedures_playbook.pdf, and business_continuity_plan.pdf

## Latest Results

WARNING Good recovery planning (enhance technical alignment): PASS Core recovery plans: incident_reponse_policy.pdf, contingency_planning_policy.pdf
- PASS Plan maintenance: 3 files updated within last year

---
*Generated 2025-06-25 22:12 UTC*