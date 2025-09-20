# KSI-INR-03: Generate after action reports and regularly incorporate lessons learned into operations

## Overview

**Category:** Incident Reporting
**Status:** FAIL
**Last Check:** 2025-09-20 00:52

**What it validates:** Generate after action reports and regularly incorporate lessons learned into operations

**Why it matters:** Automated after-action infrastructure using Lambda functions (after-action-report-generator, lessons-learned-tracker, incident-analysis-summary, security-review-automation), Security Hub for incident analysis, and resolved findings tracking for lessons learned implementation

## Validation Method

1. `aws securityhub get-findings --max-results 50 --output json`
   *Verify Security Hub incident analysis capability for after-action review*

2. `aws lambda list-functions --output json`
   *Verify Lambda functions for automated reporting (need 3+ with report/analysis/lesson/review keywords)*

3. `aws securityhub describe-standards --output json`
   *Verify continuous improvement framework via Security Hub standards*

4. `aws securityhub get-findings --filters '{"RecordState":[{"Value":"RESOLVED","Comparison":"EQUALS"}]}' --max-results 20 --output json 2>/dev/null || echo '{"Findings":[]}'`
   *Validate resolved findings demonstrating lessons learned implementation*

5. `aws securityhub get-enabled-standards --output json 2>/dev/null || echo '{"StandardsSubscriptions":[]}'`
   *Verify enabled Security Hub standards for compliance tracking*

## Latest Results

- FAIL Insufficient after-action infrastructure (score: 0): Missing - need 3 more Lambda functions, Security Hub findings analysis not available, no continuous improvement framework

---
*Generated 2025-09-20 00:52 UTC*