### Vesting Schedule Template

**Endpoints:** `GET /v1alpha1/issuers/{issuerId}/vestingScheduleTemplates`

**Description:** _Details of a vesting schedule template._

**Example:**
```json
{
  "id": "1",
  "issuerId": "7",
  "name": "1/24, No Cliff",
  "description": "Shares vest monthly for the next 24 months on the same day as the start date.",
  "vestingScheduleType": "DATE"
}
```

**Properties:**
| Property | Type | Description | Required |
| --- | --- | --- | --- |
| `description` | `STRING` | The description of the vesting schedule template. <br/>**Constraints:** Max length: 1000 | - |
| `id` | `STRING` | The identifier of the vesting schedule template. <br/>**Constraints:** Max length: 50 | - |
| `issuerId` | `STRING` | The identifier of the issuer to which this vesting schedule template belongs. <br/>**Constraints:** Max length: 50 | - |
| `name` | `STRING` | The name of the vesting schedule template. <br/>**Constraints:** Max length: 500 | - |
| `vestingScheduleType` | [Vesting Schedule Type](../types/vesting_schedule_type.md) | The type of vesting schedule found within this template. | - |