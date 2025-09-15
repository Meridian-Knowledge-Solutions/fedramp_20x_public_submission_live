# KSI-INR-02: Maintain a log of incidents and periodically review past incidents for patterns or vulnerabilities

## Overview

**Category:** Incident Reporting
**Status:** PASS
**Last Check:** 2025-09-15 01:58

**What it validates:** Maintain a log of incidents and periodically review past incidents for patterns or vulnerabilities

**Why it matters:** Validates incident tracking through CloudTrail integration, EventBridge logs, and manual evidence of incident database with pattern analysis

## Validation Method

1. `aws events list-rules --output json`
   *Check automated incident detection and logging rules*

2. `aws logs describe-log-groups --log-group-name-prefix '/aws/events/' --output json`
   *Validate incident logging infrastructure in CloudWatch*

3. **Manual Review:** Check evidence_v2/KSI-INR-02/ for incident_database.xlsx, incident_pattern_analysis_report.pdf, and quarterly_incident_review_minutes.pdf

## Latest Results

WARNING Good incident logging (increase analysis frequency): WARNING No dedicated security log groups found (may use general logging)
- PASS Incident tracking and analysis: Incident Tracking and Analysis Template (KSI-INR-02).pdf
- PASS Recent reviews: 1 incident analysis documents updated within 6 months

---
*Generated 2025-09-15 01:58 UTC*