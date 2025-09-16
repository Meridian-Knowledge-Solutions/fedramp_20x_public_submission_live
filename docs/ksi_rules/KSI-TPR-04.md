# KSI-TPR-04: Monitor third party software for upstream vulnerabilities

## Overview

**Category:** Third-Party Information Resources
**Status:** FAIL
**Last Check:** 2025-09-16 05:51

**What it validates:** Monitor third party software for upstream vulnerabilities

**Why it matters:** AWS Inspector and ECR vulnerability scanning provides automated monitoring of third-party software components and container images

## Validation Method

1. `aws inspector2 get-configuration --output json`
   *Inspector configuration status for automated vulnerability scanning*

2. `aws inspector2 list-findings --filter-criteria '{"findingStatus":[{"value":"ACTIVE","comparison":"EQUALS"}]}' --max-results 50 --output json`
   *Active vulnerability findings from automated scanning*

3. `aws inspector2 list-findings --filter-criteria '{"componentType":[{"value":"NPM","comparison":"EQUALS"}]}' --max-results 20 --output json`
   *NPM package vulnerabilities in third-party JavaScript dependencies*

4. `aws inspector2 list-findings --filter-criteria '{"componentType":[{"value":"PYTHON_PKG","comparison":"EQUALS"}]}' --max-results 20 --output json`
   *Python package vulnerabilities in third-party Python dependencies*

5. `aws ecr describe-repositories --output json`
   *ECR repositories for container image vulnerability scanning*

6. `aws ecr describe-image-scan-findings --repository-name $(aws ecr describe-repositories --query 'repositories[0].repositoryName' --output text) --image-id imageTag=latest --output json 2>/dev/null || echo '{"imageScanFindings":{"findings":[]}}'`
   *Container image vulnerability scan findings for third-party components*

## Latest Results

- FAIL No automated third-party vulnerability monitoring infrastructure: No monitoring capabilities detected

---
*Generated 2025-09-16 05:51 UTC*