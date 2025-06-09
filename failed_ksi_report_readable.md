# 🛡️ Security Compliance Report

> 🟡 **Status:** Minor Issues

## 📊 Quick Overview

| Metric | Value |
|--------|--------|
| **Compliance Rate** | 96.1% |
| **Items Passing** | 49 |
| **Items Needing Work** | 2 |
| **Last Checked** | Unknown |

💡 **Bottom Line:** 2 security items need attention to reach full compliance.
## 🔍 Items Needing Attention

Here's what needs to be fixed, with the technical details for your team:

### 🔧 KSI-CMT

#### KSI-CMT-03

**What it does:** A secure cloud service provider will ensure that all system changes are properly documented and configuration baselines are updated accordingly.

**Issue:** No automated testing and validation:  No CodeBuild projects for automated testing;  No CodePipelines for automated change validation

**Validation Method:** 2 commands (2 successful): aws codebuild list-projects --output json; aws codepipeline list-pipelines --output json

**Last Checked:** 2025-06-09 07:55 UTC

---

### 🔧 KSI-CNA

#### KSI-CNA-05

**What it does:** A secure cloud service offering will use cloud native architecture and design principles to enforce and enhance the Confidentiality, Integrity and Availability of the system.

**Issue:** AWS Shield error:

**Validation Method:** 1 commands (0 successful): aws shield describe-subscription --output json

**Last Checked:** 2025-06-09 07:55 UTC

---
## 🎯 Next Steps

🕐 **Estimated Time to Complete:** 1-2 weeks

### ⚙️ Configuration Items (1 items)
**Technical setup** - Configure AWS services:
- KSI-CNA-05: Set up required AWS service

### 🔧 Technical Items (1 items)
**Advanced setup** - Complex configurations:
- KSI-CMT-03: Technical implementation needed

### 📞 Need Help?
Contact our security team at security@meridianks.com for assistance with any of these items.
---

## 📞 Questions?

📧 **Email:** security@meridianks.com  
📅 **Report Generated:** 2025-06-09 07:55 UTC  
🔍 **Source:** Automated FedRAMP 20x validation pipeline
