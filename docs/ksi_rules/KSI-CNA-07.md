# KSI-CNA-07: Confirm official AMIs

## 🛠 CLI Command
```bash
aws ec2 describe-instances --query Reservations[*].Instances[*].ImageId
```

## ✅ Validation Goal
Confirm official AMIs

## 📋 Justification
Initial command retained; sufficient for initial validation unless Low Mode-specific refactor is needed.

## 📆 Last Evaluated
N/A

## 📄 CLI Output Snippet
```json

```