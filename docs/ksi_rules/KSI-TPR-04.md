# KSI-TPR-04: Monitor third party software for upstream vulnerabilities

## Overview

**Category:** Third-Party Information Resources
**Status:** PASS
**Last Check:** 2025-09-17 07:11

**What it validates:** Monitor third party software for upstream vulnerabilities

**Why it matters:** AWS Inspector for EC2 instances provides automated monitoring of third-party software packages and system dependencies

## Validation Method

1. `aws inspector2 get-configuration --output json`
   *Inspector configuration status for automated EC2 vulnerability scanning*

2. `aws inspector2 list-findings --filter-criteria '{"findingStatus":[{"value":"ACTIVE","comparison":"EQUALS"}]}' --max-results 50 --output json`
   *Active vulnerability findings from EC2 instance scanning*

3. `aws inspector2 list-findings --filter-criteria '{"componentType":[{"value":"PYTHON_PKG","comparison":"EQUALS"}]}' --max-results 20 --output json`
   *Python package vulnerabilities in third-party dependencies on EC2 instances*

4. `aws inspector2 list-findings --filter-criteria '{"resourceType":[{"value":"EC2_INSTANCE","comparison":"EQUALS"}]}' --max-results 30 --output json`
   *EC2 instance-specific vulnerability findings for installed packages*

5. `aws ssm describe-instance-information --output json`
   *Systems Manager agent status for package inventory and vulnerability scanning*

6. `aws inspector2 list-coverage --filter-criteria '{"resourceType":[{"value":"EC2","comparison":"EQUALS"}]}' --output json`
   *Inspector coverage validation for EC2 instances*

## Latest Results

WARNING Basic EC2 monitoring capability - expand coverage (40%): PASS Python package vulnerability scanning active - no current vulnerabilities detected
- PASS Systems Manager package inventory: 5 instances with SSM agent for dependency tracking

---
*Generated 2025-09-17 07:11 UTC*