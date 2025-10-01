# KSI-IAM-06: Implement fine-grained automated actions on security events related to authentication and access control

## Overview

**Category:** Identity and Access Management
**Status:** PASS
**Last Check:** 2025-10-01 22:14

**What it validates:** Implement fine-grained automated actions on security events related to authentication and access control

**Why it matters:** Validates comprehensive automated security response from basic CloudWatch alarms to enterprise-grade SOAR and intelligent threat response

## Validation Method

1. `aws events list-rules --output json`
   *Check EventBridge rules for automated security event responses*

2. `aws guardduty list-detectors --output json`
   *Validate GuardDuty for automated threat detection*

3. `aws securityhub describe-hub --output json`
   *Check Security Hub for centralized security event management*

4. `aws configservice describe-config-rules --output json`
   *Validate Config rules for automated compliance enforcement*

5. `aws lambda list-functions --output json`
   *Check Lambda functions for automated security response actions*

6. `aws sns list-topics --output json`
   *Validate SNS topics for security event notifications*

7. `aws configservice describe-remediation-configurations --config-rule-names $(aws configservice describe-config-rules --query 'ConfigRules[0].ConfigRuleName' --output text 2>/dev/null || echo 'none') --output json || echo '{"RemediationConfigurations": []}'`
   *Check automated remediation for security violations*

8. `aws lambda list-functions --output json`
   *Validate custom security automation functions*

9. `aws cloudwatch describe-alarms --output json`
   *Check CloudWatch alarms for authentication and access monitoring*

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
*Generated 2025-10-01 22:14 UTC*