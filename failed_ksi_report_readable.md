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

### 🔧 KSI-CMT

#### KSI-CMT-02

**What it does:** Track and control changes to information resources

**Issue:** Exception during evaluation: No module named 'dateutil'

**Validation Method:** 8 commands (8 successful): aws cloudformation list-stacks --stack-status-filter CREATE_COMPLETE UPDATE_COMPLETE UPDATE_ROLLBACK_COMPLETE --output json; aws ec2 describe-instances --query 'Reservations[*].Instances[*].[InstanceId,Tags,LaunchTime,ImageId]' --output json (+6 more)

**Last Checked:** 2025-06-26 02:53 UTC

---
## 🎯 Next Steps

🕐 **Estimated Time to Complete:** 1-2 weeks

### 🔧 Technical Items (1 items)
**Advanced setup** - Complex configurations:
- KSI-CMT-02: Technical implementation needed

### 📞 Need Help?
Contact our security team at security@meridianks.com for assistance with any of these items.
---

## 📞 Questions?

📧 **Email:** security@meridianks.com  
📅 **Report Generated:** 2025-06-26 02:53 UTC  
🔍 **Source:** Automated FedRAMP 20x validation pipeline
