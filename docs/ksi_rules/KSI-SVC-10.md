# KSI-SVC-10: Remove unwanted information promptly, including from backups if appropriate

## Overview

**Category:** Service Configuration
**Status:** PASS
**Last Check:** 2025-09-16 04:08

**What it validates:** Remove unwanted information promptly, including from backups if appropriate

**Why it matters:** Validates automated data lifecycle management through comprehensive retention policies, backup purging automation, storage lifecycle management, and compliance-driven deletion covering AWS Backup lifecycle, S3 policies, automated purging, and data retention compliance

## Validation Method

1. `aws backup list-backup-plans --output json`
   *Validate backup lifecycle management and automated retention policies*

2. `aws s3api list-buckets --output json`
   *Check S3 storage lifecycle automation and data retention management*

3. `aws lambda list-functions --output json`
   *Check automated data purging and lifecycle management functions*

4. `aws events list-rules --output json`
   *Validate scheduled data lifecycle and automated cleanup workflows*

5. `aws logs describe-log-groups --output json`
   *Check log retention policies for compliance-driven data deletion*

6. `aws ec2 describe-snapshots --owner-ids self --output json`
   *Validate EBS snapshot lifecycle management and automated cleanup*

7. **Manual Review:** Data lifecycle management policies, retention schedules, and purging procedures documentation

## Latest Results

PASS Advanced automated data lifecycle management (100%): PASS S3 Lifecycle Policies
- PASS Backup Retention Management
- PASS Log Retention Policies
- PASS Automated Cleanup Functions

---
*Generated 2025-09-16 04:08 UTC*