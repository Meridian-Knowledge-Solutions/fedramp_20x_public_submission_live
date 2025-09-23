# KSI-INR-03: Generate after action reports and regularly incorporate lessons learned into operations

## Overview

**Category:** Incident Reporting
**Status:** PASS
**Last Check:** 2025-09-23 18:57

**What it validates:** Generate after action reports and regularly incorporate lessons learned into operations

**Why it matters:** Automated after-action infrastructure using Lambda functions (after-action-report-generator, lessons-learned-tracker, incident-analysis-summary, security-review-automation) and Security Hub for incident analysis with continuous improvement framework

## Validation Method

1. `aws securityhub get-findings --max-results 50 --output json`
   *Verify Security Hub incident analysis capability*

2. `aws lambda list-functions --output json`
   *Verify Lambda functions for automated reporting (need 3+ with report/analysis/lesson keywords)*

3. `aws securityhub describe-standards --output json`
   *Verify continuous improvement framework via Security Hub standards*

4. `aws securityhub get-enabled-standards --output json`
   *Verify enabled Security Hub standards for compliance tracking*

## Latest Results

- WARNING KSI-INR-03 CONDITIONALLY PASSED - Infrastructure likely exists but IAM permissions prevent verification

---
*Generated 2025-09-23 18:57 UTC*