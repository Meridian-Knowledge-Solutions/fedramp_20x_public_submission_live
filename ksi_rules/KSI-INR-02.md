# KSI-INR-02: Establish an insider threat program

## Overview

**Category:** Incident Reporting
**Status:** PASS
**Last Check:** 2025-10-04 02:56

**What it validates:** Establish an insider threat program

**Why it matters:** Validates insider threat detection from basic access monitoring to enterprise-grade behavioral analytics and automated threat detection

## Validation Method

1. `aws events list-rules --output json`
   *Check EventBridge rules for insider threat detection automation*

2. `aws logs describe-log-groups --output json`
   *Validate CloudWatch Logs for insider threat monitoring*

3. `aws guardduty list-detectors --output json`
   *Check GuardDuty for insider threat detection capabilities*

4. `aws securityhub get-findings --max-results 5 --output json`
   *Validate Security Hub findings for insider threat alerts*

5. **Manual Review:** Manual review of insider threat program documentation, detection rules, and response procedures

## Latest Results

PASS Comprehensive validation passed: Infrastructure is configured and operational artifacts are present. PASS Incident response infrastructure is well-configured (Score: 4/4).
- PASS Operational log found with 1 incidents.
- PASS Periodic review report found and appears valid.

---
*Generated 2025-10-04 02:56 UTC*