### Compliance

**Description:** _Compliance details of a stakeholder_

**Referenced By (1):**
- [Draft Option Grant](draft_option_grant.md)

**References (3):**
- [Federal Exemption](federal_exemption.md)
- [Iso3166 Set1 Alpha3 Code](iso3166_set1_alpha3_code.md)
- [Iso3166 Set2 Code](iso3166_set2_code.md)

**Example:**
```json
{
  "countryOfResidency": {
    "value": "USA"
  },
  "stateOfResidency": {
    "value": "US-CA"
  },
  "federalExemption": "RULE_701"
}
```

**Properties:**

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| `countryOfResidency` | [Iso3166 Set1 Alpha3 Code](iso3166_set1_alpha3_code.md) | The country of residency of the stakeholder  | - |
| `federalExemption` | [Federal Exemption](federal_exemption.md) | The federal exemption rule for the draft option grant. <br/>**Constraints:** Max length: 32 | - |
| `stateOfResidency` | [Iso3166 Set2 Code](iso3166_set2_code.md) | The state of residency of the stakeholder. Should only be provided if country_of_residency is USA. | - |