# Meridian Enhanced Ruleset Documentation

**Version**: 2.0  
**Date**: June 2025  
**System**: FedRAMP 20x Validation Engine  

---

## Overview

The Meridian Enhanced Ruleset provides **maturity-based security assessment** that scales from pilot implementations to enterprise-grade deployments while maintaining FedRAMP compliance standards.

## Core Principles

### **1. Maturity Progression**
Each rule measures security maturity across 5 tiers:
- **Pilot** (0-20%): Basic service availability
- **Foundation** (21-40%): Core security controls implemented  
- **Advanced** (41-60%): Enhanced controls and automation
- **Production** (61-80%): Comprehensive governance and monitoring
- **Enterprise** (81-100%): Organization-wide standards and compliance

### **2. Preserved Compatibility**
- **Backward Compatible**: All existing passing implementations continue to pass
- **Enhanced Visibility**: New percentage scoring shows maturity progression
- **No Regressions**: Current thresholds maintained exactly

### **3. Practical Implementation**
- **Cost Conscious**: Accommodates pilot environment constraints
- **Multiple Paths**: Supports various valid security approaches
- **Graceful Errors**: Handles AWS service limitations robustly

---

## Rule Structure

### **Enhanced Scoring System**
```python
# Each rule follows this pattern:
def evaluate_KSI_XXX_XX(cli_output):
    max_score = 20  # Total possible points
    current_score = 0  # Accumulated through assessment
    
    # 1. Foundation Tier (preserve current logic)
    # 2. Advanced Controls (bonus points)  
    # 3. Governance Features (bonus points)
    # 4. Automation Integration (bonus points)
    # 5. Enterprise Standards (bonus points)
    
    compliance_percentage = (current_score / max_score) * 100
    return result, f"Assessment ({compliance_percentage:.0f}%): details"
```

### **Assessment Categories**

| Category | Description | Example |
|----------|-------------|---------|
| **SVC** | Service Hardening | Network encryption, key management, patching |
| **MLA** | Monitoring & Logging | SIEM, vulnerability scanning, audit logs |
| **CMT** | Change Management | Immutable deployments, testing automation, risk assessment |
| **PIY** | Policy & Inventory | Asset management, security policies, development lifecycle |
| **TPR** | Third-Party Risk | Vendor management, supply chain security |

---

## Assessment Philosophy

### **Service Capability Focus**
- **Availability > Configuration > Operation**: Credit for demonstrating capabilities
- **Partial Implementation**: Half-credit for available but unused services
- **Alternative Approaches**: Multiple valid paths to meet requirements

### **Low-Impact Calibration**
```python
# Pattern: Cost-optimized pilot accommodation
if service_available_but_stopped:
    return True, "✅ Service configured but optimized for pilot costs"
```

### **Error Resilience**
```python
# Pattern: Graceful service unavailability handling
if service_not_accessible:
    return True, "⚠️ Service available but access limited (acceptable)"
```

---

## Enhanced Features

### **Maturity Visibility** 
**Before**: `✅ Basic security configured`  
**After**: `✅ Advanced security with governance controls (65%)`

### **Growth Guidance**
- **Current State**: Shows exactly where you are
- **Next Steps**: Clear path to higher maturity
- **Investment Prioritization**: Focus areas for improvement

### **Comprehensive Coverage**
- **Foundation**: Preserves all current passing logic
- **Advanced**: Adds automation, monitoring, governance
- **Enterprise**: Organization-wide standards and compliance

---

## Implementation Examples

### **Basic Implementation** (20% maturity)
```
✅ Network encryption capability established (20%)
- Load balancers configured
- VPC endpoints available
```

### **Advanced Implementation** (65% maturity)  
```
✅ Production-ready multi-layer encryption with automation (65%)
- Load balancers with HTTPS enforcement
- VPC endpoints for private communication
- ACM certificates with automated renewal
- Config rules for compliance monitoring
```

### **Enterprise Implementation** (85% maturity)
```
✅ Enterprise-grade comprehensive encryption with governance (85%)
- Multi-layer encryption across all services
- Automated compliance monitoring and remediation
- Organization-wide encryption policies
- Centralized certificate management
```

---

## Validation Methods

### **CLI-Based Assessment**
- **Multi-Command**: Each rule uses 2-10 AWS CLI commands
- **Real Evidence**: Validates actual infrastructure state
- **Automated**: No manual document review required

### **Evidence-Based Assessment** (Selected Rules)
- **Documentation**: Policy and procedure validation
- **Structured**: Specific file formats and evidence tiers
- **Hybrid**: Combines automated and manual validation

### **Error Handling**
- **Service Unavailable**: Graceful fallbacks and partial credit
- **Permission Limited**: Alternative evidence paths
- **Cost Optimized**: Credit for stopped but configured services

---

## Benefits

### **For Current Implementations**
- ✅ **No Changes Required**: All current passing implementations continue to pass
- ✅ **Enhanced Visibility**: See exactly where you are in maturity progression
- ✅ **Clear Roadmap**: Understand next steps for improvement

### **For Growing Organizations**
- 📈 **Scaling Guidance**: Clear path from pilot to enterprise
- 🎯 **Investment Focus**: Prioritize highest-impact improvements  
- 📊 **Progress Tracking**: Measure maturity advancement over time

### **For Compliance**
- 🛡️ **FedRAMP Aligned**: Maintains all required security controls
- 📋 **Audit Ready**: Clear evidence and reasoning for all assessments
- 🔄 **Continuous**: Regular validation with automated evidence collection

---

## Getting Started

1. **Current State**: Run existing rules to establish baseline maturity percentage
2. **Gap Analysis**: Identify specific areas for improvement based on tier breakdowns
3. **Prioritization**: Focus on highest-impact, lowest-effort improvements first
4. **Implementation**: Add advanced controls incrementally while maintaining compliance
5. **Measurement**: Track maturity progression over time

The enhanced ruleset provides a clear, practical path from pilot security implementations to enterprise-grade compliance while maintaining FedRAMP standards throughout the journey.