# KSI-IAM-06: Automatically disable or otherwise secure accounts with privileged access in response to suspicious activity

## Overview

**Category:** Identity and Access Management
**Status:** PASS
**Last Check:** 2025-06-24 02:28

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

5. `aws config describe-config-rules --output json`
   *Check Config rules for automated compliance remediation and account security*

6. `aws lambda list-functions --output json`
   *Identify automated response functions for account disabling and security actions*

7. `aws cloudwatch describe-alarms --output json`
   *Check CloudWatch alarms for suspicious privileged account activity monitoring*

## Latest Results

PASS Strong automated response capabilities (82%): PASS Advanced threat detection: GuardDuty enabled (1 detector(s))
- PASS Centralized security management: Security Hub enabled
- PASS Automated security triggers: 1 active EventBridge rules
- PASS Modern identity automation: Identity Center configured (1 instance(s))
- PASS Built-in automated identity controls: Session management, conditional access, risk-based authentication
- WARNING No Config rules found for automated remediation
- WARNING 2 Lambda functions found but none explicitly security-focused
- FAIL No CloudWatch alarms found for security monitoring

---
*Generated 2025-06-24 02:28 UTC*