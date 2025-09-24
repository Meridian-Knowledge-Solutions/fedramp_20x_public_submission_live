# KSI-SVC-10: Remove unwanted information promptly, including from backups if appropriate

## Overview

**Category:** Service Configuration
**Status:** FAIL
**Last Check:** 2025-09-24 03:26

**What it validates:** Remove unwanted information promptly, including from backups if appropriate

**Why it matters:** Validates automated data lifecycle management through comprehensive retention policies...

## Validation Method

1. `aws backup list-backup-plans --output json`
   *Verify backup plans are configured.*

2. `aws backup get-backup-plan --backup-plan-id $(aws backup list-backup-plans --query 'BackupPlansList[0].BackupPlanId' --output text 2>/dev/null || echo 'none') --output json 2>/dev/null || echo '{"BackupPlan":{}}'`
   *ADDED: Retrieve details of the primary backup plan to validate retention rules.*

3. `aws s3api list-inventory-configurations --bucket $(aws s3api list-buckets --query 'Buckets[0].Name' --output text 2>/dev/null || echo 'none') --output json 2>/dev/null || echo '{"InventoryConfigurationList":[]}'`
   *ADDED: Check for S3 Inventory configs as a proxy for lifecycle management.*

4. `aws lambda list-functions --output json`
   *Check automated data purging and lifecycle management functions.*

5. `aws logs describe-log-groups --output json`
   *Check log retention policies for compliance-driven data deletion.*

## Latest Results

FAIL Insufficient automated data lifecycle management (50%): FAIL S3 Lifecycle Management
- PASS Backup Retention Management
- FAIL Log Retention Policies
- PASS Automated Cleanup Functions

---
*Generated 2025-09-24 03:26 UTC*