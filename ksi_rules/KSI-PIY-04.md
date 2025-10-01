# KSI-PIY-04: Maintain an inventory of authorized software

## Overview

**Category:** Policy and Inventory
**Status:** PASS
**Last Check:** 2025-10-01 06:31

**What it validates:** Maintain an inventory of authorized software

**Why it matters:** Validates comprehensive authorized software management from basic allow-lists to enterprise-grade application control and compliance tracking

## Validation Method

1. `aws codebuild list-projects --output json`
   *Check CodeBuild for authorized software deployment pipelines*

2. `aws codepipeline list-pipelines --output json`
   *Validate CodePipeline for authorized software deployment*

3. `aws lambda list-functions --output json`
   *Check Lambda functions for authorized serverless software*

4. `aws organizations describe-organization --output json`
   *Validate organization-wide authorized software policies*

## Latest Results

PASS Comprehensive SDLC security integration with enterprise automation (100%): PASS Build Security Integration
- PASS Pipeline Security Gates
- PASS Security Automation Functions
- PASS Development Governance

---
*Generated 2025-10-01 06:31 UTC*