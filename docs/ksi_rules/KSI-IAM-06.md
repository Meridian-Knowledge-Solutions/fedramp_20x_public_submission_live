# KSI-IAM-06: Automatically disable or otherwise secure accounts with privileged access in response to suspicious activity

## Overview

**Category:** Identity and Access Management
**Status:** PASS
**Last Check:** 2025-06-30 03:26

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
   *Check Config rules in management account for automated compliance remediation*

6. `aws lambda list-functions --output json`
   *Identify automated response functions for account disabling and security actions*

7. `aws cloudwatch describe-alarms --output json`
   *Check CloudWatch alarms for suspicious privileged account activity monitoring*

## Latest Results

PASS Enterprise-grade automated response capabilities (119%): PASS Advanced threat detection: GuardDuty enabled (1 detector(s))
- PASS Centralized security management: Security Hub enabled
- PASS Automated security triggers: 7 active EventBridge rules
- PASS Modern identity automation: Identity Center configured (1 instance(s))
- PASS Built-in automated identity controls: Session management, conditional access, risk-based authentication
- PASS Enterprise automated compliance: 369 Config rules for security across accounts
- PASS Automated response functions: 2 security automation functions
- PASS Enterprise automated monitoring: 1 security alarms across accounts
- PASS Enterprise multi-account security governance: Cross-account automation capabilities

---
*Generated 2025-06-30 03:26 UTC*