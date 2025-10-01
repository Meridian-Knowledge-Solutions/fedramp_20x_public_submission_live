# KSI-SVC-08: Use infrastructure as code to apply controls to the provisioning and management of resources

## Overview

**Category:** Service Configuration
**Status:** PASS
**Last Check:** 2025-10-01 08:13

**What it validates:** Use infrastructure as code to apply controls to the provisioning and management of resources

**Why it matters:** Validates comprehensive IaC implementation from basic CloudFormation to enterprise-grade policy-driven deployment and automated compliance

## Validation Method

1. `aws cloudformation list-stacks --output json`
   *Check CloudFormation stacks for infrastructure as code deployment*

2. `aws lambda list-functions --output json`
   *Validate Lambda functions for IaC automation and deployment*

3. `aws events list-rules --output json`
   *Check EventBridge rules for automated IaC workflows*

4. **Manual Review:** Manual review of IaC templates, policies, and deployment pipelines

## Latest Results

PASS Good change cleanup processes (60%): PASS Infrastructure As Code
- PASS Automated Cleanup
- PASS Resource Lifecycle Management
- FAIL Residual Element Detection
- FAIL Change Impact Tracking

---
*Generated 2025-10-01 08:13 UTC*