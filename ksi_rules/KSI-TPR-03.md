# KSI-TPR-03: Identify and prioritize mitigation of potential supply chain risks

## Overview

**Category:** Third-Party Information Resources
**Status:** PASS
**Last Check:** 2025-09-26 17:30

**What it validates:** Identify and prioritize mitigation of potential supply chain risks

**Why it matters:** Automated validation of risk identification and mitigation via the compliance broker's tiered policy configuration in Parameter Store.

## Validation Method

1. `aws ssm get-parameter --name "/lms-compliance/policies" --output json`
   *Verify the codified risk management plan (the broker's policies)*

2. `aws logs get-query-results --query-id $(aws logs start-query --log-group-name '/aws/lambda/lms-compliance-broker' --start-time $(date -d '30 days ago' +%s) --end-time $(date +%s) --query-string 'fields destination_url | parse destination_url /https?:\/\/(?<host>[^\/]+)/ | stats count() by host' --output text --query 'queryId') --output json`
   *Identify third-party services via dynamic logs*

## Latest Results

PASS Supply chain risks identified and mitigation prioritized via broker policies: PASS Identification: 5 third-party services identified.
- PASS Prioritization & Mitigation: Tiered policies for high and low-impact tenants are configured.

---
*Generated 2025-09-26 17:30 UTC*