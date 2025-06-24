# 🛡️ Security Compliance Report

> 🟠 **Status:** Some Work Needed

## 📊 Quick Overview

| Metric | Value |
|--------|--------|
| **Compliance Rate** | 92.2% |
| **Items Passing** | 47 |
| **Items Needing Work** | 4 |
| **Last Checked** | Unknown |

💡 **Bottom Line:** 4 security items need attention to reach full compliance.
## 🔍 Items Needing Attention

Here's what needs to be fixed, with the technical details for your team:

### 🔧 KSI-RPL

#### KSI-RPL-01

**What it does:** Define Recovery Time Objectives (RTO) and Recovery Point Objectives (RPO)

**Issue:** Exception during evaluation: 'list' object has no attribute 'get'

**Validation Method:** 3 commands (3 successful): aws rds describe-db-instances --query 'DBInstances[*].[DBInstanceIdentifier,BackupRetentionPeriod,LatestRestorableTime,PreferredBackupWindow]' --output json; aws backup list-backup-plans --output json; evidence_check

**Last Checked:** 2025-06-24 02:05 UTC

---

#### KSI-RPL-02

**What it does:** Develop and maintain a recovery plan that aligns with defined recovery objectives

**Issue:** Exception during evaluation: 'list' object has no attribute 'get'

**Validation Method:** 3 commands (2 successful): aws rds describe-db-instances --query 'DBInstances[*].[DBInstanceIdentifier,DeletionProtection,BackupRetentionPeriod,PreferredMaintenanceWindow]' --output json; aws backup describe-backup-plans --output json; evidence_check

**Last Checked:** 2025-06-24 02:05 UTC

---

#### KSI-RPL-03

**What it does:** Perform system backups aligned with recovery objectives

**Issue:** Exception during evaluation: 'list' object has no attribute 'get'

**Validation Method:** 5 commands (5 successful): aws backup list-backup-plans --output json; aws backup get-backup-plan --backup-plan-id $(aws backup list-backup-plans --query 'BackupPlansList[0].BackupPlanId' --output text) --output json (+3 more)

**Last Checked:** 2025-06-24 02:05 UTC

---

#### KSI-RPL-04

**What it does:** A secure cloud service offering will define, maintain, and test incident response plan(s) and recovery capabilities to ensure minimal service disruption and data loss during incidents and contingencies.

**Issue:** Exception during evaluation: 'list' object has no attribute 'get'

**Validation Method:** 4 commands (4 successful): aws backup list-restore-jobs --max-results 20 --output json; aws backup list-backup-jobs --by-state COMPLETED --by-created-after 2024-05-01 --output json (+2 more)

**Last Checked:** 2025-06-24 02:05 UTC

---
## 🎯 Next Steps

🕐 **Estimated Time to Complete:** 2-4 weeks

### 🔧 Technical Items (4 items)
**Advanced setup** - Complex configurations:
- KSI-RPL-01: Technical implementation needed
- KSI-RPL-02: Technical implementation needed
- KSI-RPL-03: Technical implementation needed
- ...and 1 more technical items

### 📞 Need Help?
Contact our security team at security@meridianks.com for assistance with any of these items.
---

## 📞 Questions?

📧 **Email:** security@meridianks.com  
📅 **Report Generated:** 2025-06-24 02:05 UTC  
🔍 **Source:** Automated FedRAMP 20x validation pipeline
