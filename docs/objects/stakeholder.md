### Stakeholder

**Endpoints:** `GET /v1alpha1/issuers/{issuerId}/stakeholders`

**Description:** _A stakeholder is any person or entity who holds an outstanding security._

**Example:**
```json
{
  "id": "4902",
  "issuerId": "7",
  "fullName": "Emily Wilson",
  "email": "emily@esharesinc.com",
  "employeeId": "1213511",
  "relationship": "STAKEHOLDER_RELATIONSHIP_EMPLOYEE",
  "group": "Founders",
  "entityType": "INDIVIDUAL",
  "address": {
    "country": "USA"
  }
}
```

**Properties:**
| Property | Type | Description | Required |
| --- | --- | --- | --- |
| `address` | [Stakeholder Address](../types/stakeholder_address.md) | The address of the stakeholder. This will not be set for all stakeholders. | - |
| `email` | `STRING` | The stakeholder's email. <br/>**Constraints:** Max length: 1000 | - |
| `employeeId` | `STRING` | An employee identifier for the stakeholder, if it exists. <br/>**Constraints:** Max length: 256 | - |
| `entityType` | [Stakeholder Entity Type](../types/stakeholder_entity_type.md) | The entity type of the stakeholder. This will not be set for all stakeholders. <br/>**Constraints:** Max length: 1000 | - |
| `fullName` | `STRING` | The stakeholder's full legal name. <br/>**Constraints:** Max length: 1000 | - |
| `group` | `STRING` | The group to which the stakeholder belongs. This will not be set for all stakeholders. <br/>**Constraints:** Max length: 1000 | - |
| `id` | `STRING` | The identifier of the stakeholder. <br/>**Constraints:** Max length: 50 | - |
| `issuerId` | `STRING` | An identifier for the issuer related to the stakeholder. <br/>**Constraints:** Max length: 50 | - |
| `relationship` | [Stakeholder Relationship](../types/stakeholder_relationship.md) | The relationship of the stakeholder with the issuer. This will not be set for all stakeholders. | - |