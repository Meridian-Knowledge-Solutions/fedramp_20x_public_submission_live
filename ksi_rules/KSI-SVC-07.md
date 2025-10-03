# KSI-SVC-07: Perform regularly scheduled scans for vulnerabilities and apply patches promptly

## Overview

**Category:** Service Configuration
**Status:** PASS
**Last Check:** 2025-10-03 22:39

**What it validates:** Perform regularly scheduled scans for vulnerabilities and apply patches promptly

**Why it matters:** Validates comprehensive vulnerability management from basic patch baselines to enterprise-grade automated scanning, remediation, and compliance

## Validation Method

1. `aws ssm describe-patch-baselines --output json`
   *Check SSM patch baselines for vulnerability management*

2. `aws ssm describe-instance-information --output json`
   *Validate SSM managed instances for patch compliance*

3. `aws ssm describe-patch-groups --output json`
   *Check patch groups for organized vulnerability remediation*

4. `aws ssm list-documents --document-filter-list key=DocumentType,value=Automation --output json`
   *Validate SSM automation for scheduled patch deployment*

5. `aws ssm describe-maintenance-windows --output json`
   *Check maintenance windows for scheduled patching operations*

6. `aws inspector2 get-configuration --output json`
   *Validate Inspector for continuous vulnerability scanning*

7. `aws ecr describe-repositories --output json`
   *Check ECR repositories for container image vulnerability scanning*

8. `aws lambda list-layers --output json`
   *Validate Lambda layers for serverless vulnerability management*

9. `aws organizations describe-organization --output json`
   *Check organization-wide vulnerability management policies*

## Latest Results

PASS Advanced risk-informed patching with controlled deployment and compliance (55%): PASS Consistent patch management: 17 patch baselines configured.
- PASS Automated patch deployment capability: 6/6 instances with SSM agent online (100%).
- PASS Patch automation framework: 27 documents for automated patching.
- PASS Serverless patch management: 1 Lambda layers for runtime dependency management.
- PASS Enterprise-wide patch governance: AWS Organizations enables centralized policies.
- PASS Advanced organization features: SCPs for patch management policy enforcement enabled.

---
*Generated 2025-10-03 22:39 UTC*