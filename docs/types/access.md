### Access

**Description:** _Context about the access of a given corporation._

**Example:**
```json
{
  "accessLevel": "FULL_ACCESS",
  "accessReason": ""
}
```

**Properties:**
| Property | Type | Description | Required |
| --- | --- | --- | --- |
| `accessLevel` | `STRING` | The access level of a given corporation. <br/>**Constraints:** Min length: 1, Max length: 100 | `REQUIRED` |
| `accessReason` | `STRING` | Details about the access level of a given corporation. <br/>**Constraints:** Max length: 1000 | - |