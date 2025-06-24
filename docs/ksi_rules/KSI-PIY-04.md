# KSI-PIY-04: Build security considerations into SDLC and align with CISA Secure By Design principles

## Overview

**Category:** Policy and Inventory
**Status:** PASS
**Last Check:** 2025-06-24 17:21

**What it validates:** Build security considerations into SDLC and align with CISA Secure By Design principles

**Why it matters:** Validates secure development through CodeCommit, CodeBuild security scanning, and SDLC documentation

## Validation Method

1. `aws codecommit list-repositories --output json`
   *Check code repositories for secure development practices*

2. **Manual Review:** Check evidence_v2/KSI-PIY-04/ for secure_sdlc_procedures.pdf and cisa_secure_by_design_alignment.pdf

## Latest Results

WARNING Basic secure development practices (expand documentation): INFO No CodeCommit repositories (may use external source control)
- PASS Secure SDLC documentation: Secure Software Development Lifecycle (SDLC) Policy.pdf

---
*Generated 2025-06-24 17:21 UTC*