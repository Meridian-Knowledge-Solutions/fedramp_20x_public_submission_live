# 🛡️ Security Compliance Report

> 🟡 **Status:** Minor Issues

## 📊 Quick Overview

| Metric | Value |
|--------|--------|
| **Compliance Rate** | 94.1% |
| **Items Passing** | 48 |
| **Items Needing Work** | 3 |
| **Last Checked** | Unknown |

💡 **Bottom Line:** 3 security items need attention to reach full compliance.
## 🔍 Items Needing Attention

Here's what needs to be fixed, with the technical details for your team:

### 🔧 KSI-CNA

#### KSI-CNA-01

**What it does:** Configure ALL information resources to limit inbound and outbound traffic

**Issue:** No VPCs found

**Validation Method:** 8 commands (8 successful): aws ec2 describe-security-groups --output json; aws ec2 describe-network-acls --output json (+6 more)

**Last Checked:** 2025-06-09 21:56 UTC

---

#### KSI-CNA-04

**What it does:** Use immutable infrastructure patterns

**Issue:** No Infrastructure as Code patterns found

**Validation Method:** 9 commands (9 successful): aws ec2 describe-instances --query 'Reservations[*].Instances[*].[InstanceId,Tags,LaunchTime,ImageId]' --output json; aws ec2 describe-launch-templates --output json (+7 more)

**Last Checked:** 2025-06-09 21:56 UTC

---

#### KSI-CNA-05

**What it does:** Have denial of service protection

**Issue:** AWS Shield error:

**Validation Method:** 8 commands (7 successful): aws shield describe-subscription --output json; aws wafv2 list-web-acls --scope REGIONAL --output json (+6 more)

**Last Checked:** 2025-06-09 21:56 UTC

---
## 🎯 Next Steps

🕐 **Estimated Time to Complete:** 1-2 weeks

### ⚙️ Configuration Items (1 items)
**Technical setup** - Configure AWS services:
- KSI-CNA-05: Set up required AWS service

### 🔧 Technical Items (2 items)
**Advanced setup** - Complex configurations:
- KSI-CNA-01: Technical implementation needed
- KSI-CNA-04: Technical implementation needed

### 📞 Need Help?
Contact our security team at security@meridianks.com for assistance with any of these items.
---

## 📞 Questions?

📧 **Email:** security@meridianks.com  
📅 **Report Generated:** 2025-06-09 21:56 UTC  
🔍 **Source:** Automated FedRAMP 20x validation pipeline
