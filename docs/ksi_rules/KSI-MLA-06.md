# KSI-MLA-06: Centrally track and prioritize the mitigation and/or remediation of identified vulnerabilities

## Overview

**Category:** Monitoring, Logging, and Auditing
**Status:** PASS
**Last Check:** 2025-09-16 07:31

**What it validates:** Centrally track and prioritize the mitigation and/or remediation of identified vulnerabilities

**Why it matters:** Validates comprehensive centralized vulnerability tracking from basic findings collection to enterprise-grade vulnerability lifecycle management, covering automated prioritization, remediation workflows, compliance tracking, and cross-account vulnerability coordination with metrics and reporting

## Validation Method

1. `aws securityhub get-findings --max-results 100 --output json`
   *Check Security Hub for centralized vulnerability tracking and finding aggregation from multiple sources*

2. `aws inspector2 list-findings --max-results 50 --output json`
   *Validate Inspector findings for vulnerability prioritization and severity-based tracking*

3. `aws ssm describe-patch-group-compliance --output json`
   *Check patch compliance tracking for systematic vulnerability remediation and patch management*

4. `aws config get-compliance-summary-by-config-rule --output json`
   *Validate Config rule compliance for configuration vulnerability tracking and governance*

5. `aws securityhub get-insights --output json`
   *Check Security Hub insights for advanced vulnerability analytics and trend analysis*

6. `aws cloudwatch describe-alarms --output json`
   *Validate vulnerability alerting and automated response triggers for priority vulnerabilities*

7. `aws lambda list-functions --output json`
   *Check automated vulnerability management functions for remediation workflow automation*

8. `aws events list-rules --output json`
   *Validate EventBridge rules for vulnerability lifecycle automation and workflow integration*

9. `aws sns list-topics --output json`
   *Check SNS topics for vulnerability notification workflows and stakeholder communication*

10. `aws organizations describe-organization --output json`
   *Validate enterprise-wide vulnerability tracking and cross-account centralized management*

## Latest Results

- PASS KSI retired in Phase Two - superseded by KSI-MLA-03 (FedRAMP Vulnerability Response and Detection standard)

---
*Generated 2025-09-16 07:31 UTC*