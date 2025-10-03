# KSI-SVC-10: Perform regularly scheduled backups

## Overview

**Category:** Service Configuration
**Status:** PASS
**Last Check:** 2025-10-03 22:39

**What it validates:** Perform regularly scheduled backups

**Why it matters:** Validates comprehensive backup strategy from basic manual backups to enterprise-grade automated backup policies and disaster recovery

## Validation Method

1. `aws backup list-backup-plans --output json`
   *Check AWS Backup plans for automated backup scheduling*

2. `aws backup get-backup-plan --backup-plan-id $(aws backup list-backup-plans --query 'BackupPlansList[0].BackupPlanId' --output text) --output json || echo '{"BackupPlan": null}'`
   *Validate backup plan details and retention policies*

3. `aws s3api list-buckets --query 'Buckets[0].Name' --output text | xargs -I {} aws s3api list-inventory-configurations --bucket {} --output json || echo '{"InventoryConfigurationList": []}'`
   *Check S3 bucket backup and versioning configurations*

4. `aws lambda list-functions --output json`
   *Validate Lambda functions for backup automation*

5. `aws logs describe-log-groups --output json`
   *Check CloudWatch Logs for backup operation monitoring*

## Latest Results

PASS Good automated data lifecycle (75%): FAIL S3 Lifecycle Management
- PASS Backup Retention Management
- PASS Log Retention Policies
- PASS Automated Cleanup Functions

---
*Generated 2025-10-03 22:39 UTC*