# FedRAMP 20x Public Trust Center – Meridian LMS

This repository is the **public-facing trust center** for Meridian LMS FedRAMP 20x Low authorization, providing real-time compliance visibility and transparency for federal agencies.

It demonstrates **automated validation**, **machine-readable evidence**, **SCN automation**, **continuous compliance monitoring**, and **Phase 2 Moderate readiness** aligned with GSA's FedRAMP 20x pilot goals.

---

## 🌐 Live Trust Center Dashboard

**🌐 [FedRAMP 20x Trust Center](https://meridian-knowledge-solutions.github.io/fedramp_20x_public_submission_live/)**

### 🚀 Three-Tier POA&M System
We implemented a proactive enhancement tracking beyond traditional compliance gaps:
- **🚨 Tier 1: Compliance POA&M** - Traditional remediation for failed validations (30 day SLA)
- **📈 Tier 2: Low Risk Findings** - Low risk findings in passing KSIs (90 day cycles)
- **🕒 Tier 3: Improvement Opportunities** - Proactive improvement opportunities (180-day cycles)

### 🔄 SCN Automation 
Simplified change notification tracking with public transparency:
- **🔄 Automatic Classification** - All 5 SCN types with service impact analysis
- **🚨 Emergency Procedures** - Emergency mode detection and handling
- **📋 Audit Transparency** - Public access to change summaries and classification

### 📊 Dual-Interface Design
- **🔍 Compliance Dashboard** - Real-time KSI monitoring and analysis
- **🛡️ RFC-0011 Trust Center** - Federal agency access portal
- **📋 SCN Transparency** - Change notification tracking and evidence

### Real-time Features:
- ✅ **Live KSI Status**: Pass/fail for all Key Security Indicators with auto-refresh
- 🔍 **Advanced Filtering**: Search and filter by status, category, keyword, or enhancement opportunities
- 💻 **CLI Evidence**: View actual AWS CLI commands with execution details and timing
- 📋 **Detailed Reasoning**: Understand why each KSI passed/failed with assessment breakdown
- 📈 **Enhancement Detection**: Identification of improvement opportunities in passing KSIs
- 🛠 **GitHub Integration**: Report failed KSIs and create enhancement tracking issues
- 📊 **Compliance Metrics**: Real-time dashboard with trend tracking and 4-metric overview
- 🌙 **Modern Interface**: Light/dark mode with responsive design and keyboard shortcuts
- **📋 SCN Monitoring**: Live change notification status and automated compliance

### 🛡️ Federal Agency Portal (RFC-0011 Compliant)
- **🔧 API Access**: Machine-readable authorization data with structured endpoints
- **📋 Federal Access Request**: Official .gov/.mil workflow for authorization materials
- **🚨 Incident Reporting**: FedRAMP Category 1-5 classification templates
- **📞 Emergency Hotline**: 24/7 security incident response (1-hour SLA)
- **📋 SCN Transparency**: Public access to change notifications and evidence summaries

---

## 🔧 Technical Implementation Architecture

### **Validation Engine Components**
```
📁 Root Repository Structure
├── cli_command_register.json         # 60+ KSI definitions with validation logic
├── validation_engine.py              # Multi-command assertion processing engine
├── cli_assertion_rules_full.py       # 60+ rule functions with pass/fail logic
├── unified_ksi_validations.json      # Source of truth for all validation results
├── run_all_cli_commands.py          # CLI evidence collection orchestrator
├── generate_unified_validations.py   # Results consolidation and publishing
├── evidence_v2/                      # Structured evidence repository (private)
│   ├── KSI-{CATEGORY}-{ID}/          # Individual KSI evidence containers
│   │   ├── cli_output.json           # Raw CLI command outputs
│   │   └── *.pdf, *.png, *.xlsx      # Manual evidence documents
├── results/                          # Public validation results
│   ├── continuous_ksi_results.json   # Trend analysis and metadata
│   └── evidence_commit_metadata.json # Git audit trail timestamps
├── docs/ksi_rules/                   # Auto-generated rule documentation
│   └── KSI-{CATEGORY}-{ID}.md        # Individual KSI rule explanations
├── validation/                       # Validation engine intermediate files
├── phase2_compliance/                # Phase 2 Moderate readiness artifacts
│   ├── 3pao_audit_report.json        # Technical validation for 3PAO assessment
│   ├── validation_consistency_log.json # Automation consistency tracking
│   ├── technical_validation_log.json # Technical correctness verification
│   └── fingerprint_cache.json       # Evidence integrity verification
└── audit_summaries/                  # SCN and change tracking (public-safe)
    ├── external_repo_changes_public.json # Infrastructure change summaries
    └── scn_classification.json       # Change notification classification
```

### **Quality Assurance Pipeline**
- **Master Validator**: Consistency checking and technical validation for 3PAO assessment
- **Fingerprint Validation**: Evidence integrity verification using SHA-256 hashing
- **Multi-account Support**: Management account validation for enterprise controls
- **Automation Reliability**: Zero false positive validation with comprehensive error handling
- **Technical Correctness**: Automated verification of CLI command execution and assertion logic

### **Detailed Validation Flow**
```
Evidence Collection → CLI Execution → Assertion Processing → Validation Engine → Master Validator → Public Dashboard
         ↓              ↓               ↓                    ↓                ↓               ↓
   evidence_v2/    cli_command_    cli_assertion_    validation_engine.py  consistency_   Trust Center
   [KSI-ID]/       register.json    rules_full.py                         validation      Dashboard
         ↓              ↓               ↓                    ↓                ↓               ↓
   Raw Evidence    60+ KSI Defs    60+ Rule Funcs    Multi-cmd Engine    3PAO Ready      Live Status
   CLI + Manual    AWS Commands    Pass/Fail Logic   Result Synthesis    Audit Reports   Real-time
```

---

## 📋 Evidence Traceability Matrix

### **KSI-to-Evidence Mapping**
Each KSI validation includes complete traceability:
- **CLI Commands**: Automated evidence collection via AWS APIs (githubactions_role)
- **Manual Evidence**: Policy documents, procedures, and organizational artifacts stored in `evidence_v2/`
- **Validation Results**: Machine-readable pass/fail with detailed reasoning in `unified_ksi_validations.json`
- **Evidence Paths**: Direct links to supporting evidence files with git commit tracking
- **Assertion Logic**: Documented rule functions in `cli_assertion_rules_full.py`
- **Rule Documentation**: Auto-generated explanations in `docs/ksi_rules/`

### **Audit Trail Components**
| Component | Location | Purpose | Audit Value |
|-----------|----------|---------|------------|
| `unified_ksi_validations.json` | Root | Source of truth for all KSI results | Primary compliance evidence |
| `evidence_v2/{KSI-ID}/` | Private repo | Raw evidence and CLI outputs | Detailed technical validation |
| `docs/ksi_rules/` | Public | Auto-generated rule documentation | Methodology transparency |
| `results/continuous_ksi_results.json` | Public | Trend analysis and metadata | Historical compliance tracking |
| `results/evidence_commit_metadata.json` | Public | Git SHA + timestamps for all evidence | Tamper-evident audit trail |
| `phase2_compliance/3pao_audit_report.json` | Private | Technical validation summary | 3PAO assessment readiness |
| `validation_consistency_log.json` | Private | Automation consistency tracking | Quality assurance verification |
| `failed_ksi_report_readable.md` | Public | Detailed analysis of failed KSIs | Remediation guidance |

### **Evidence Currency Tracking**
- **Real-time Updates**: Daily GitHub Actions execution with timestamped results
- **Git Audit Trail**: Complete SHA tracking for all evidence files and validation results
- **Automated Timestamps**: ISO 8601 timestamps for every validation cycle
- **Evidence Integrity**: SHA-256 fingerprinting for tamper detection
- **Version Control**: Full git history for all evidence and validation changes

---

## 🎯 Phase 2 Moderate Readiness

### **Enhanced Capabilities for Moderate Assessment**
- **✅ Consistency Validation**: Master validator ensures automation reliability across 60+ KSIs
- **✅ Technical Validation**: 3PAO-ready audit reports and comprehensive validation logs
- **✅ Evidence Maturity**: Complete evidence collection across all KSI categories with manual + automated validation
- **✅ Compliance Tracking**: Dedicated Phase 2 compliance files in `phase2_compliance/` directory
- **✅ Multi-Account Architecture**: Enterprise-grade validation across management and member accounts
- **✅ Advanced Automation**: 60+ rule functions with sophisticated assertion logic and error handling
- **✅ Audit Trail Integrity**: Tamper-evident evidence tracking with cryptographic verification

### **3PAO Integration Points**
- **Audit Reports**: `3pao_audit_report.json` with comprehensive technical validation results
- **Consistency Logs**: `validation_consistency_log.json` for automation verification and quality assurance
- **Evidence Packages**: Complete evidence trails for independent verification and sampling
- **Technical Documentation**: Auto-generated rule documentation for methodology review
- **Quality Metrics**: Automated tracking of validation consistency and technical correctness
- **Compliance History**: Full historical tracking of all KSI validation results and trends

### **Advanced Technical Features**
- **Zero False Positives**: Sophisticated validation logic eliminates compliance measurement errors
- **Service Impact Analysis**: Distinguishes customer-facing vs operational changes for accurate SCN classification
- **Emergency Procedures**: FRR-SCN-EX-02 compliant emergency mode detection and handling
- **Multi-Command Validation**: Complex KSIs validated through multiple AWS CLI commands with consolidated results
- **Evidence Correlation**: Automated correlation between CLI outputs and manual evidence documents
- **Continuous Monitoring**: Real-time compliance posture with immediate deviation detection

---

## 🗃️ Repository Structure & Key Transparency Artifacts

### 🗃️ Organized Directory Structure
```
📁 Root (KSI Validation - existing structure preserved)
├── unified_ksi_validations.json     # Source of truth for all validations
├── results/                         # KSI validation result files  
├── docs/                           # Auto-generated KSI documentation
├── validation/                     # KSI validation engine results
├── directory_index.json            # Structure guide for integration
├── multi_account_status.json       # Multi-account validation status
└── phase2_compliance/               # Phase 2 Moderate readiness artifacts

📁 audit_summaries/ (SCN & Change Tracking)
├── external_repo_changes_public.json  # Public infrastructure change summary
└── scn_classification.json            # SCN classification and analysis
```

### 📁 Key Transparency Artifacts

| File                                | Purpose                                                  | Access |
|-------------------------------------|----------------------------------------------------------|--------|
| **KSI Validation (Root)**           |                                                          |        |
| `unified_ksi_validations.json`      | **Source of Truth**: All validation results with evidence | [📄 Download](https://meridian-knowledge-solutions.github.io/fedramp_20x_public_submission_live/unified_ksi_validations.json) |
| `failed_ksi_report_readable.md`     | **Remediation Guide**: Detailed analysis of failed KSIs | [📋 View Report](https://meridian-knowledge-solutions.github.io/fedramp_20x_public_submission_live/failed_ksi_report_readable.md) |
| `evidence_commit_metadata.json`     | **Audit Trail**: Git SHA + timestamps for all evidence | [🔍 Inspect](https://meridian-knowledge-solutions.github.io/fedramp_20x_public_submission_live/evidence_commit_metadata.json) |
| `docs/ksi_rules/`                   | **Rule Documentation**: Auto-generated KSI validation logic | [📚 Browse](https://github.com/Meridian-Knowledge-Solutions/fedramp_20x_public_submission_live/tree/main/docs/ksi_rules) |
| **SCN & Change Tracking**          |                                                          |        |
| `audit_summaries/external_repo_changes_public.json` | **Infrastructure Changes**: Public summary of external repository changes | [🗃️ View](https://meridian-knowledge-solutions.github.io/fedramp_20x_public_submission_live/audit_summaries/external_repo_changes_public.json) |
| `audit_summaries/scn_classification.json` | **SCN Classification**: Change notification classification and analysis | [📋 View](https://meridian-knowledge-solutions.github.io/fedramp_20x_public_submission_live/audit_summaries/scn_classification.json) |
| `directory_index.json`              | **Structure Guide**: Complete repository organization reference | [📖 View](https://meridian-knowledge-solutions.github.io/fedramp_20x_public_submission_live/directory_index.json) |
| **Phase 2 Compliance**             |                                                          |        |
| `phase2_compliance/3pao_audit_report.json` | **3PAO Readiness**: Technical validation summary for assessors | Private Repository |
| `phase2_compliance/validation_consistency_log.json` | **Quality Assurance**: Automation consistency tracking | Private Repository |
| `phase2_compliance/technical_validation_log.json` | **Technical Verification**: Technical correctness validation | Private Repository |

---

## 🗃️ Architecture & Validation Flow

### Automated Evidence Pipeline
```
Private Repository → CLI Commands → Evidence Collection → Assertion Logic → Master Validator → Public Dashboard
                  ↓
        SCN Classification → Change Analysis → Public Summaries → Audit Transparency → Phase 2 Compliance
```

### Daily Automation Process
1. **📄 Evidence Collection**: GitHub Actions execute AWS CLI commands via OIDC role assumption
2. **⚡ Validation Engine**: Python assertion logic evaluates compliance across 60+ KSIs
3. **📊 Results Generation**: Consolidated JSON with detailed reasoning and evidence paths
4. **📋 SCN Classification**: Change classification and notification generation with service impact analysis
5. **🗃️ Audit Summary**: Generate public-safe summaries in audit_summaries/ directory
6. **🌐 Dashboard Update**: Real-time sync to public trust center with live status updates
7. **📋 Report Generation**: Failed KSI analysis and remediation guidance
8. **🎯 Phase 2 Validation**: Master validator runs consistency and technical correctness checks
9. **🔍 Quality Assurance**: Evidence integrity verification and audit trail generation

### Validation Methodology
- **CLI-Based Evidence**: Technical controls verified via AWS API with role-based access
- **Automated Assertions**: Machine-readable pass/fail logic with sophisticated rule functions
- **SCN Classification**: Service impact vs operational change analysis with FRA-SCN-03 compliance
- **Continuous Monitoring**: Daily validation with trend tracking and deviation detection
- **Audit-Ready**: Complete trail from command to conclusion with cryptographic integrity
- **Public Transparency**: Sanitized summaries for public audit access while protecting sensitive evidence
- **Quality Validation**: Master validator ensures automation consistency for 3PAO assessment
- **Multi-Account Support**: Enterprise validation across management and member AWS accounts

---

## 📁 For Federal Agencies & Auditors

### What You Can See
- **Real-time Compliance**: Current security posture across all 60+ KSIs with live dashboard
- **Evidence Transparency**: Actual CLI commands and raw outputs with execution metadata
- **Validation Logic**: Complete methodology documentation for each security control assessment
- **Trend Analysis**: Compliance improvement over time with historical tracking
- **Remediation Plans**: Detailed guidance for addressing failures with actionable recommendations
- **Change Transparency**: SCN automation with public summaries and service impact analysis
- **Infrastructure Intelligence**: Public summaries of infrastructure changes with security context
- **Audit Summaries**: Public-safe evidence summaries ready for 3PAO and agency review
- **Technical Validation**: Phase 2 readiness indicators and quality assurance metrics

### SCN Transparency
| SCN Information | Available Evidence | Compliance Standard |
|----------------|-------------------|-------------------|
| **Change Classification** | `audit_summaries/scn_classification.json` with FedRAMP 20x compliant logic | FRA-SCN-03, FRR-SCN-03 |
| **Infrastructure Changes** | `audit_summaries/external_repo_changes_public.json` with public-safe summaries | FRR-SCN-01, FRR-SCN-04 |
| **Emergency Procedures** | Emergency mode detection and handling in classification | FRR-SCN-EX-02 |
| **Service Impact Analysis** | Customer vs operational change distinction | FRR-SCN-IM-01 |
| **Timeline Management** | Automatic deadline calculation and tracking | FRR-SCN-07, FRR-SCN-08 |

### Audit Trail Components
| Audit Question | Available Evidence | File Location |
|----------------|-------------------|---------------|
| **What was tested?** | CLI commands visible in dashboard + JSON | `unified_ksi_validations.json` |
| **How was it validated?** | Assertion logic and rule documentation | `cli_assertion_rules_full.py`, `docs/ksi_rules/` |
| **When was it tested?** | Timestamps in all evidence files | `results/evidence_commit_metadata.json` |
| **What were the results?** | Real-time dashboard + downloadable reports | Live dashboard + `failed_ksi_report_readable.md` |
| **Can it be reproduced?** | Complete automation via GitHub Actions | `.github/workflows/` |
| **What changes occurred?** | SCN classification with service impact analysis | `audit_summaries/scn_classification.json` |
| **How were changes tracked?** | Public summaries with audit transparency | `audit_summaries/external_repo_changes_public.json` |
| **What was the compliance impact?** | Infrastructure monitoring with change classification | SCN automation results |
| **Is the automation reliable?** | Master validator consistency tracking | `phase2_compliance/validation_consistency_log.json` |
| **Are the technical controls valid?** | Technical validation and correctness verification | `phase2_compliance/technical_validation_log.json` |

---

## ✅ Sample KSI Validation

```json
{
  "ksi_id": "KSI-CED-01",
  "validation_id": "KSI-CED-01",
  "assertion": true,
  "assertion_reason": "✅ Security awareness training evidence: cyber_security_training.png, security_training_roster.png, fedramp_role_based.png",
  "cli_command": "1 commands (1 successful): evidence_check",
  "cli_output_digest": "",
  "cli_output_interpretation": "✅ All 1 commands executed successfully | 📄 Manual evidence validation",
  "timestamp": "2025-06-06T11:48:54.165169",
  "validation_method": "validation-engine-sync",
  "commands_executed": 1,
  "successful_commands": 1,
  "failed_commands": 0,
  "original_timestamp": "2025-06-06T11:48:53.771623",
  "synced_from_validation_engine": true,
  "requirement": "A secure cloud service provider will continuously educate their employees on cybersecurity measures, testing them regularly to ensure their knowledge is satisfactory.",
  "long_name": "Cybersecurity Education",
  "category_prefix": "KSI-CED",
  "total_category_controls": 2,
  "evidence_path": "evidence_v2/KSI-CED-01/cli_output.json"
}
```

## 📋 Sample SCN Classification

```json
{
  "scn_type": "adaptive",
  "requires_notification": true,
  "change_id": "SCN-20250720-001",
  "emergency_mode": false,
  "service_impact_analysis": {
    "customer_facing": false,
    "operational_improvement": true,
    "infrastructure_changes": ["security_groups", "monitoring"]
  },
  "compliance_status": {
    "FRR-SCN-03": "enhanced_classification_complete",
    "FRA-SCN-03": "decision_tree_followed",
    "FRR-SCN-09": "all_elements_included"
  },
  "notification_timeline": {
    "type": "post_completion",
    "business_days": 10,
    "due_date": "2025-08-03"
  }
}
```

## 📋 Sample Infrastructure Changes (Public)

```json
{
  "terraform_changes_detected": true,
  "scn_classification": "adaptive",
  "fedramp_20x_compliant": true,
  "monitoring_metadata": {
    "analysis_timestamp": "2025-09-08T10:30:00Z",
    "monitor_version": "3.0.0-simplified",
    "output_classification": "public-minimal",
    "sanitization_applied": true,
    "data_protection_notice": "Operational details excluded for security"
  }
}
```

---

## 🛡️ Trust Center Features

### 📋 Available Materials

**📓 Public Access:**
- Real-time compliance dashboard with live KSI status
- KSI validation methodology with complete rule documentation
- Service architecture overview with security design principles
- Continuous monitoring reports with trend analysis
- SCN automation transparency with change classification
- Infrastructure change summaries with security context
- Public audit summaries ready for agency review
- Phase 2 readiness indicators and quality metrics

**🔐 Federal Agency Access:**
- Complete authorization package with technical documentation
- Detailed security plans and implementation guides
- 3PAO assessment reports and validation results
- Continuous monitoring data with raw evidence
- Complete SCN evidence packages with detailed analysis
- Enhanced compliance documentation for audit support
- Phase 2 compliance artifacts for Moderate assessment
- Technical validation logs and consistency tracking

### 📞 CSP Contact Information
- **Primary Contact**: Meridian Federal Cloud Operations 
- **Email**: [security@meridianks.com](mailto:security@meridianks.com)
- **Phone**: +1 (571) 665-5287 
- **Support**: 24/7 for critical security issues
- **SCN Coordinator**: Automated SCN tracking with public summaries
- **3PAO Support**: Technical validation assistance for assessment activities

---

## 🎯 FedRAMP 20x Pilot Goals

This implementation demonstrates:
- ✅ **Machine-readable compliance data** for automated assessment with 60+ KSI validation
- ✅ **Real-time transparency** for federal agency trust with live dashboard
- ✅ **Reproducible validation** through automated pipelines with complete audit trails
- ✅ **Continuous monitoring** with immediate visibility and deviation detection
- ✅ **Audit-ready documentation** with complete traceability and evidence integrity
- ✅ **Open source methodology** for community advancement and peer review
- ✅ **SCN automation** with FedRAMP 20x compliant classification and service impact analysis
- ✅ **Service impact analysis** distinguishing customer vs operational changes
- ✅ **Emergency procedures** with compliant handling and timeline management
- ✅ **Public audit summaries** ready for agency and 3PAO review
- ✅ **Infrastructure intelligence** with public-safe change tracking and security context
- ✅ **Phase 2 readiness** with technical validation and quality assurance for Moderate assessment
- ✅ **Advanced automation** with zero false positives and sophisticated validation logic
- ✅ **Multi-account architecture** supporting enterprise-grade validation and governance

---

## 🚀 Service Information

- **Service**: Meridian LMS
- **Authorization Level**: FedRAMP 20x Low (Phase 2 Moderate Ready)
- **Hosting Environment**: AWS Commercial (US-East)
- **Assessment Method**: Machine-readable validation with automated KSI assessment + manual evidence
- **SCN Management**: FedRAMP 20x compliant automation with public transparency
- **Change Classification**: All 5 SCN types with service impact analysis and emergency procedures
- **Emergency Procedures**: Compliant emergency mode detection with public summaries
- **Quality Assurance**: Master validator for automation consistency and technical correctness
- **Evidence Management**: Structured evidence repository with integrity verification
- **Multi-Account Support**: Enterprise validation across management and member accounts

---

## 📈 Compliance Commitment

We are committed to achieving and maintaining **FedRAMP 20x Low authorization** and **Phase 2 Moderate readiness** through:
- Daily automated validation across 60+ Key Security Indicators
- Continuous security monitoring with real-time deviation detection
- Proactive remediation of failed KSIs with detailed guidance
- Transparent reporting to federal stakeholders with live dashboard access
- SCN automation with public transparency and service impact analysis
- Service impact-based change classification with zero false positives
- Public audit summaries for streamlined 3PAO and agency review processes
- Real-time infrastructure monitoring with public access to security-relevant changes
- Technical validation and quality assurance for 3PAO assessment confidence
- Advanced automation reliability with consistency tracking and error detection
- Complete evidence traceability with cryptographic integrity verification

---

## 🔬 Community & Feedback

This repository supports GSA's FedRAMP 20x pilot goals of:
- **Community-driven trust models** with open methodology and peer review
- **Transparent, machine-verifiable compliance** with real-time validation
- **Practical automation for real-world authorization** with sophisticated technical implementation
- **Simplified change management** with public audit transparency and service impact analysis
- **Streamlined evidence access** for efficient 3PAO and agency audit processes
- **Quality assurance innovation** with automated consistency validation for assessment reliability
- **Technical excellence** with advanced validation logic and zero false positive measurement

**Questions?** [Open a GitHub Issue](https://github.com/Meridian-Knowledge-Solutions/fedramp_20x_public_submission_live/issues) or email [security@meridianks.com](mailto:security@meridianks.com)

---

## 📄 Compliance Standards

**Compliant with:**
- RFC-0008 (Continuous Reporting)
- RFC-0011 (Trust Center Requirements)
- FedRAMP 20x Low Authorization Requirements
- FedRAMP Minimum Assessment Standard
- FedRAMP 20x Low Definitions and Rules
- FedRAMP 20x Combined Requirements Release 25.06A
- SCN Requirements: FRR-SCN-01, FRR-SCN-03, FRR-SCN-04, FRR-SCN-07, FRR-SCN-08, FRR-SCN-09
- Emergency Procedures: FRR-SCN-EX-02 compliant emergency mode
- Impact Categorization: FRR-SCN-IM-01 detection and routing
- Quality Assurance: Phase 2 Moderate technical validation standards
- Evidence Management: Cryptographic integrity verification and audit trail requirements

---
