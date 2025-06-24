# KSI-MLA-01: Operate a SIEM or similar system for centralized, tamper-resistant logging

## Overview

**Category:** Monitoring, Logging, and Auditing
**Status:** PASS
**Last Check:** 2025-06-24 18:59

**What it validates:** Operate a SIEM or similar system for centralized, tamper-resistant logging

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

PASS Mature SIEM with solid log management and alerting (64%): PASS CloudTrail foundation: 1 trails (0 active, 1 tamper-resistant)
- PASS Centralized log collection: 8 log groups (6 AWS services, 2 applications)
- WARNING Partial retention management: 6/8 log groups with retention policies
- PASS Compliance-grade retention: 3 log groups with long-term retention (365+ days)
- PASS Cryptographic infrastructure: 11 KMS keys available for log protection
- PASS Advanced threat detection: 20 Security Hub findings (4 active)
- PASS Enterprise-wide logging: AWS Organizations enables centralized multi-account SIEM
- PASS Multi-region audit coverage: 1 trails across all regions
- PASS Global service monitoring: 1 trails capturing global AWS events

---
*Generated 2025-06-24 18:59 UTC*