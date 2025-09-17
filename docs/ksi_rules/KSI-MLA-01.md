# KSI-MLA-01: Operate a Security Information and Event Management (SIEM) or similar system(s) for centralized, tamper-resistant logging of events, activities, and changes

## Overview

**Category:** Monitoring, Logging, and Auditing
**Status:** PASS
**Last Check:** 2025-09-17 05:04

**What it validates:** Operate a Security Information and Event Management (SIEM) or similar system(s) for centralized, tamper-resistant logging of events, activities, and changes

**Why it matters:** Validates comprehensive SIEM capabilities from basic centralized logging to enterprise-grade log management, analysis, and compliance

## Validation Method

1. `aws cloudtrail describe-trails --output json`
   *Check CloudTrail for centralized, tamper-resistant logging foundation*

2. `aws logs describe-log-groups --output json`
   *Validate centralized log collection and retention policies in CloudWatch*

3. `aws cloudwatch describe-alarms --output json`
   *Check automated log analysis and real-time alerting capabilities*

4. `aws kms list-keys --output json`
   *Validate cryptographic protection and encryption for sensitive logs*

5. `aws config describe-delivery-channels --output json`
   *Check compliance-grade log delivery and audit trail mechanisms*

6. `aws s3api list-buckets --output json`
   *Validate log archival, long-term storage, and forensic capabilities*

7. `aws securityhub get-findings --max-results 20 --output json`
   *Check advanced threat detection and security event correlation*

8. `aws organizations describe-organization --output json`
   *Validate enterprise-wide centralized logging and cross-account capabilities*

## Latest Results

PASS Production-ready SIEM with advanced monitoring capabilities (75%): PASS CloudTrail foundation: 1 trails (0 active, 1 tamper-resistant)
- PASS Real-time log analysis: CloudTrail integrated with CloudWatch Logs
- PASS Centralized log collection: 14 log groups (11 AWS services, 3 applications)
- WARNING Partial retention management: 9/14 log groups with retention policies
- PASS Compliance-grade retention: 4 log groups with long-term retention (365+ days)
- PASS Cryptographic infrastructure: 14 KMS keys available for log protection
- INFO No CloudWatch alarms found for automated log analysis
- PASS Advanced threat detection: 20 Security Hub findings (20 active)
- INFO No Config delivery channels found for compliance log delivery
- PASS Log archival capability: 1 S3 buckets for long-term log storage
- PASS Enterprise-wide logging: AWS Organizations enables centralized multi-account SIEM
- PASS Multi-region audit coverage: 1 trails across all regions
- PASS Global service monitoring: 1 trails capturing global AWS events
- PASS Enterprise-wide CloudTrail: Organization-wide audit coverage

---
*Generated 2025-09-17 05:04 UTC*