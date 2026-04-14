### Vesting Schedule Template

**Endpoints:** `GET /v1alpha1/issuers/{issuerId}/vestingScheduleTemplates`

**Description:** _Details of a vesting schedule template._

**Referenced By (1):**
- [List Vesting Schedule Templates Response](../types/list_vesting_schedule_templates_response.md)

**References (2):**
- [Vesting Period](../types/vesting_period.md)
- [Vesting Schedule Type](../types/vesting_schedule_type.md)

**Example:**
```json
{
  "id": "1",
  "uuid": "550e8400-e29b-41d4-a716-446655440000",
  "issuerId": "7",
  "name": "1/24, No Cliff",
  "description": "Shares vest monthly for the next 24 months on the same day as the start date.",
  "vestingScheduleType": "DATE",
  "periods": [
    {
      "order": 1,
      "percentage": "100",
      "vestingMethod": "MONTHLY",
      "vestingOccurs": "SAME_DAY_AS_START_DATE",
      "length": 24,
      "lengthUnit": "MONTH"
    }
  ]
}
```

**Properties:**

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| `description` | `STRING` | The description of the vesting schedule template. <br/>**Constraints:** Max length: 1000 | - |
| `id` | `STRING` | The identifier of the vesting schedule template. <br/>**Constraints:** Max length: 50 | - |
| `issuerId` | `STRING` | The identifier of the issuer to which this vesting schedule template belongs. <br/>**Constraints:** Max length: 50 | - |
| `name` | `STRING` | The name of the vesting schedule template. <br/>**Constraints:** Max length: 500 | - |
| `periods` | [`Array` of [Vesting Period](../types/vesting_period.md)] | The vesting periods that define how shares vest. | - |
| `uuid` | `STRING` | The UUID of the vesting schedule template. <br/>**Constraints:** Min length: 36, Max length: 36 | - |
| `vestingScheduleType` | [Vesting Schedule Type](../types/vesting_schedule_type.md) | The type of vesting schedule found within this template. | - |