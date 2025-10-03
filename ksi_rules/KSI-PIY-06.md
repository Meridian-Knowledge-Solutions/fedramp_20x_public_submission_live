# KSI-PIY-06: Have dedicated security staff and budget with executive support

## Overview

**Category:** Policy and Inventory
**Status:** PASS
**Last Check:** 2025-10-03 19:13

**What it validates:** Have dedicated security staff and budget with executive support

**Why it matters:** Validates organizational commitment to security through active personnel engagement, tooling investment, monitoring capabilities, and governance structure appropriate to organization size

## Validation Method

1. `aws cloudtrail lookup-events --lookup-attributes AttributeKey=EventName,AttributeValue=ConsoleLogin --start-time $(date -u -d '30 days ago' '+%Y-%m-%dT%H:%M:%S') --max-items 50 --output json`
   *Measure active security team engagement*

2. `aws cloudtrail lookup-events --lookup-attributes AttributeKey=EventName,AttributeValue=PutConfigRule --start-time $(date -u -d '90 days ago' '+%Y-%m-%dT%H:%M:%S') --max-items 50 --output json`
   *Evidence of Config rule deployment activity*

3. `aws cloudtrail lookup-events --lookup-attributes AttributeKey=EventName,AttributeValue=PutMetricAlarm --start-time $(date -u -d '90 days ago' '+%Y-%m-%dT%H:%M:%S') --max-items 50 --output json`
   *Evidence of CloudWatch alarm deployment activity*

4. `aws configservice describe-config-rules --output json`
   *Count deployed Config rules*

5. `aws cloudwatch describe-alarms --query 'MetricAlarms[?contains(AlarmName, `Security`) || contains(AlarmName, `Unauthorized`) || contains(AlarmName, `IAM`) || contains(AlarmName, `Root`)]' --output json`
   *Count security monitoring alarms*

6. `aws lambda list-functions --query 'Functions[?contains(FunctionName, `security`) || contains(FunctionName, `incident`) || contains(FunctionName, `compliance`)]' --output json`
   *Count security automation functions*

## Latest Results

PASS Adequate security commitment (6/10 = 60%): PASS Active engagement: 46 logins, 2 principal(s)
- PASS Config deployment activity: 50 rule deployment(s)
- PASS Alarm deployment activity: 13 alarm deployment(s)
- PASS Config rules deployed: 327 rules
- FAIL No security alarms configured
- FAIL No security Lambda functions

---
*Generated 2025-10-03 19:13 UTC*