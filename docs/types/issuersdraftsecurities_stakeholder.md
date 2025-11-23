### Issuersdraftsecurities Stakeholder

**Description:** _Details of a stakeholder_

**Referenced By (1):**
- [Draft Option Grant](draft_option_grant.md)

**References (2):**
- [Issuersdraftsecurities Stakeholder Relationship](issuersdraftsecurities_stakeholder_relationship.md)
- [Stakeholder Type](stakeholder_type.md)

**Example:**
```json
{
  "name": "Jane Doe",
  "email": "jane.doe@example.com",
  "employeeId": "adsfc123",
  "type": "STAKEHOLDER_TYPE_INDIVIDUAL",
  "relationship": "STAKEHOLDER_RELATIONSHIP_EMPLOYEE"
}
```

**Properties:**

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| `email` | `STRING` | The email of the stakeholder to whom this security will be issued. <br/>**Constraints:** Min length: 1, Max length: 100 | - |
| `employeeId` | `STRING` | The employee id of the stakeholder in the HR partner system. <br/>**Constraints:** Max length: 100 | - |
| `name` | `STRING` | The name of the stakeholder to whom this security will be issued. <br/>**Constraints:** Min length: 1, Max length: 256 | - |
| `relationship` | [Issuersdraftsecurities Stakeholder Relationship](issuersdraftsecurities_stakeholder_relationship.md) | The relationship of the stakeholder to the issuer. | - |
| `type` | [Stakeholder Type](stakeholder_type.md) | The type of the stakeholder. | - |