# FedRAMP 20x Public Trust Center – Meridian LMS

This repository is the **public-facing trust center** for Meridian Knowledge Solutions' FedRAMP 20x Low authorization, providing real-time compliance visibility and transparency for federal agencies.

It demonstrates **automated validation**, **machine-readable evidence**, and **continuous compliance monitoring** aligned with GSA's FedRAMP 20x pilot goals.

---

## 🔗 Live Trust Center Dashboard

**🌐 [FedRAMP 20x Trust Center](https://meridian-knowledge-solutions.github.io/fedramp_20x_public_submission_live/)**

### 🚀 New Three-Tier POA&M System
We implemented a proactive enhancement tracking beyond traditional compliance gaps:
- **🚨 Tier 1: Compliance POA&M** - Traditional remediation for failed validations (30 day SLA)
- **📈 Tier 2: Low Risk Findings** - Low risk findings in passing KSIs (90 day cycles)
- **🕒 Tier 3: Improvement Opportunities** - Proactive improvement opportunities (180-day cycles)

### 📊 Dual-Interface Design
- **🔍 Compliance Dashboard** - Real-time KSI monitoring and analysis
- **🛡️ RFC-0011 Trust Center** - Federal agency access portal

### Real-time Features:
- ✅ **Live KSI Status**: Pass/fail for all Key Security Indicators with auto-refresh
- 🔍 **Advanced Filtering**: Search and filter by status, category, keyword, or enhancement opportunities
- 💻 **CLI Evidence**: View actual AWS CLI commands with execution details and timing
- 📋 **Detailed Reasoning**: Understand why each KSI passed/failed with assessment breakdown
- 📈 **Enhancement Detection**: Identification of improvement opportunities in passing KSIs
- 🐛 **GitHub Integration**: Report failed KSIs and create enhancement tracking issues
- 📊 **Compliance Metrics**: Real-time dashboard with trend tracking and 4-metric overview
- 🌙 **Modern Interface**: Light/dark mode with responsive design and keyboard shortcuts

### 🛡️ Federal Agency Portal (RFC-0011 Compliant)
- **🔧 API Access**: Machine-readable authorization data with structured endpoints
- **📋 Federal Access Request**: Official .gov/.mil workflow for authorization materials
- **🚨 Incident Reporting**: FedRAMP Category 1-5 classification templates
- **📞 Emergency Hotline**: 24/7 security incident response (1-hour SLA)

### 🔄 Continuous Improvement Features
- **Proactive Enhancement Tracking**: Find improvements in compliant controls
- **Business Value Assessment**: ROI calculation for security enhancements  
- **Priority-Based Roadmaps**: High/Medium/Low improvement sequencing
- **Evidence Currency Management**: Automatic staleness detection and refresh cycles

### 📱 Interactive Experience
- **Command Execution Analysis**: Full CLI logs with comprehensive command register
- **Why This Result**: Detailed assessment explanations with technical breakdown
- **Enhancement Planning**: Structured improvement workflows with templates
- **Export Capabilities**: JSON downloads, GitHub issue creation, incident templates

---

## 📁 Key Transparency Artifacts

| File                                | Purpose                                                  | Access |
|-------------------------------------|----------------------------------------------------------|--------|
| `unified_ksi_validations.json`      | **Source of Truth**: All validation results with evidence | [📄 Download](https://meridian-knowledge-solutions.github.io/fedramp_20x_public_submission_live/unified_ksi_validations.json) |
| `failed_ksi_report_readable.md`     | **Remediation Guide**: Detailed analysis of failed KSIs | [📋 View Report](https://meridian-knowledge-solutions.github.io/fedramp_20x_public_submission_live/failed_ksi_report_readable.md) |
| `evidence_commit_metadata.json`     | **Audit Trail**: Git SHA + timestamps for all evidence | [🔍 Inspect](https://meridian-knowledge-solutions.github.io/fedramp_20x_public_submission_live/evidence_commit_metadata.json) |
| `docs/ksi_rules/`                   | **Rule Documentation**: Auto-generated KSI validation logic | [📚 Browse](https://github.com/Meridian-Knowledge-Solutions/fedramp_20x_public_submission_live/tree/main/docs/ksi_rules) |

---

## 🏗️ Architecture & Validation Flow

### Automated Evidence Pipeline
```
Private Repository → CLI Commands → Evidence Collection → Assertion Logic → Public Dashboard
```

### Daily Automation Process
1. **🔄 Evidence Collection**: GitHub Actions execute AWS CLI commands
2. **⚡ Validation Engine**: Python assertion logic evaluates compliance
3. **📊 Results Generation**: Consolidated JSON with detailed reasoning
4. **🌐 Dashboard Update**: Real-time sync to public trust center
5. **📋 Report Generation**: Failed KSI analysis and remediation guidance

### Validation Methodology
- **CLI-Based Evidence**: Technical controls verified via AWS API
- **Automated Assertions**: Machine-readable pass/fail logic
- **Continuous Monitoring**: Daily validation with trend tracking
- **Audit-Ready**: Complete trail from command to conclusion

---

## 🔍 For Federal Agencies & Auditors

### What You Can See
- **Real-time Compliance**: Current security posture across all KSIs
- **Evidence Transparency**: Actual CLI commands and raw outputs
- **Validation Logic**: How each security control is assessed
- **Trend Analysis**: Compliance improvement over time
- **Remediation Plans**: Detailed guidance for addressing failures

### Audit Trail Components
| Audit Question | Available Evidence |
|----------------|-------------------|
| **What was tested?** | CLI commands visible in dashboard + JSON |
| **How was it validated?** | Assertion logic in source repository |
| **When was it tested?** | Timestamps in all evidence files |
| **What were the results?** | Real-time dashboard + downloadable reports |
| **Can it be reproduced?** | Complete automation via GitHub Actions |

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

---

## 🛡️ Trust Center Features

### 📋 Available Materials

**🔒 Public Access:**
- Real-time compliance dashboard
- KSI validation methodology  
- Service architecture overview
- Continuous monitoring reports

**🔐 Federal Agency Access:**
- Complete authorization package
- Detailed security plans
- 3PAO assessment reports
- Continuous monitoring data

### 📞 CSP Contact Information
- **Primary Contact**: Meridian Federal Cloud Operations 
- **Email**: [security@meridianks.com](mailto:security@meridianks.com)
- **Phone**: +1 (571) 665-5287 
- **Support**: 24/7 for critical security issues

---

## 🎯 FedRAMP 20x Pilot Goals

This implementation demonstrates:
- ✅ **Machine-readable compliance data** for automated assessment
- ✅ **Real-time transparency** for federal agency trust
- ✅ **Reproducible validation** through automated pipelines
- ✅ **Continuous monitoring** with immediate visibility
- ✅ **Audit-ready documentation** with complete traceability
- ✅ **Open source methodology** for community advancement

---

## 🚀 Service Information

- **Service**: Meridian LMS
- **Authorization Level**: FedRAMP 20x Low
- **Hosting Environment**: AWS Commercial (US-East)
- **Assessment Method**: Machine-readable validation with automated KSI assessment

---

## 📈 Compliance Commitment

We are committed to achieving and maintaining **FedRAMP 20x Low authorization** through:
- Daily automated validation
- Continuous security monitoring  
- Proactive remediation of failed KSIs
- Transparent reporting to federal stakeholders

---

## 📬 Community & Feedback

This repository supports GSA's FedRAMP 20x pilot goals of:
- **Community-driven trust models**
- **Transparent, machine-verifiable compliance**
- **Practical automation for real-world authorization**

**Questions?** [Open a GitHub Issue](https://github.com/Meridian-Knowledge-Solutions/fedramp_20x_public_submission_live/issues) or email [security@meridianks.com](mailto:security@meridianks.com)

---

## 📄 Compliance Standards

**Compliant with:**
- RFC-0008 (Continuous Reporting)
- RFC-0011 (Trust Center Requirements)
- FedRAMP 20x Low Authorization Requirements
- FedRAMP Minimum Assessment Standard
- FedRAMP 20x Low Definitions and Rules

---

*Last updated: June 6, 2025 | Auto-synced from private validation pipeline*
