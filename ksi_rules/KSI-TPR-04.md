# KSI-TPR-04: Conduct vulnerability scans for applications and operating systems

## Overview

**Category:** Third-Party Information Resources
**Status:** PASS
**Last Check:** 2025-10-01 08:13

**What it validates:** Conduct vulnerability scans for applications and operating systems

**Why it matters:** Validates comprehensive vulnerability scanning from basic Inspector to enterprise-grade continuous scanning and automated remediation

## Validation Method

1. `aws inspector2 get-configuration --output json`
   *Check Inspector configuration for vulnerability scanning*

2. `aws inspector2 list-findings --filter-criteria '{"componentType":[{"comparison":"EQUALS","value":"OPERATING_SYSTEM"}]}' --max-results 50 --output json`
   *Validate OS vulnerability findings from Inspector*

3. `aws inspector2 list-findings --filter-criteria '{"componentType":[{"comparison":"EQUALS","value":"APPLICATION"}]}' --max-results 50 --output json`
   *Check application vulnerability findings from Inspector*

4. `aws inspector2 list-findings --filter-criteria '{"findingStatus":[{"comparison":"EQUALS","value":"ACTIVE"}]}' --max-results 100 --output json`
   *Validate active vulnerability findings requiring remediation*

5. `aws inspector2 list-coverage --filter-criteria '{"resourceType":[{"comparison":"EQUALS","value":"AWS_EC2_INSTANCE"}]}' --max-results 100 --output json`
   *Check Inspector coverage for EC2 instances*

6. `aws ssm describe-instance-information --output json`
   *Validate SSM agent deployment for vulnerability management*

## Latest Results

PASS Good third-party package monitoring - expand coverage (40%): PASS EC2 Inspector coverage verified: 6 instances available for third-party package scanning
- PASS Package inventory capability: 6 instances with SSM agent for dependency tracking

---
*Generated 2025-10-01 08:13 UTC*