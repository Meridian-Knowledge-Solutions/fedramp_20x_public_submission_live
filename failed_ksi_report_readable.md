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

#### KSI-CNA-03

**What it does:** Use logical networking for traffic flow controls

**Issue:** Insufficient logical networking (3%) - no meaningful traffic flow controls:  No logical routing: Using default route tables only (1 total);  No cus...

**Validation Method:** 9 commands (9 successful): aws ec2 describe-route-tables --output json; aws ec2 describe-network-acls --output json (+7 more)

**Last Checked:** 2025-06-09 22:46 UTC

---
## 🎯 Next Steps

🕐 **Estimated Time to Complete:** 1-2 weeks

### ⚙️ Configuration Items (1 items)
**Technical setup** - Configure AWS services:
- KSI-CNA-03: Set up required AWS service

### 📞 Need Help?
Contact our security team at security@meridianks.com for assistance with any of these items.
---

## 📞 Questions?

📧 **Email:** security@meridianks.com  
📅 **Report Generated:** 2025-06-09 22:46 UTC  
🔍 **Source:** Automated FedRAMP 20x validation pipeline
