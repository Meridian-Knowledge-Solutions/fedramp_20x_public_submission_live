# KSI-PIY-04: Build security considerations into SDLC and align with CISA Secure By Design principles

<<<<<<< Updated upstream
<<<<<<< Updated upstream
<<<<<<< Updated upstream
<<<<<<< Updated upstream
*Generated on 2025-06-10 13:17:42 UTC*
=======
*Generated on 2025-06-10 13:18:11 UTC*
>>>>>>> Stashed changes
=======
*Generated on 2025-06-10 13:18:23 UTC*
>>>>>>> Stashed changes
=======
*Generated on 2025-06-10 13:18:26 UTC*
>>>>>>> Stashed changes
=======
*Generated on 2025-06-10 13:18:59 UTC*
>>>>>>> Stashed changes

## 📖 Overview

**KSI ID:** `KSI-PIY-04`
**Description:** Build security considerations into SDLC and align with CISA Secure By Design principles
**Justification:** Validates secure development through CodeCommit, CodeBuild security scanning, and SDLC documentation
<<<<<<< Updated upstream
<<<<<<< Updated upstream
<<<<<<< Updated upstream
<<<<<<< Updated upstream
**Last Validation:** ✅ 2025-06-10T13:17:42.456817
=======
**Last Validation:** ✅ 2025-06-10T13:18:11.049131
>>>>>>> Stashed changes
=======
**Last Validation:** ✅ 2025-06-10T13:18:23.546506
>>>>>>> Stashed changes
=======
**Last Validation:** ✅ 2025-06-10T13:18:26.136781
>>>>>>> Stashed changes
=======
**Last Validation:** ✅ 2025-06-10T13:18:58.721881
>>>>>>> Stashed changes
**Result:** ⚠️ Basic secure development practices (expand documentation): ℹ️ No CodeCommit repositories (may use external source control); ✅ Secure SDLC documentation: Secure Software Development Lifecycle (SDLC) Policy.pdf

## 🛠️ Implementation

### Commands Executed
1. **Command:** `aws codecommit list-repositories --output json`
   **Purpose:** Check code repositories for secure development practices

2. **Command:** `evidence_check`
   **Purpose:** Check evidence_v2/KSI-PIY-04/ for secure_sdlc_procedures.pdf and cisa_secure_by_design_alignment.pdf

## 📋 Evidence Requirements

### 🖥️ CLI Validation
- **Command:** `aws codecommit list-repositories --output json`
  - **Purpose:** Check code repositories for secure development practices

### 📄 Manual Evidence
- Check evidence_v2/KSI-PIY-04/ for secure_sdlc_procedures.pdf and cisa_secure_by_design_alignment.pdf

## 🧠 Validation Logic

**Function:** `evaluate_KSI_PIY_04`

**Documentation:** KSI-PIY-04: Build security considerations into the Software Development Lifecycle 
and align with CISA Secure By Design principles

Expected: Code Repositories + SDLC Documentation

### Rule Implementation
```python
def evaluate_KSI_PIY_04(cli_output):
    """
    KSI-PIY-04: Build security considerations into the Software Development Lifecycle 
    and align with CISA Secure By Design principles
    
    Expected: Code Repositories + SDLC Documentation
    """
    evidence_dir = Path("evidence_v2/KSI-PIY-04")
    code_repos = None
    if "commands" in cli_output:
        for cmd in cli_output["commands"]:
            cli_command = cmd.get("cli_command", "")
            raw_output = cmd.get("raw_output", {})
            if "list-repositories" in cli_command:
                code_repos = raw_output.get("repositories", [])
    manual_evidence = []
    if evidence_dir.exists():
        sdlc_files = [
            "Secure Software Development Lifecycle (SDLC) Policy.pdf"
        ]
    # ... (additional validation logic) ...
```

## 📜 Compliance Mapping

**Control Description:** Build security considerations into SDLC and align with CISA Secure By Design principles

**Implementation Justification:** Validates secure development through CodeCommit, CodeBuild security scanning, and SDLC documentation

**FedRAMP 20x Category:** Policy and Inventory

## 📊 Recent Validation Results

**Evidence Analysis:** ❌ All 2 commands failed execution | ⚠️ No usable output

**Commands Executed:** 2
**Validation Method:** validation-engine-sync

---
*Documentation auto-generated from KSI validation pipeline*
*Source: cli_command_register.json, unified_ksi_validations.json*