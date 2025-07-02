# KSI-INR-03: Generate after action reports and regularly incorporate lessons learned into operations with automated incident tracking

## Overview

**Category:** Incident Reporting
**Status:** PASS
**Last Check:** 2025-07-02 03:18

**What it validates:** Generate after action reports and regularly incorporate lessons learned into operations with automated incident tracking

**Why it matters:** Hybrid validation combining automated SecurityHub incident analysis with manual after action report documentation

## Validation Method

1. `aws securityhub get-insights --output json`
   *Retrieve SecurityHub insights to identify available incident analysis capabilities*

2. `aws securityhub get-insight-results --insight-arn arn:aws:securityhub:us-east-1:893894210484:insight/893894210484/custom/5bcb2cd3-64e4-4493-b0ea-0dd45ec3b08c --output json`
   *Get specific incident insight results for after action analysis - production account specific*

3. `aws securityhub get-findings --filters '{"WorkflowState":[{"Value":"RESOLVED","Comparison":"EQUALS"}]}' --max-items 10 --output json`
   *Retrieve resolved security findings to demonstrate incident resolution and lessons learned*

4. `aws securityhub describe-standards --output json`
   *Verify security standards are being tracked for continuous improvement*

5. **Manual Review:** Check evidence_v2/KSI-INR-03/ for after_action_reports.pdf, lessons_learned_database.xlsx, operational_improvements_tracking.pdf, and incident_response_improvements.pdf

## Latest Results

WARNING Basic after action reporting (increase lessons learned implementation): PASS Core after action documentation: Sample After Action Reports and Implementation Examples.pdf
- PASS Recent after action reports: 2 AARs within last year
- WARNING Limited evidence of lessons learned implementation into operations

---
*Generated 2025-07-02 03:18 UTC*