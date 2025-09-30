# KSI-TPR-04: Monitor third party software for upstream vulnerabilities

## Overview

**Category:** Third-Party Information Resources
**Status:** PASS
**Last Check:** 2025-09-30 00:27

**What it validates:** Monitor third party software for upstream vulnerabilities

**Why it matters:** AWS Inspector for EC2 instances provides automated monitoring of third-party application packages and dependencies (Python, NPM, etc.) that process federal information

## Validation Method

1. `aws inspector2 get-configuration --output json`
   *Inspector configuration status for automated third-party package vulnerability scanning*

2. `aws inspector2 list-findings --filter-criteria '{"componentType":[{"value":"PYTHON_PKG","comparison":"EQUALS"}]}' --max-results 20 --output json`
   *Python package vulnerabilities in third-party dependencies (boto3, requests, etc.)*

3. `aws inspector2 list-findings --filter-criteria '{"componentType":[{"value":"NPM","comparison":"EQUALS"}]}' --max-results 20 --output json`
   *NPM package vulnerabilities in third-party JavaScript dependencies*

4. `aws inspector2 list-findings --filter-criteria '{"findingStatus":[{"value":"ACTIVE","comparison":"EQUALS"}]}' --max-results 30 --output json`
   *All active vulnerability findings to verify Inspector scanning capability*

5. `aws inspector2 list-coverage --filter-criteria '{"resourceType":[{"value":"EC2","comparison":"EQUALS"}]}' --output json`
   *Inspector coverage validation for EC2 instances available for package scanning*

6. `aws ssm describe-instance-information --output json`
   *Systems Manager agent status for third-party package inventory and dependency tracking*

## Latest Results

WARNING Basic monitoring infrastructure - deploy third-party packages for full coverage (40%): PASS Inspector coverage service active - verify instances enrolled for package scanning
- PASS Package inventory capability: 6 instances with SSM agent for dependency tracking

---
*Generated 2025-09-30 00:27 UTC*