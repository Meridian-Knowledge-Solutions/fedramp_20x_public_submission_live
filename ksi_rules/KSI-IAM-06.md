# KSI-IAM-06: Automatically disable or otherwise secure accounts with privileged access in response to suspicious activity

## Overview

**Category:** Identity and Access Management
**Status:** PASS
**Last Check:** 2025-09-28 03:01

**What it validates:** Automatically disable or otherwise secure accounts with privileged access in response to suspicious activity

**Why it matters:** Validates end-to-end automated response workflows including threat detection, event triggers, and account security actions through modern AWS security services and Identity Center integration

## Validation Method

1. `aws events list-rules --output json`
   *Check EventBridge rules for automated security response triggers (critical for automation)*

2. `aws guardduty list-detectors --output json`
   *Validate GuardDuty threat detection service for suspicious activity identification*

3. `aws securityhub describe-hub --output json`
   *Check Security Hub for centralized security findings and automated response coordination*

4. `aws configservice describe-config-rules --output json`
   *Check Config rules for automated compliance monitoring and remediation triggers*

5. `aws lambda list-functions --output json`
   *Validate Lambda functions for automated security response and account management workflows*

6. `aws sns list-topics --output json`
   *Check SNS topics for security incident notification and alert distribution*

7. `aws config describe-remediation-configurations --config-rule-names $(aws configservice describe-config-rules --query 'ConfigRules[0:5].ConfigRuleName' --output text 2>/dev/null || echo 'none') --output json 2>/dev/null || echo '{"RemediationConfigurations": []}'`
   *Check Config remediation for automated account security and compliance enforcement*

8. `aws lambda list-functions --output json`
   *Identify automated response functions for account disabling and security actions*

9. `aws cloudwatch describe-alarms --output json`
   *Check CloudWatch alarms for suspicious privileged account activity monitoring*

## Latest Results

PASS Strong automated response capabilities (81%): PASS Advanced threat detection: GuardDuty enabled (1 detector(s))
- PASS Centralized security management: Security Hub enabled
- PASS Automated security triggers: 11 active EventBridge rules
- WARNING No Identity Center found (missing modern automated identity controls)
- PASS Enterprise governance: Config rules managed centrally (multi-account architecture)
- PASS Automated response functions: 12 security automation functions
- PASS Automated monitoring: 13 security-focused alarms
- PASS Centralized governance model detected (multi-account architecture)

---
*Generated 2025-09-28 03:01 UTC*