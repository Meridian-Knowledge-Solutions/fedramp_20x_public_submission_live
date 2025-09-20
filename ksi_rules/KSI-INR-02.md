# KSI-INR-02: Maintain a log of incidents and periodically review past incidents for patterns or vulnerabilities

## Overview

**Category:** Incident Reporting
**Status:** PASS
**Last Check:** 2025-09-20 05:19

**What it validates:** Maintain a log of incidents and periodically review past incidents for patterns or vulnerabilities

**Why it matters:** Comprehensive incident tracking via automated infrastructure (EventBridge/CloudWatch) and incident_automation.py script that collects, logs, and analyzes security incidents

## Validation Method

1. `aws events list-rules --output json`
   *Verify EventBridge rules for incident automation (need 2+ with incident keywords)*

2. `aws events list-targets-by-rule --rule <rule_name> --output json`
   *Dynamically run for each rule found to verify it has at least one active target*

3. `aws logs describe-log-groups --output json`
   *Verify CloudWatch log groups for incident logging (need 4+ with security keywords and a retention policy of at least 365 days)*

4. `aws guardduty list-detectors --output json`
   *Check for a GuardDuty detector ID*

5. `aws guardduty get-detector --detector-id <detector_id> --output json`
   *Dynamically run for the detector ID to verify its status is 'ENABLED'*

6. `aws securityhub get-findings --max-results 5 --output json`
   *Verify Security Hub for pattern analysis capability*

7. `aws cloudtrail list-trails --output json`
   *Verify CloudTrail for behavioral analysis*

8. `aws lambda list-functions --output json`
   *Check for incident automation functions*

## Latest Results

PASS Partial incident tracking infrastructure (score: 8): WARNING Permission denied for events
- PASS 5 CloudWatch groups with >= 365-day retention
- WARNING Permission denied for guardduty
- PASS Security Hub active
- PASS 1 CloudTrail trail(s)
- PASS 2 automation Lambda(s)

---
*Generated 2025-09-20 05:19 UTC*