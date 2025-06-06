# KSI-SVC-02: Encrypt or secure network traffic

<<<<<<< Updated upstream
<<<<<<< Updated upstream
*Generated on 2025-06-06 08:21:01 UTC*
=======
*Generated on 2025-06-06 08:22:08 UTC*
>>>>>>> Stashed changes
=======
*Generated on 2025-06-06 08:23:18 UTC*
>>>>>>> Stashed changes

## 📖 Overview

**KSI ID:** `KSI-SVC-02`
**Description:** Encrypt or secure network traffic
**Justification:** Validates network traffic encryption through load balancers, VPC endpoints, and HTTPS configurations
<<<<<<< Updated upstream
<<<<<<< Updated upstream
**Last Validation:** ✅ 2025-06-06T08:21:01.668876
=======
**Last Validation:** ✅ 2025-06-06T08:22:08.664811
>>>>>>> Stashed changes
=======
**Last Validation:** ✅ 2025-06-06T08:23:18.265951
>>>>>>> Stashed changes
**Result:** ✅ Network traffic security configured: ℹ️ No load balancers found (acceptable for low-impact); ⚠️ No VPC endpoints found - traffic goes over internet

## 🛠️ Implementation

### Commands Executed
1. **Command:** `aws elbv2 describe-load-balancers --output json`
   **Purpose:** Check load balancer SSL/TLS configurations

2. **Command:** `aws ec2 describe-vpc-endpoints --output json`
   **Purpose:** Validate VPC endpoints for private service communication

## 📋 Evidence Requirements

### 🖥️ CLI Validation
- **Command:** `aws elbv2 describe-load-balancers --output json`
  - **Purpose:** Check load balancer SSL/TLS configurations
- **Command:** `aws ec2 describe-vpc-endpoints --output json`
  - **Purpose:** Validate VPC endpoints for private service communication

## 🧠 Validation Logic

**Function:** `evaluate_KSI_SVC_02`

**Documentation:** Simple rule for KSI-SVC-02: Network traffic encryption
Expected: Load Balancers + VPC Endpoints

### Rule Implementation
```python
def evaluate_KSI_SVC_02(cli_output):
    """
    Simple rule for KSI-SVC-02: Network traffic encryption
    Expected: Load Balancers + VPC Endpoints
    """
    if "commands" not in cli_output:
        return False, "❌ Multi-command format required"
    commands = cli_output["commands"]
    load_balancers = None
    vpc_endpoints = None
    for cmd in commands:
        cli_command = cmd.get("cli_command", "")
        raw_output = cmd.get("raw_output", {})
        if "describe-load-balancers" in cli_command:
            load_balancers = raw_output.get("LoadBalancers", [])
        elif "describe-vpc-endpoints" in cli_command:
            vpc_endpoints = raw_output.get("VpcEndpoints", [])
    findings = []
    encryption_mechanisms = 0
    if load_balancers is not None:
    # ... (additional validation logic) ...
```

## 📜 Compliance Mapping

**Control Description:** Encrypt or secure network traffic

**Implementation Justification:** Validates network traffic encryption through load balancers, VPC endpoints, and HTTPS configurations

**FedRAMP 20x Category:** Service Configuration

## 📊 Recent Validation Results

**Evidence Analysis:** ✅ All 2 commands executed successfully | ✅ Command output received | ✅ Command output received

**Commands Executed:** 2
**Validation Method:** multi-command

---
*Documentation auto-generated from KSI validation pipeline*
*Source: cli_command_register.json, unified_ksi_validations.json*