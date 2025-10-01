# KSI-MLA-03: Rapidly detect and remediate or mitigate vulnerabilities

## Overview

**Category:** Monitoring, Logging, and Auditing
**Status:** PASS
**Last Check:** 2025-10-01 08:13

**What it validates:** Rapidly detect and remediate or mitigate vulnerabilities

**Why it matters:** Validates comprehensive vulnerability detection from basic security monitoring to enterprise-grade automated remediation and threat intelligence

## Validation Method

1. `aws securityhub get-enabled-standards --region us-east-1 --output json`
   *Check Security Hub enabled standards for vulnerability detection*

2. `aws inspector2 get-configuration --output json`
   *Validate Inspector for continuous vulnerability scanning*

3. `aws securityhub get-findings --filters '{"RecordState":[{"Value":"ACTIVE","Comparison":"EQUALS"}],"WorkflowStatus":[{"Value":"NEW","Comparison":"EQUALS"}]}' --max-results 50 --output json`
   *Check active Security Hub findings for rapid detection*

4. `aws ssm describe-patch-baselines --output json`
   *Validate patch baselines for automated vulnerability remediation*

5. `aws lambda list-functions --output json`
   *Check Lambda functions for automated remediation workflows*

6. `aws cloudwatch describe-alarms --output json`
   *Validate CloudWatch alarms for vulnerability detection alerts*

7. `aws organizations describe-organization --output json`
   *Check organization-wide vulnerability management policies*

## Latest Results

PASS Strong vulnerability management with automated remediation (78%): FAIL Security Hub not configured for vulnerability detection
- PASS Automated vulnerability scanning: Inspector EC2, ECR scanning enabled
- PASS Multi-service vulnerability coverage: Both EC2 and ECR scanning for comprehensive assessment
- PASS Automated patch management: 17 patch baselines (15 default, 2 custom)
- PASS Tailored remediation: 2 custom patch baselines for targeted vulnerability response
- PASS Security automation: 2 Lambda functions for security operations
- PASS Real-time threat detection: 1 CloudWatch alarms for rapid vulnerability alerting
- PASS Active threat analysis: 50 active security findings (0 critical, 28 high)
- PASS Enterprise vulnerability management: AWS Organizations enables centralized multi-account detection

---
*Generated 2025-10-01 08:13 UTC*