# KSI-INR-02: Maintain a log of incidents and periodically review past incidents for patterns or vulnerabilities

## Overview

**Category:** Incident Reporting
**Status:** FAIL
**Last Check:** 2025-09-20 01:37

**What it validates:** Maintain a log of incidents and periodically review past incidents for patterns or vulnerabilities

**Why it matters:** Comprehensive incident tracking via automated infrastructure (EventBridge/CloudWatch) and incident_automation.py script that collects, logs, and analyzes security incidents from GuardDuty, Security Hub, and CloudTrail for pattern identification

## Validation Method

1. `aws events list-rules --output json`
   *Verify EventBridge rules for incident automation (need 2+ with incident keywords)*

2. `aws logs describe-log-groups --output json`
   *Verify CloudWatch log groups for incident logging (need 4+ with security keywords)*

3. `aws guardduty list-detectors --output json`
   *Verify GuardDuty is active as primary threat detection source*

4. `aws guardduty list-findings --detector-id $(aws guardduty list-detectors --query 'DetectorIds[0]' --output text 2>/dev/null || echo 'none') --max-results 5 --output json 2>/dev/null || echo '{"FindingIds":[]}'`
   *Validate GuardDuty is providing incident data for script analysis*

5. `aws securityhub get-findings --max-results 5 --output json 2>/dev/null || echo '{"Findings":[]}'`
   *Verify Security Hub for pattern analysis capability*

6. `aws cloudtrail lookup-events --max-items 5 --output json 2>/dev/null || echo '{"Events":[]}'`
   *Verify CloudTrail behavioral data availability*

7. `aws lambda list-functions --query "Functions[?contains(FunctionName, 'incident') || contains(FunctionName, 'inr') || contains(FunctionName, 'security')]" --output json 2>/dev/null || echo '{"Functions":[]}'`
   *Check if incident_automation.py is deployed as Lambda function*

8. `aws s3api list-buckets --output json`
   *Verify S3 storage for incident reports and evidence*

9. `aws cloudwatch describe-alarms --output json 2>/dev/null || echo '{"MetricAlarms":[]}'`
   *Check monitoring alarms for incident detection/script health*

## Latest Results

- FAIL KSI-INR-02 NOT MET (score: 0): Missing - need 2 more EventBridge rules, need 4 more log groups, enable GuardDuty or Security Hub, no automation evidence. Found: No components detected

---
*Generated 2025-09-20 01:37 UTC*