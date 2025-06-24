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

### 🔧 KSI-CNA

#### KSI-CNA-04

**What it does:** Use immutable infrastructure patterns

**Issue:** Exception during evaluation: No module named 'dateutil'

**Validation Method:** 9 commands (9 successful): aws ec2 describe-instances --query 'Reservations[*].Instances[*].[InstanceId,Tags,LaunchTime,ImageId]' --output json; aws ec2 describe-launch-templates --output json (+7 more)

**Last Checked:** 2025-06-24 18:59 UTC

---
## 🎯 Next Steps

🕐 **Estimated Time to Complete:** 1-2 weeks

### 🔧 Technical Items (1 items)
**Advanced setup** - Complex configurations:
- KSI-CNA-04: Technical implementation needed

### 📞 Need Help?
Contact our security team at security@meridianks.com for assistance with any of these items.
---

## 📞 Questions?

📧 **Email:** security@meridianks.com  
📅 **Report Generated:** 2025-06-24 18:59 UTC  
🔍 **Source:** Automated FedRAMP 20x validation pipeline
