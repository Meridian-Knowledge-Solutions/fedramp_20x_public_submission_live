# KSI-TPR-02: Regularly confirm that services handling federal information or are likely to impact the confidentiality, integrity, or availability of federal information are FedRAMP authorized and securely configured

## Overview

**Category:** Third-Party Information Resources
**Status:** PASS
<<<<<<< Updated upstream
**Last Check:** 2025-09-08 18:55
=======
**Last Check:** 2025-09-08 19:00
>>>>>>> Stashed changes

**What it validates:** Regularly confirm that services handling federal information or are likely to impact the confidentiality, integrity, or availability of federal information are FedRAMP authorized and securely configured

**Why it matters:** Validates FedRAMP authorization verification through service assessment, compliance monitoring, and authorization status tracking

## Validation Method

1. `aws organizations list-accounts --output json`
   *Check organizational structure for FedRAMP authorized service boundaries*

2. **Manual Review:** Check evidence_v2/KSI-TPR-02/ for fedramp_authorization_verification.xlsx, service_authorization_status.pdf, compliance_monitoring_procedures.pdf, and federal_data_handling_matrix.pdf

## Latest Results

PASS Comprehensive FedRAMP service verification with integrated documentation (100%): INFO Evidence validation triggered via CLI
- PASS Comprehensive federal information mapping: Federal Information Mapping - Meridian LMS.pdf
- PASS FedRAMP authorization verification included in comprehensive mapping
- PASS Security configuration compliance included in comprehensive mapping
- PASS Regular verification process included in comprehensive mapping

---
<<<<<<< Updated upstream
*Generated 2025-09-08 18:55 UTC*
=======
*Generated 2025-09-08 19:00 UTC*
>>>>>>> Stashed changes
