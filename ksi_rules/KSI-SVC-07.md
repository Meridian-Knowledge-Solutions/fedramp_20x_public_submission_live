# KSI-SVC-07: Use a consistent, risk-informed approach for applying security patches

## Overview

**Category:** Service Configuration
**Status:** PASS
**Last Check:** 2025-09-23 18:57

**What it validates:** Use a consistent, risk-informed approach for applying security patches

**Why it matters:** Validates comprehensive risk-informed patch management from basic patch baseline configuration to enterprise-grade vulnerability-driven patching, covering automated deployment, compliance monitoring, container patching, lambda layer management, and organizational patch governance with risk assessment and testing workflows

## Validation Method

1. `aws ssm describe-patch-baselines --output json`
   *Check patch baselines for consistent patching approach and vulnerability management standards*

2. `aws ssm describe-instance-information --output json`
   *Validate SSM agent coverage for automated patching and centralized system management*

3. `aws ssm describe-patch-groups --output json`
   *Analyze patch groups for risk-informed patching segmentation and deployment scheduling*

4. `aws ssm list-documents --document-filter-list key=DocumentType,value=Command --output json`
   *Check SSM documents for patch automation workflows and risk-informed deployment procedures*

5. `aws ssm describe-maintenance-windows --output json`
   *Validate maintenance windows for controlled patch deployment and risk mitigation scheduling*

6. `aws inspector2 get-configuration --output json`
   *Check Inspector for vulnerability-driven patch prioritization and risk assessment automation*

7. `aws ecr describe-repositories --output json`
   *Analyze container registries for container image patching and vulnerability scanning integration*

8. `aws lambda list-layers --output json`
   *Check Lambda layers for serverless runtime patching and dependency management*

9. `aws config describe-config-rules --output json`
   *Validate Config rules for patch compliance monitoring and governance automation*

10. `aws organizations describe-organization --output json`
   *Check enterprise-wide patch management policies and organizational risk-informed patching standards across accounts*

## Latest Results

PASS Advanced risk-informed patching with controlled deployment and compliance (55%): PASS Consistent patch management: 17 patch baselines configured.
- PASS Automated patch deployment capability: 6/6 instances with SSM agent online (100%).
- PASS Patch automation framework: 14 documents for automated patching.
- PASS Serverless patch management: 1 Lambda layers for runtime dependency management.
- PASS Enterprise-wide patch governance: AWS Organizations enables centralized policies.
- PASS Advanced organization features: SCPs for patch management policy enforcement enabled.

---
*Generated 2025-09-23 18:57 UTC*