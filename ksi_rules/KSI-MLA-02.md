# KSI-MLA-02: Regularly review and audit logs

## Overview

**Category:** Monitoring, Logging, and Auditing
**Status:** PASS
**Last Check:** 2025-10-02 03:01

**What it validates:** Regularly review and audit logs

**Why it matters:** Validates comprehensive log review from basic notification-driven processes to enterprise-grade automated analysis and compliance governance

## Validation Method

1. `aws cloudwatch describe-alarms --output json`
   *Check CloudWatch alarms for automated log review*

2. `aws logs describe-metric-filters --output json`
   *Validate metric filters for log pattern analysis*

3. `aws sns list-topics --output json`
   *Check SNS topics for log review notifications*

4. `aws logs describe-log-groups --output json`
   *Analyze log retention policies and compliance*

5. `aws cloudtrail lookup-events --max-items 10 --output json`
   *Check recent audit events for review validation*

6. `aws securityhub get-insights --output json`
   *Validate advanced log correlation and security analytics*

7. `aws lambda list-functions --output json`
   *Check custom log processing and automated review functions*

8. `aws organizations describe-organization --output json`
   *Validate enterprise-wide centralized log review capabilities*

## Latest Results

PASS Enterprise-grade log review with comprehensive analysis and governance (83%): PASS Log review notifications: 9 SNS topics for alert delivery
- PASS Manual review capability: 25 log groups available for analysis
- PASS Automated log monitoring: 7 CloudWatch alarms for log review
- PASS Security-focused review: 2 alarms for security event detection
- PASS Advanced log correlation: 1 Security Hub insights for intelligent analysis
- PASS Audit event analysis: 10 recent CloudTrail events available for review
- PASS Custom log processing: 1 Lambda functions for advanced log analysis
- PASS Compliance retention: 25/25 log groups with retention policies
- PASS Long-term audit capability: 24 log groups with compliance-grade retention (365+ days)
- PASS Enterprise log aggregation: AWS Organizations enables centralized multi-account log review

---
*Generated 2025-10-02 03:01 UTC*