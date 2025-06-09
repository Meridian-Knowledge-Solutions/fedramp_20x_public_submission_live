# KSI-CMT-03: Implement automated testing and validation of changes prior to deployment

*Generated on 2025-06-09 08:02:50 UTC*

## 📖 Overview

**KSI ID:** `KSI-CMT-03`
**Description:** Implement automated testing and validation of changes prior to deployment
**Justification:** Validates automated testing through CodeBuild, CodePipeline, and pre-deployment validation
**Last Validation:** ✅ 2025-06-09T08:02:50.228210
**Result:** ✅ Comprehensive automated testing via Infrastructure as Code: Infrastructure as Code security scanning; SARIF security reports generated; Checkov compliance validation

## 🛠️ Implementation

### Commands Executed
1. **Command:** `aws codebuild list-projects --output json`
   **Purpose:** Check CodeBuild projects for automated testing

2. **Command:** `aws codepipeline list-pipelines --output json`
   **Purpose:** Validate CodePipeline for automated change validation

## 📋 Evidence Requirements

### 🖥️ CLI Validation
- **Command:** `aws codebuild list-projects --output json`
  - **Purpose:** Check CodeBuild projects for automated testing
- **Command:** `aws codepipeline list-pipelines --output json`
  - **Purpose:** Validate CodePipeline for automated change validation

## 🧠 Validation Logic

**Function:** `evaluate_KSI_CMT_03`

**Documentation:** KSI-CMT-03: Implement automated testing and validation of changes prior to deployment

Updated to recognize Infrastructure as Code security scanning via Checkov
instead of traditional CodeBuild/CodePipeline approaches.

### Rule Implementation
```python
def evaluate_KSI_CMT_03(cli_output):
    """
    KSI-CMT-03: Implement automated testing and validation of changes prior to deployment
    
    Updated to recognize Infrastructure as Code security scanning via Checkov
    instead of traditional CodeBuild/CodePipeline approaches.
    """
    evidence_dir = Path("evidence_v2/KSI-CMT-03")
    if not evidence_dir.exists():
        return False, "❌ Evidence directory evidence_v2/KSI-CMT-03/ not found"
    automated_testing_evidence = []
    testing_score = 0
    if (evidence_dir / "automated_testing_proof.json").exists():
        automated_testing_evidence.append("Infrastructure as Code security scanning")
        testing_score += 2  # High value - proves automated testing runs
        try:
            with open(evidence_dir / "automated_testing_proof.json", 'r') as f:
                proof_data = json.load(f)
                scan_tool = proof_data.get('scan_tool', 'Unknown')
                files_scanned = proof_data.get('files_scanned', 0)
    # ... (additional validation logic) ...
```

## 📜 Compliance Mapping

**Control Description:** Implement automated testing and validation of changes prior to deployment

**Implementation Justification:** Validates automated testing through CodeBuild, CodePipeline, and pre-deployment validation

**FedRAMP 20x Category:** Change Management

## 📊 Recent Validation Results

**Evidence Analysis:** ✅ All 2 commands executed successfully | ✅ Command output received | ✅ Command output received

**Commands Executed:** 2
**Validation Method:** validation-engine-sync

---
*Documentation auto-generated from KSI validation pipeline*
*Source: cli_command_register.json, unified_ksi_validations.json*