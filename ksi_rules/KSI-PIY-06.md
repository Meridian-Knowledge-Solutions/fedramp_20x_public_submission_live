# KSI-PIY-06: Maintain policies for incident response and reporting

## Overview

**Category:** Policy and Inventory
**Status:** FAIL
**Last Check:** 2025-10-01 08:13

**What it validates:** Maintain policies for incident response and reporting

**Why it matters:** Validates comprehensive incident management from basic response procedures to enterprise-grade automated detection and forensics

## Validation Method

1. `aws cloudtrail lookup-events --lookup-attributes AttributeKey=EventName,AttributeValue=ConsoleLogin --max-items 50 --output json`
   *Check CloudTrail for authentication incident detection*

2. `aws cloudtrail lookup-events --lookup-attributes AttributeKey=EventName,AttributeValue=CreateAccessKey --max-items 50 --output json`
   *Validate CloudTrail for access key creation monitoring*

3. `aws cloudtrail lookup-events --lookup-attributes AttributeKey=EventName,AttributeValue=DeleteBucket --max-items 50 --output json`
   *Check CloudTrail for destructive action monitoring*

4. `aws lambda list-functions --query 'Functions[?Tags.Purpose==`IncidentResponse`]' --output json || echo '{"Functions": []}'`
   *Validate Lambda functions for automated incident response*

5. `aws configservice describe-config-rules --query 'ConfigRules[?contains(ConfigRuleName, `incident`) || contains(ConfigRuleName, `security`)].ConfigRuleName' --output json`
   *Check Config rules for incident detection automation*

6. `aws iam list-roles --query 'Roles[*].RoleName' --output json`
   *Validate IAM roles for incident response team access*

## Latest Results

- FAIL: Insufficient security commitment (0/4). Lacking evidence in: Active Principals Identified, Recent Iam Management, Security Monitoring Active, Security Automation Present.

---
*Generated 2025-10-01 08:13 UTC*