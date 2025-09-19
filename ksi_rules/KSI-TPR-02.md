# KSI-TPR-02: Regularly confirm that services handling federal information or are likely to impact the confidentiality, integrity, or availability of federal information are FedRAMP authorized and securely configured

## Overview

**Category:** Third-Party Information Resources
**Status:** PASS
**Last Check:** 2025-09-16 07:31

**What it validates:** Regularly confirm that services handling federal information or are likely to impact the confidentiality, integrity, or availability of federal information are FedRAMP authorized and securely configured

**Why it matters:** Validates FedRAMP authorization verification through service assessment, compliance monitoring, and authorization status tracking

## Validation Method

1. `aws organizations list-accounts --output json`
   *Check organizational structure for FedRAMP authorized service boundaries*

2. **Manual Review:** Check evidence_v2/KSI-TPR-02/ for fedramp_authorization_verification.xlsx, service_authorization_status.pdf, compliance_monitoring_procedures.pdf, and federal_data_handling_matrix.pdf

## Latest Results

- PASS KSI retired in Phase Two - superseded by KSI-TPR-01 (FedRAMP Minimum Assessment Standard)

---
*Generated 2025-09-16 07:31 UTC*