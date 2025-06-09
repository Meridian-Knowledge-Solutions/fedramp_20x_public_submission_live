# KSI-CMT-03: Implement automated testing and validation of changes prior to deployment

*Generated on 2025-06-09 08:28:57 UTC*

## 📖 Overview

**KSI ID:** `KSI-CMT-03`
**Description:** Implement automated testing and validation of changes prior to deployment
**Justification:** Validates automated testing through Infrastructure as Code security scanning with Checkov, SARIF reports, and pre-deployment validation via external automation
**Last Validation:** ✅ 2025-06-09T08:28:57.293571
**Result:** ✅ Comprehensive automated testing via Infrastructure as Code: Infrastructure as Code security scanning; SARIF security reports generated; Checkov compliance validation

## 🛠️ Implementation

### Commands Executed
1. **Command:** `evidence_check`
   **Purpose:** Check evidence_v2/KSI-CMT-03/ for automated_testing_proof.json, sarif_metadata.json, and checkov_scan_summary.json from Infrastructure as Code security automation

## 📋 Evidence Requirements

### 📄 Manual Evidence
- Check evidence_v2/KSI-CMT-03/ for automated_testing_proof.json, sarif_metadata.json, and checkov_scan_summary.json from Infrastructure as Code security automation

## 🧠 Validation Logic

**Function:** `evaluate_KSI_CMT_03`

**Documentation:** KSI-CMT-03: Implement automated testing and validation of changes prior to deployment

Uses Infrastructure as Code security scanning evidence from external automation
instead of traditional CodeBuild/CodePipeline approaches.

### Rule Implementation
```python
def evaluate_KSI_CMT_03(cli_output):
    """
    KSI-CMT-03: Implement automated testing and validation of changes prior to deployment
    
    Uses Infrastructure as Code security scanning evidence from external automation
    instead of traditional CodeBuild/CodePipeline approaches.
    """
    evidence_dir = Path("evidence_v2/KSI-CMT-03")
    if not evidence_dir.exists():
        return False, "❌ Evidence directory evidence_v2/KSI-CMT-03/ not found"
    automated_testing_evidence = []
    testing_score = 0
    if (evidence_dir / "automated_testing_proof.json").exists():
        automated_testing_evidence.append("Infrastructure as Code security scanning")
        testing_score += 2
        try:
            with open(evidence_dir / "automated_testing_proof.json", 'r') as f:
                proof_data = json.load(f)
                scan_tool = proof_data.get('scan_tool', 'Unknown')
                files_scanned = proof_data.get('files_scanned', 0)
    # ... (additional validation logic) ...
```

## 📜 Compliance Mapping

**Control Description:** Implement automated testing and validation of changes prior to deployment

**Implementation Justification:** Validates automated testing through Infrastructure as Code security scanning with Checkov, SARIF reports, and pre-deployment validation via external automation

**FedRAMP 20x Category:** Change Management

## 📊 Recent Validation Results

**Evidence Analysis:** ✅ All 1 commands executed successfully | 📄 Manual evidence validation

**Commands Executed:** 1
**Validation Method:** validation-engine-sync

---
*Documentation auto-generated from KSI validation pipeline*
*Source: cli_command_register.json, unified_ksi_validations.json*