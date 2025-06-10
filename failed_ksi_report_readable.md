# 🛡️ Security Compliance Report

> 🟡 **Status:** Minor Issues

## 📊 Quick Overview

| Metric | Value |
|--------|--------|
| **Compliance Rate** | 98.0% |
| **Items Passing** | 50 |
| **Items Needing Work** | 1 |
| **Last Checked** | Unknown |

💡 **Bottom Line:** 1 security items need attention to reach full compliance.
## 🔍 Items Needing Attention

Here's what needs to be fixed, with the technical details for your team:

### 🔧 KSI-TPR

#### KSI-TPR-02

**What it does:** Regularly confirm that services handling federal information or are likely to impact the confidentiality, integrity, or availability of federal information are FedRAMP authorized and securely configured

**Issue:** Exception during evaluation: 'str' object has no attribute 'get'

**Validation Method:** 7 commands (4 successful): aws organizations list-accounts --output json; aws config describe-configuration-recorders --output json (+5 more)

**Last Checked:** 2025-06-10 19:20 UTC

---
## 🎯 Next Steps

🕐 **Estimated Time to Complete:** 1-2 weeks

### 🔧 Technical Items (1 items)
**Advanced setup** - Complex configurations:
- KSI-TPR-02: Technical implementation needed

### 📞 Need Help?
Contact our security team at security@meridianks.com for assistance with any of these items.
---

## 📞 Questions?

📧 **Email:** security@meridianks.com  
📅 **Report Generated:** 2025-06-10 19:20 UTC  
🔍 **Source:** Automated FedRAMP 20x validation pipeline
