
# FedRAMP 20x Machine-Readable Submission Package

This repository contains a machine-readable authorization package developed for the FedRAMP 20x Phase One Pilot. It reflects all Key Security Indicators (KSIs) as outlined in RFC-0006 and integrates metadata, evidence references, and traceability to NIST SP 800-53 controls.

## 📁 Directory Structure

```
machine_readable_package.json
evidence/
  ksi-[code]/
    static/    # PDF screenshots, diagrams, policies, etc.
    live/      # CLI/API outputs, JSON exports, logs, etc.
```

## 📄 machine_readable_package.json

This is the primary structured artifact submitted as part of the pilot. It includes:

### `csp_information`
| Field | Description |
|-------|-------------|
| `organization_name` | Name of the Cloud Service Provider |
| `system_name` | The system/service being submitted for authorization |
| `deployment_environment` | Cloud deployment (e.g., AWS GovCloud (US)) |
| `submission_date` | Date of submission |
| `contact_email` | Primary contact for submission |
| `submission_version` | Version of the submitted package |

### `submission_summary`
| Field | Description |
|-------|-------------|
| `rationale` | Summary of submission and control families included |
| `3pao_summary` | Summary of independent review (optional in pilot) |

### `ksi_validations`
This array contains all nine KSI blocks:

- `KSI-CNA`: Cloud Native Architecture
- `KSI-SC`: Service Configuration
- `KSI-IAM`: Identity and Access Management
- `KSI-MLA`: Monitoring, Logging, and Auditing
- `KSI-CM`: Change Management
- `KSI-PI`: Policy and Inventory
- `KSI-3IR`: Third Party Information Resources
- `KSI-CE`: Cybersecurity Education
- `KSI-IR`: Incident Response

Each KSI includes:

| Field | Description |
|-------|-------------|
| `ksi_id` | Unique identifier for the KSI |
| `title` | Full title of the KSI |
| `impact_levels` | Which FedRAMP baselines this KSI applies to |
| `related_controls` | NIST SP 800-53 controls mapped to the KSI |
| `continuous_reporting` | Boolean indicating if evidence can be automatically refreshed |
| `validation_results[]` | Array of validations under the KSI |

### `validation_results[]`
Each validation includes:

| Field | Description |
|-------|-------------|
| `description` | The security capability being asserted |
| `assertion` | `"true"` or `"false"` (boolean result of validation) |
| `evidence_reference` | File path to supporting artifact in evidence directory |
| `evidence_type` | Format/type of evidence (e.g., PDF, CLI Output, Policy) |
| `validation_method` | Explanation of how the validation was performed |
| `validation_timestamp` | Timestamp of the validation or evidence snapshot |
| `service_dependencies` | AWS/GCP/Azure services used in the implementation |

### `data_schema_definition`
| Field | Description |
|-------|-------------|
| `field_definitions` | Metadata describing the meaning of each field in the package |

---

## 📝 Pilot Participation Guidance

This format aligns with the Key Security Indicators model published in [RFC-0006](https://github.com/FedRAMP/rfcs/discussions/18). The structure is intentionally future-proof and allows gradual movement from static compliance toward continuous validation.

To contribute or suggest improvements, submit issues or PRs referencing this repo and RFC alignment.
