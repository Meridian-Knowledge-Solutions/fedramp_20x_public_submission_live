# FedRAMP KSI Logic Explainer

A tool that explains the evaluation logic for each Key Security Implementation (KSI) in human-readable terms for 3PAO assessors and FedRAMP stakeholders.

## What This Tool Does

Bridges the gap between automated FedRAMP assessment results and understanding **WHY** a KSI passed or failed. Instead of just seeing a score, you get the step-by-step logic that determined the result.

**Example**: Rather than "KSI_CNA_01: 85%", you see:
```
✅ Award points for ingress controls (Security Groups are restrictive)
✅ Award points for egress controls (Custom rules detected)  
✅ Award bonus points for subnet-level controls (Network ACLs configured)
⚠️ Missing VPC Endpoints (reduces score)
```

## Who Should Use This

- **3PAO Assessors** conducting FedRAMP assessments
- **Cloud Security Architects** designing compliant systems  
- **Compliance Teams** preparing for FedRAMP authorization
- **DevSecOps Teams** implementing security controls

## Quick Start

### Requirements
- Python 3.6+ (most systems have this)
- No additional packages needed

### Download and Run
```bash
# Download the script
curl -O https://raw.githubusercontent.com/Meridian-Knowledge-Solutions/fedramp_20x_public_submission_live/main/3PAO-Fortreum/ksi_explainer.py

# Make it executable (Linux/Mac)
chmod +x ksi_explainer.py

# Run interactively
python3 ksi_explainer.py --interactive
```

### First Steps
```bash
# See all available options
python3 ksi_explainer.py

# Explain a specific KSI
python3 ksi_explainer.py KSI_CNA_01

# Show all KSIs by category
python3 ksi_explainer.py --categories
```

## Common Use Cases

### During Assessment Review
```bash
# Generate full logic documentation
python3 ksi_explainer.py --report > ksi_logic_reference.txt

# Understand why a specific KSI failed
python3 ksi_explainer.py KSI_IAM_01

# Search for specific topics
python3 ksi_explainer.py --interactive
# Then choose option 4 to search (e.g., "MFA", "encryption", "backup")
```

### Pre-Assessment Planning
```bash
# Review all networking requirements
python3 ksi_explainer.py --report KSI_CNA_01 KSI_CNA_02 KSI_CNA_03

# Understand identity management logic
python3 ksi_explainer.py --report KSI_IAM_01 KSI_IAM_04
```

### Team Training
```bash
# Interactive exploration mode
python3 ksi_explainer.py --interactive

# Show assessment methodology overview
python3 ksi_explainer.py --summary
```

## Available KSI Categories

- **CNA**: Cloud Networking & Architecture (5 KSIs)
- **SVC**: Services (3 KSIs documented)
- **IAM**: Identity & Access Management (2 KSIs documented)  
- **MLA**: Monitoring, Logging & Analysis (2 KSIs documented)
- **CMT**: Configuration Management & Testing (3 KSIs documented)
- **PIY**: Personnel & Information (1 KSI documented)
- **TPR**: Third Party Resources (1 KSI documented)
- **RPL**: Recovery & Resilience (2 KSIs documented)
- **INR**: Incident & Non-Compliance Response (1 KSI documented)

## Important Notes

⚠️ **This tool explains assessment LOGIC, not actual results**
- Use this to understand how evaluations work
- You still need the main assessment script to run actual evaluations
- This is for education and transparency, not for generating compliance reports

✅ **What this helps with:**
- Understanding why KSIs pass or fail
- Planning remediation efforts
- Training assessment teams
- Documenting assessment methodology

❌ **What this doesn't do:**
- Run actual AWS assessments
- Generate official compliance reports
- Replace 3PAO professional judgment
- Provide legal compliance advice

## Getting Help

### Built-in Help
```bash
# Interactive mode with menu
python3 ksi_explainer.py --interactive

# Command-line options
python3 ksi_explainer.py
```

### Example Output
```
KSI_CNA_01: Configure ALL information resources to limit inbound and outbound traffic
============================================================================
Evidence Type: AWS CLI Commands

Logic Flow:
IF Security Groups exist AND most are restrictive (not 0.0.0.0/0 for SSH/RDP):
    ✅ Award points for ingress controls
IF Security Groups have restrictive egress (empty rules or specific targets):
    ✅ Award points for egress controls  
...

Passing Criteria: ≥80% restrictive security groups + some egress controls + network segmentation
```

## License

GitHub Default

## Contributing

This tool documents the assessment logic from the main FedRAMP evaluation script. For questions about specific KSI logic or to suggest improvements, please open an issue in the [GitHub repository](https://github.com/Meridian-Knowledge-Solutions/fedramp_20x_public_submission_live).

---

**Version**: 1.0  
**Last Updated**: June 2025  
**Compatible with**: FedRAMP Low Impact assessments
