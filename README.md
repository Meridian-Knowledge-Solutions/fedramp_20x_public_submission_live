# FedRAMP 20x Public Trust Center – Meridian LMS

This repository is the **public-facing trust center** for Meridian LMS FedRAMP 20x Low authorization, providing real-time compliance visibility and transparency for federal agencies.

It demonstrates **automated validation**, **machine-readable evidence**, **enhanced SCN automation**, and **continuous compliance monitoring** aligned with GSA's FedRAMP 20x pilot goals.

---

## 🔗 Live Trust Center Dashboard

**🌐 [FedRAMP 20x Trust Center](https://meridian-knowledge-solutions.github.io/fedramp_20x_public_submission-live/)**

### 🚀 Three-Tier POA&M System
We implemented a proactive enhancement tracking beyond traditional compliance gaps:
- **🚨 Tier 1: Compliance POA&M** - Traditional remediation for failed validations (30 day SLA)
- **📈 Tier 2: Low Risk Findings** - Low risk findings in passing KSIs (90 day cycles)
- **🕒 Tier 3: Improvement Opportunities** - Proactive improvement opportunities (180-day cycles)

### 📋 Enhanced SCN Automation 
We've implemented **Enhanced FedRAMP 20x Combined Requirements** compliant SCN automation:
- **🔄 Automatic Classification** - All 5 SCN types with service impact analysis
- **🚨 Emergency Procedures** - FRR-SCN-EX-02 compliant emergency mode detection
- **🏗️ Infrastructure Intelligence** - Terraform repository monitoring with impact assessment
- **📧 Complete Notification** - All FRR-SCN-09 elements with 3PAO integration
- **📦 Evidence Packages** - Professional compliance documentation with audit trails

### 📊 Dual-Interface Design
- **🔍 Compliance Dashboard** - Real-time KSI monitoring and analysis
- **🛡️ RFC-0011 Trust Center** - Federal agency access portal
- **📋 SCN Transparency** - Public change notification tracking and evidence

### Real-time Features:
- ✅ **Live KSI Status**: Pass/fail for all Key Security Indicators with auto-refresh
- 🔍 **Advanced Filtering**: Search and filter by status, category, keyword, or enhancement opportunities
- 💻 **CLI Evidence**: View actual AWS CLI commands with execution details and timing
- 📋 **Detailed Reasoning**: Understand why each KSI passed/failed with assessment breakdown
- 📈 **Enhancement Detection**: Identification of improvement opportunities in passing KSIs
- 🐛 **GitHub Integration**: Report failed KSIs and create enhancement tracking issues
- 📊 **Compliance Metrics**: Real-time dashboard with trend tracking and 4-metric overview
- 🌙 **Modern Interface**: Light/dark mode with responsive design and keyboard shortcuts
- **📋 SCN Monitoring**: Live change notification status and automated compliance

### 🛡️ Federal Agency Portal (RFC-0011 Compliant)
- **🔧 API Access**: Machine-readable authorization data with structured endpoints
- **📋 Federal Access Request**: Official .gov/.mil workflow for authorization materials
- **🚨 Incident Reporting**: FedRAMP Category 1-5 classification templates
- **📞 Emergency Hotline**: 24/7 security incident response (1-hour SLA)
- **📋 SCN Transparency**: Public access to change notifications and evidence packages

### 🔄 Continuous Improvement Features
- **Proactive Enhancement Tracking**: Find improvements in compliant controls
- **Business Value Assessment**: ROI calculation for security enhancements  
- **Priority-Based Roadmaps**: High/Medium/Low improvement sequencing
- **Evidence Currency Management**: Automatic staleness detection and refresh cycles
- **Enhanced SCN Management**: Service impact vs operational change distinction

### 📱 Interactive Experience
- **Command Execution Analysis**: Full CLI logs with comprehensive command register
- **Why This Result**: Detailed assessment explanations with technical breakdown
- **Enhancement Planning**: Structured improvement workflows with templates
- **Export Capabilities**: JSON downloads, GitHub issue creation, incident templates
- **SCN Evidence Access**: Download complete compliance packages and email templates

---

## 📁 Repository Structure & Key Transparency Artifacts

### 🏗️ Organized Directory Structure
```
📁 Root (KSI Validation - existing structure preserved)
├── unified_ksi_validations.json     # Source of truth for all validations
├── results/                         # KSI validation result files  
├── docs/                           # Auto-generated KSI documentation
├── validation/                     # KSI validation engine results
├── directory_index.json            # Structure guide for integration
├── enhanced_scn_status.json        # SCN automation status
└── multi_account_status.json       # Multi-account validation status

📁 scn_automation/ (Enhanced SCN Management)
├── scn_classification.json         # Latest SCN classification results
├── scn_issues/                     # Public GitHub issues for transparency
└── external_repo_changes.json      # Terraform infrastructure monitoring

📁 compliance_evidence/ (Professional Evidence Packages)
├── enhanced_scn_compliance/        # Complete compliance evidence
├── package_metadata.json           # Evidence package metadata
└── README.md                       # Compliance package documentation

📁 audit_summaries/ (Audit & Compliance Tracking)
├── scn_classification.json         # SCN audit data
└── evidence_commit_metadata.json   # Evidence audit trails
```

### 🔍 Key Transparency Artifacts

| File                                | Purpose                                                  | Access |
|-------------------------------------|----------------------------------------------------------|--------|
| **KSI Validation (Root)**           |                                                          |        |
| `unified_ksi_validations.json`      | **Source of Truth**: All validation results with evidence | [📄 Download](https://meridian-knowledge-solutions.github.io/fedramp_20x_public_submission_live/unified_ksi_validations.json) |
| `failed_ksi_report_readable.md`     | **Remediation Guide**: Detailed analysis of failed KSIs | [📋 View Report](https://meridian-knowledge-solutions.github.io/fedramp_20x_public_submission_live/failed_ksi_report_readable.md) |
| `evidence_commit_metadata.json`     | **Audit Trail**: Git SHA + timestamps for all evidence | [🔍 Inspect](https://meridian-knowledge-solutions.github.io/fedramp_20x_public_submission_live/evidence_commit_metadata.json) |
| `docs/ksi_rules/`                   | **Rule Documentation**: Auto-generated KSI validation logic | [📚 Browse](https://github.com/Meridian-Knowledge-Solutions/fedramp_20x_public_submission_live/tree/main/docs/ksi_rules) |
| **Enhanced SCN Automation**         |                                                          |        |
| `scn_automation/scn_classification.json` | **SCN Status**: Latest change classification and analysis | [📋 View](https://meridian-knowledge-solutions.github.io/fedramp_20x_public_submission_live/scn_automation/scn_classification.json) |
| `scn_automation/scn_issues/`        | **Public Issues**: GitHub issues for change transparency | [🔍 Browse](https://github.com/Meridian-Knowledge-Solutions/fedramp_20x_public_submission_live/tree/main/scn_automation/scn_issues) |
| `scn_automation/external_repo_changes.json` | **Infrastructure**: Terraform monitoring and impact analysis | [🏗️ View](https://meridian-knowledge-solutions.github.io/fedramp_20x_public_submission_live/scn_automation/external_repo_changes.json) |
| **Compliance Evidence**             |                                                          |        |
| `compliance_evidence/`              | **Evidence Packages**: Complete FedRAMP compliance documentation | [📦 Browse](https://github.com/Meridian-Knowledge-Solutions/fedramp_20x_public_submission_live/tree/main/compliance_evidence) |
| `directory_index.json`              | **Structure Guide**: Complete repository organization reference | [📖 View](https://meridian-knowledge-solutions.github.io/fedramp_20x_public_submission_live/directory_index.json) |
| `enhanced_scn_status.json`          | **SCN Status**: Enhanced automation status and capabilities | [📊 View](https://meridian-knowledge-solutions.github.io/fedramp_20x_public_submission_live/enhanced_scn_status.json) |

---

## 🏗️ Architecture & Validation Flow

### Enhanced Automated Evidence Pipeline
```
Private Repository → CLI Commands → Evidence Collection → Assertion Logic → Public Dashboard
                  ↓
        Enhanced SCN Classification → Change Analysis → Evidence Packages → Public Transparency
```

### Daily Automation Process
1. **🔄 Evidence Collection**: GitHub Actions execute AWS CLI commands
2. **⚡ Validation Engine**: Python assertion logic evaluates compliance
3. **📊 Results Generation**: Consolidated JSON with detailed reasoning
4. **📋 Enhanced SCN Automation**: Change classification and notification generation
5. **🏗️ Infrastructure Monitoring**: Terraform repository impact analysis
6. **🌐 Dashboard Update**: Real-time sync to public trust center with organized structure
7. **📋 Report Generation**: Failed KSI analysis and remediation guidance
8. **📦 Evidence Packaging**: Professional compliance documentation with audit trails

### Validation Methodology
- **CLI-Based Evidence**: Technical controls verified via AWS API
- **Automated Assertions**: Machine-readable pass/fail logic
- **Enhanced SCN Classification**: Service impact vs operational change analysis
- **Continuous Monitoring**: Daily validation with trend tracking
- **Audit-Ready**: Complete trail from command to conclusion
- **Professional Packaging**: Evidence packages with metadata and documentation

---

## 🔍 For Federal Agencies & Auditors

### What You Can See
- **Real-time Compliance**: Current security posture across all KSIs
- **Evidence Transparency**: Actual CLI commands and raw outputs
- **Validation Logic**: How each security control is assessed
- **Trend Analysis**: Compliance improvement over time
- **Remediation Plans**: Detailed guidance for addressing failures
- **Change Transparency**: Complete SCN automation with public GitHub issues
- **Infrastructure Intelligence**: Terraform monitoring with service impact analysis
- **Evidence Packages**: Professional compliance documentation ready for audit

### Enhanced SCN Transparency
| SCN Information | Available Evidence |
|----------------|-------------------|
| **Change Classification** | `scn_automation/scn_classification.json` with enhanced FedRAMP 20x logic |
| **Public Issues** | GitHub issues in `scn_automation/scn_issues/` with complete transparency |
| **Infrastructure Impact** | `scn_automation/external_repo_changes.json` with Terraform analysis |
| **Evidence Packages** | `compliance_evidence/` with professional documentation |
| **Emergency Procedures** | FRR-SCN-EX-02 compliant emergency mode detection and handling |

### Audit Trail Components
| Audit Question | Available Evidence |
|----------------|-------------------|
| **What was tested?** | CLI commands visible in dashboard + JSON |
| **How was it validated?** | Assertion logic in source repository |
| **When was it tested?** | Timestamps in all evidence files |
| **What were the results?** | Real-time dashboard + downloadable reports |
| **Can it be reproduced?** | Complete automation via GitHub Actions |
| **What changes occurred?** | Enhanced SCN classification with service impact analysis |
| **How were stakeholders notified?** | Public GitHub issues + email templates in evidence packages |
| **What was the compliance impact?** | Infrastructure monitoring with transformative vs operational distinction |

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

## 📋 Sample Enhanced SCN Classification

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

---

## 🛡️ Trust Center Features

### 📋 Available Materials

**🔒 Public Access:**
- Real-time compliance dashboard
- KSI validation methodology  
- Service architecture overview
- Continuous monitoring reports
- Enhanced SCN automation transparency
- Infrastructure change monitoring
- Professional evidence packages

**🔐 Federal Agency Access:**
- Complete authorization package
- Detailed security plans
- 3PAO assessment reports
- Continuous monitoring data
- Complete SCN evidence packages
- Enhanced compliance documentation

### 📞 CSP Contact Information
- **Primary Contact**: Meridian Federal Cloud Operations 
- **Email**: [security@meridianks.com](mailto:security@meridianks.com)
- **Phone**: +1 (571) 665-5287 
- **Support**: 24/7 for critical security issues
- **SCN Coordinator**: Enhanced SCN automation with GitHub issue tracking

---

## 🎯 Enhanced FedRAMP 20x Pilot Goals

This implementation demonstrates:
- ✅ **Machine-readable compliance data** for automated assessment
- ✅ **Real-time transparency** for federal agency trust
- ✅ **Reproducible validation** through automated pipelines
- ✅ **Continuous monitoring** with immediate visibility
- ✅ **Audit-ready documentation** with complete traceability
- ✅ **Open source methodology** for community advancement
- ✅ **Enhanced SCN automation** with FedRAMP 20x Combined Requirements compliance
- ✅ **Service impact analysis** distinguishing customer vs operational changes
- ✅ **Emergency procedures** with FRR-SCN-EX-02 compliant handling
- ✅ **Professional evidence packaging** ready for 3PAO and agency review
- ✅ **Infrastructure intelligence** with Terraform monitoring and impact assessment

---

## 🚀 Service Information

- **Service**: Meridian LMS
- **Authorization Level**: FedRAMP 20x Low
- **Hosting Environment**: AWS Commercial (US-East)
- **Assessment Method**: Machine-readable validation with automated KSI assessment
- **SCN Management**: Enhanced FedRAMP 20x Combined Requirements compliant automation
- **Change Classification**: All 5 SCN types with service impact analysis
- **Emergency Procedures**: FRR-SCN-EX-02 compliant with retroactive notification capability

---

## 📈 Compliance Commitment

We are committed to achieving and maintaining **FedRAMP 20x Low authorization** through:
- Daily automated validation
- Continuous security monitoring  
- Proactive remediation of failed KSIs
- Transparent reporting to federal stakeholders
- Enhanced SCN automation with zero false positives
- Service impact-based change classification
- Professional evidence packaging for audit readiness
- Real-time infrastructure monitoring with public transparency

---

## 📬 Community & Feedback

This repository supports GSA's FedRAMP 20x pilot goals of:
- **Community-driven trust models**
- **Transparent, machine-verifiable compliance**
- **Practical automation for real-world authorization**
- **Enhanced change management** with service impact analysis
- **Professional evidence packaging** for streamlined audit processes

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
- Enhanced SCN Requirements: FRR-SCN-01, FRR-SCN-03, FRR-SCN-04, FRR-SCN-07, FRR-SCN-08, FRR-SCN-09
- Emergency Procedures: FRR-SCN-EX-02 compliant emergency mode
- Impact Categorization: FRR-SCN-IM-01 detection and routing

---

