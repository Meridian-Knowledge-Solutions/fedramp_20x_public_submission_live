# KSI-CNA-05: Inspect interface policies

## 🛠 CLI Command
```bash
aws wafv2 list-web-acls --scope CLOUDFRONT --region us-east-1
```

## ✅ Validation Goal
Inspect interface policies

## 📋 Justification
WAF is used to prevent DoS attacks; requires follow-up call to get-web-acl to validate rules and targets.

## 📆 Last Evaluated
N/A

## 📄 CLI Output Snippet
```json

```