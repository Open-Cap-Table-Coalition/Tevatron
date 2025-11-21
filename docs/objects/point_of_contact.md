### Point Of Contact

**Endpoints:** `GET /v1alpha1/issuers/{issuerId}/pointsOfContact`

**Description:** _A point of contact for an issuer. Examples include a Legal Admin or an Option Signatory._

**Example:**
```json
{
  "issuerId": "7",
  "userFullName": "MaryStuart",
  "userEmail": "mary.stuart@example.com",
  "type": "PRIMARY_CONTACT"
}
```

**Properties:**
| Property | Type | Description | Required |
| --- | --- | --- | --- |
| `issuerId` | `STRING` | An identifier for the issuer related to the point of contact. <br/>**Constraints:** Max length: 50 | - |
| `type` | [Point Of Contact Type](../types/point_of_contact_type.md) | The type of point of contact. | - |
| `userEmail` | `STRING` | The point of contact email. <br/>**Constraints:** Min length: 1, Max length: 1000 | - |
| `userFullName` | `STRING` | The point of contact full name. <br/>**Constraints:** Min length: 1, Max length: 1000 | - |