# KSI-TPR-04: Monitor third party software information resources for upstream vulnerabilities, with contractual notification requirements or active monitoring services

## Overview

**Category:** Third-Party Information Resources
**Status:** PASS
<<<<<<< Updated upstream
**Last Check:** 2025-09-08 18:55
=======
**Last Check:** 2025-09-08 19:00
>>>>>>> Stashed changes

**What it validates:** Monitor third party software information resources for upstream vulnerabilities, with contractual notification requirements or active monitoring services

**Why it matters:** Validates third-party vulnerability monitoring through Inspector, Security Hub, and active monitoring of external dependencies

## Validation Method

1. `aws inspector2 get-configuration --output json`
   *Check Inspector for third-party component vulnerability monitoring*

2. `aws securityhub describe-hub --output json`
   *Validate Security Hub for third-party vulnerability finding aggregation*

3. **Manual Review:** Check evidence_v2/KSI-TPR-04/ for vendor_vulnerability_monitoring_contracts.pdf, upstream_vulnerability_alerts.xlsx, and third_party_monitoring_procedures.pdf

## Latest Results

WARNING Basic vulnerability monitoring capability: WARNING Inspector vulnerability monitoring not accessible
- PASS Manual evidence validation completed (vulnerability monitoring documentation verified)

---
<<<<<<< Updated upstream
*Generated 2025-09-08 18:55 UTC*
=======
*Generated 2025-09-08 19:00 UTC*
>>>>>>> Stashed changes
