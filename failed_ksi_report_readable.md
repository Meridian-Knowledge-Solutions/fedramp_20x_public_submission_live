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

**Issue:** Exception during evaluation: cannot access local variable 'detected_vpcs' where it is not associated with a value

**Validation Method:** 8 commands (8 successful): aws ec2 describe-security-groups --output json; aws ec2 describe-network-acls --output json (+6 more)

**Last Checked:** 2025-06-09 22:20 UTC

---

#### KSI-CNA-02

**What it does:** Design systems to minimize the attack surface and minimize lateral movement if compromised

**Issue:** Insufficient attack surface controls (0%) - critical security gaps:  CRITICAL: All 6 subnets are public (maximum attack surface);  Excellent AZ seg...

**Validation Method:** 9 commands (9 successful): aws ec2 describe-subnets --output json; aws ec2 describe-security-groups --output json (+7 more)

**Last Checked:** 2025-06-09 22:20 UTC

---

#### KSI-CNA-03

**What it does:** Use logical networking for traffic flow controls

**Issue:** Insufficient logical networking (3%) - no meaningful traffic flow controls:  No logical routing: Using default route tables only (1 total);  No cus...

**Validation Method:** 9 commands (9 successful): aws ec2 describe-route-tables --output json; aws ec2 describe-network-acls --output json (+7 more)

**Last Checked:** 2025-06-09 22:20 UTC

---
## 🎯 Next Steps

🕐 **Estimated Time to Complete:** 1-2 weeks

### ⚙️ Configuration Items (1 items)
**Technical setup** - Configure AWS services:
- KSI-CNA-03: Set up required AWS service

### 🔧 Technical Items (2 items)
**Advanced setup** - Complex configurations:
- KSI-CNA-01: Technical implementation needed
- KSI-CNA-02: Technical implementation needed

### 📞 Need Help?
Contact our security team at security@meridianks.com for assistance with any of these items.
---

## 📞 Questions?

📧 **Email:** security@meridianks.com  
📅 **Report Generated:** 2025-06-09 22:20 UTC  
🔍 **Source:** Automated FedRAMP 20x validation pipeline
