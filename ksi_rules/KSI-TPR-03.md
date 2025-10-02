# KSI-TPR-03: Document all third-party services used in the system security policy

## Overview

**Category:** Third-Party Information Resources
**Status:** PASS
**Last Check:** 2025-10-02 03:01

**What it validates:** Document all third-party services used in the system security policy

**Why it matters:** Validates third-party service documentation from basic vendor lists to enterprise-grade supply chain risk management and compliance tracking

## Validation Method

1. `aws ssm get-parameter --name '/lms-compliance/policies' --output json || echo '{"Parameter": null}'`
   *Check SSM Parameter Store for third-party service documentation*

## Latest Results

PASS Supply chain risks identified and mitigation prioritized via broker policies: PASS Identification: 5 third-party services identified.
- PASS Prioritization & Mitigation: Tiered policies for high and low-impact tenants are configured.

---
*Generated 2025-10-02 03:01 UTC*