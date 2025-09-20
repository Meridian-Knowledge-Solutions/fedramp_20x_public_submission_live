# KSI-IAM-06: Automatically disable or otherwise secure accounts with privileged access in response to suspicious activity

## Overview

**Category:** Identity and Access Management
**Status:** PASS
**Last Check:** 2025-09-20 01:37

**What it validates:** Automatically disable or otherwise secure accounts with privileged access in response to suspicious activity

**Why it matters:** Validates end-to-end automated response workflows including threat detection, event triggers, and account security actions through modern AWS security services and Identity Center integration

## Validation Method

1. `aws events list-rules --output json`
   *Check EventBridge rules for automated security response triggers (critical for automation)*

2. `aws guardduty list-detectors --output json`
   *Validate GuardDuty threat detection service for suspicious activity identification*

3. `aws securityhub describe-hub --output json`
   *Check Security Hub for centralized security findings and automated response coordination*

4. `aws sso-admin list-instances --output json`
   *Validate Identity Center for built-in automated session and access controls*

5. `aws configservice describe-config-rules --output json`
   *Check Config rules for automated compliance monitoring and remediation triggers*

6. `aws lambda list-functions --output json`
   *Validate Lambda functions for automated security response and account management workflows*

7. `aws sns list-topics --output json`
   *Check SNS topics for security incident notification and alert distribution*

8. `aws config describe-remediation-configurations --config-rule-names $(aws configservice describe-config-rules --query 'ConfigRules[0:5].ConfigRuleName' --output text 2>/dev/null || echo 'none') --output json 2>/dev/null || echo '{"RemediationConfigurations": []}'`
   *Check Config remediation for automated account security and compliance enforcement*

9. `aws lambda list-functions --output json`
   *Identify automated response functions for account disabling and security actions*

10. `aws cloudwatch describe-alarms --output json`
   *Check CloudWatch alarms for suspicious privileged account activity monitoring*

## Latest Results

PASS Enterprise-grade automated response capabilities (91%): PASS Advanced threat detection: GuardDuty enabled (1 detector(s))
- PASS Centralized security management: Security Hub enabled
- PASS Automated security triggers: 10 active EventBridge rules
- PASS Modern identity automation: Identity Center configured (1 instance(s))
- PASS Built-in automated identity controls: Session management, conditional access, risk-based authentication
- PASS Enterprise governance: Config rules managed centrally (multi-account architecture)
- PASS Automated response functions: 5 security automation functions
- PASS Enterprise governance: CloudWatch alarms managed centrally (multi-account architecture)
- INFO Multi-account architecture detected (governance centralized)

---
*Generated 2025-09-20 01:37 UTC*