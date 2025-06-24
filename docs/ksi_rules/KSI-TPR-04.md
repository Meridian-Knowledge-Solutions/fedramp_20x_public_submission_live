# KSI-TPR-04: Monitor third party software for upstream vulnerabilities with contractual notification or active monitoring

## Overview

**Category:** Third-Party Information Resources
**Status:** PASS
**Last Check:** 2025-06-24 00:57

**What it validates:** Monitor third party software for upstream vulnerabilities with contractual notification or active monitoring

**Why it matters:** Validates vulnerability monitoring through Inspector, Security Hub, and contractual requirements documentation

## Validation Method

1. `aws inspector2 list-findings --max-results 20 --output json`
   *Check Inspector findings for third-party component vulnerabilities*

2. **Manual Review:** Check evidence_v2/KSI-TPR-04/ for vulnerability_monitoring_contracts.pdf, upstream_vulnerability_procedures.pdf, and third_party_notification_agreements.pdf

## Latest Results

PASS Third-party software vulnerability monitoring established: PASS Active third-party vulnerability monitoring: 20 component vulnerabilities detected
- PASS Manual evidence validation completed (vulnerability monitoring documentation verified)

---
*Generated 2025-06-24 00:57 UTC*