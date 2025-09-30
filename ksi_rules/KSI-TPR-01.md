# KSI-TPR-01: Identify all third-party information resources

## Overview

**Category:** Third-Party Information Resources
**Status:** PASS
**Last Check:** 2025-09-30 00:27

**What it validates:** Identify all third-party information resources

**Why it matters:** Automated discovery via compliance broker logs (dynamic) and Parameter Store whitelist (static)

## Validation Method

1. `aws lambda list-functions --query 'Functions[?contains(FunctionName, `broker`) || contains(FunctionName, `compliance`)].FunctionName' --output json`
   *Verify compliance broker is deployed*

2. `aws logs describe-log-groups --log-group-name-prefix '/aws/lambda/' --query 'logGroups[?contains(logGroupName, `broker`)]' --output json`
   *Confirm broker logging is active*

3. `aws logs get-query-results --query-id $(aws logs start-query --log-group-name '/aws/lambda/lms-compliance-broker' --start-time $(date -d '30 days ago' +%s) --end-time $(date +%s) --query-string 'fields destination_url | parse destination_url /https?:\/\/(?<host>[^\/]+)/ | stats count() by host' --output text --query 'queryId') --output json`
   *Retrieve third-party hosts from broker logs*

4. `aws ssm get-parameter --name "/lms-compliance/policies" --output json`
   *Retrieve the static third-party whitelist from Parameter Store (static evidence)*

## Latest Results

- PASS Third-party resources identified via static configuration: PASS Static discovery: 5 third-party services identified from whitelist

---
*Generated 2025-09-30 00:27 UTC*