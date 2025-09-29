# KSI-PIY-06: Have staff and budget for security commensurate with the size, complexity, scope, executive priorities, and risk of the service offering that demonstrates commitment to delivering a secure service

## Overview

**Category:** Policy and Inventory
**Status:** FAIL
**Last Check:** 2025-09-29 22:00

**What it validates:** Have staff and budget for security commensurate with the size, complexity, scope, executive priorities, and risk of the service offering that demonstrates commitment to delivering a secure service

**Why it matters:** For small teams, this validates security commitment by measuring operational participation from all types of human users (IAM, SSO, Federated). It uses activity proxies and scales expectations based on account complexity.

## Validation Method

1. `aws cloudtrail lookup-events --lookup-attributes AttributeKey=EventName,AttributeValue=ConsoleLogin`
   *Identifies recent, unique human principals (IAM, SSO, Federated) logging into the console. The calling script must add dynamic start/end times for the last 60 days.*

2. `aws cloudtrail lookup-events --lookup-attributes AttributeKey=EventName,AttributeValue=CreateRole`
   *Checks for recent IAM role creation. The calling script must add dynamic start/end times for the last 60 days.*

3. `aws cloudtrail lookup-events --lookup-attributes AttributeKey=EventName,AttributeValue=AttachRolePolicy`
   *Checks for recent IAM policy management. The calling script must add dynamic start/end times for the last 60 days.*

4. `aws securityhub get-findings --filters '{"WorkflowState":[{"Value":"RESOLVED","Comparison":"EQUALS"}],"UpdatedAt":{"DateRange":{"Value":60,"Unit":"DAYS"}}}' --max-items 20 --query 'Findings[*].{Id:Id,UpdatedAt:UpdatedAt,Title:Title}'`
   *Finds recently resolved Security Hub findings, indicating active security response.*

5. `aws lambda list-functions --query 'Functions[?Tags.Purpose==`security-automation`].{FunctionName:FunctionName,Role:Role}'`
   *Identifies security automation infrastructure by looking for a specific tag, which is more reliable than name matching.*

6. `aws configservice describe-config-rules --query 'ConfigRules[?ConfigRuleState==`ACTIVE`].[ConfigRuleName,ConfigRuleState]'`
   *Verifies active compliance monitoring is in place as a core security practice.*

7. `aws iam list-roles --query 'Roles[*].RoleName'`
   *Provides a simple metric for account complexity (total number of roles) to scale IAM activity thresholds.*

## Latest Results

- FAIL: Insufficient security commitment (0/4). Lacking evidence in: Active Principals Identified, Recent Iam Management, Security Monitoring Active, Security Automation Present.

---
*Generated 2025-09-29 22:00 UTC*