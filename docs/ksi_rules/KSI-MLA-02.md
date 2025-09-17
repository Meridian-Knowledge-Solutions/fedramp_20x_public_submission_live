# KSI-MLA-02: Regularly review and audit logs

## Overview

**Category:** Monitoring, Logging, and Auditing
**Status:** PASS
**Last Check:** 2025-09-17 10:50

**What it validates:** Regularly review and audit logs

**Why it matters:** Validates comprehensive log review capabilities from basic notification-driven processes to enterprise-grade automated analysis, compliance governance, and cross-account log review

## Validation Method

1. `aws cloudwatch describe-alarms --output json`
   *Check CloudWatch alarms for automated log review and real-time monitoring*

2. `aws logs describe-metric-filters --output json`
   *Validate metric filters for log pattern analysis and security event detection*

3. `aws sns list-topics --output json`
   *Check SNS topics for log review notifications and alert delivery mechanisms*

4. `aws logs describe-log-groups --output json`
   *Analyze log retention policies, encryption, and compliance-grade log management*

5. `aws cloudtrail lookup-events --max-items 10 --output json`
   *Check recent audit events for manual and automated review process validation*

6. `aws securityhub get-insights --output json`
   *Validate advanced log correlation, security analytics, and threat intelligence*

7. `aws config describe-config-rules --output json`
   *Check automated compliance rules for log governance and audit trail validation*

8. `aws lambda list-functions --output json`
   *Validate custom log processing, automated review functions, and intelligent analysis*

9. `aws organizations describe-organization --output json`
   *Check enterprise-wide centralized log review and cross-account analysis capabilities*

## Latest Results

PASS Production-ready log review with good automation (50%): PASS Log review notifications: 2 SNS topics for alert delivery
- PASS Manual review capability: 14 log groups available for analysis
- PASS Advanced log correlation: 1 Security Hub insights for intelligent analysis
- PASS Audit event analysis: 10 recent CloudTrail events available for review
- WARNING Partial retention management: 9/14 log groups with retention policies
- PASS Long-term audit capability: 4 log groups with compliance-grade retention (365+ days)
- PASS Enterprise log aggregation: AWS Organizations enables centralized multi-account log review

---
*Generated 2025-09-17 10:50 UTC*