# KSI-CNA-05: Have denial of service protection

*Generated on 2025-06-09 21:56:37 UTC*

## 📖 Overview

**KSI ID:** `KSI-CNA-05`
**Description:** Have denial of service protection
**Justification:** Validates comprehensive multi-layer DDoS protection through network-layer shields, application-layer filtering, edge protection, capacity-based mitigation, and automated response capabilities
**Last Validation:** ❌ 2025-06-09T21:56:37.301327
**Result:** ❌ AWS Shield error: 

## 🛠️ Implementation

### Commands Executed
1. **Command:** `aws shield describe-subscription --output json`
   **Purpose:** Check AWS Shield Advanced subscription for premium DDoS protection and response team

2. **Command:** `aws wafv2 list-web-acls --scope REGIONAL --output json`
   **Purpose:** Validate WAF for application-layer DDoS protection and rate limiting

3. **Command:** `aws wafv2 list-web-acls --scope CLOUDFRONT --output json`
   **Purpose:** Check CloudFront WAF for edge-based application protection

4. **Command:** `aws cloudfront list-distributions --output json`
   **Purpose:** Verify CloudFront distributions for edge-based DDoS protection and traffic distribution

5. **Command:** `aws elbv2 describe-load-balancers --output json`
   **Purpose:** Check load balancers for traffic distribution and DDoS mitigation capabilities

6. **Command:** `aws autoscaling describe-auto-scaling-groups --output json`
   **Purpose:** Validate Auto Scaling Groups for capacity-based DDoS mitigation

7. **Command:** `aws route53 list-hosted-zones --output json`
   **Purpose:** Check Route 53 for DNS-layer protection and traffic routing capabilities

8. **Command:** `aws cloudwatch describe-alarms --output json`
   **Purpose:** Verify CloudWatch alarms for DDoS detection and automated response

## 📋 Evidence Requirements

### 🖥️ CLI Validation
- **Command:** `aws shield describe-subscription --output json`
  - **Purpose:** Check AWS Shield Advanced subscription for premium DDoS protection and response team
- **Command:** `aws wafv2 list-web-acls --scope REGIONAL --output json`
  - **Purpose:** Validate WAF for application-layer DDoS protection and rate limiting
- **Command:** `aws wafv2 list-web-acls --scope CLOUDFRONT --output json`
  - **Purpose:** Check CloudFront WAF for edge-based application protection
- **Command:** `aws cloudfront list-distributions --output json`
  - **Purpose:** Verify CloudFront distributions for edge-based DDoS protection and traffic distribution
- **Command:** `aws elbv2 describe-load-balancers --output json`
  - **Purpose:** Check load balancers for traffic distribution and DDoS mitigation capabilities
- **Command:** `aws autoscaling describe-auto-scaling-groups --output json`
  - **Purpose:** Validate Auto Scaling Groups for capacity-based DDoS mitigation
- **Command:** `aws route53 list-hosted-zones --output json`
  - **Purpose:** Check Route 53 for DNS-layer protection and traffic routing capabilities
- **Command:** `aws cloudwatch describe-alarms --output json`
  - **Purpose:** Verify CloudWatch alarms for DDoS detection and automated response

## 🧠 Validation Logic

**Function:** `evaluate_KSI_CNA_05`

**Documentation:** Fixed rule for KSI-CNA-05: Basic DDoS protection
Expected: AWS Shield status

### Rule Implementation
```python
def evaluate_KSI_CNA_05(cli_output):
    """
    Fixed rule for KSI-CNA-05: Basic DDoS protection
    Expected: AWS Shield status
    """
    if "commands" not in cli_output:
        return False, "❌ Multi-command format required"
    commands = cli_output["commands"]
    for cmd in commands:
        cli_command = cmd.get("cli_command", "")
        raw_output = cmd.get("raw_output", {})
        if "describe-subscription" in cli_command:
            if isinstance(raw_output, str):
                if "InvalidParameterValueException" in raw_output or "SubscriptionNotFound" in raw_output:
                    return True, "✅ AWS Shield Standard protection active (sufficient for Low impact)"
                else:
                    return False, f"❌ AWS Shield error: {raw_output[:100]}"
            elif isinstance(raw_output, dict):
                if "SubscriptionArn" in raw_output:
                    return True, "✅ AWS Shield Advanced subscription active"
    # ... (additional validation logic) ...
```

## 📜 Compliance Mapping

**Control Description:** Have denial of service protection

**Implementation Justification:** Validates comprehensive multi-layer DDoS protection through network-layer shields, application-layer filtering, edge protection, capacity-based mitigation, and automated response capabilities

**FedRAMP 20x Category:** Cloud Native Architecture

## 📊 Recent Validation Results

**Evidence Analysis:** ❌ All 8 commands failed execution | ⚠️ No usable output

**Commands Executed:** 8
**Validation Method:** validation-engine-sync

---
*Documentation auto-generated from KSI validation pipeline*
*Source: cli_command_register.json, unified_ksi_validations.json*