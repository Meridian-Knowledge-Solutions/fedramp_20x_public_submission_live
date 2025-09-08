# KSI-PIY-04: Build security considerations into SDLC and align with CISA Secure By Design principles

## Overview

**Category:** Policy and Inventory
**Status:** PASS
<<<<<<< Updated upstream
**Last Check:** 2025-09-08 18:55
=======
**Last Check:** 2025-09-08 19:00
>>>>>>> Stashed changes

**What it validates:** Build security considerations into SDLC and align with CISA Secure By Design principles

**Why it matters:** Validates secure development lifecycle through CodeBuild security testing, pipeline security gates, and alignment with CISA Secure By Design principles

## Validation Method

1. `aws codebuild list-projects --output json`
   *Check CodeBuild projects for security testing integration in SDLC*

2. `aws codepipeline list-pipelines --output json`
   *Validate CodePipeline for security gates and SDLC security integration*

3. `aws ecr describe-repositories --output json`
   *Check ECR repositories for container security scanning in development workflow*

4. **Manual Review:** Check evidence_v2/KSI-PIY-04/ for secure_sdlc_procedures.pdf, cisa_secure_by_design_alignment.pdf, security_testing_integration.pdf, and development_security_standards.pdf

## Latest Results

- WARNING Basic secure development practices (expand documentation): PASS Secure SDLC documentation: Secure Software Development Lifecycle (SDLC) Policy.pdf

---
<<<<<<< Updated upstream
*Generated 2025-09-08 18:55 UTC*
=======
*Generated 2025-09-08 19:00 UTC*
>>>>>>> Stashed changes
