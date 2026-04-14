### Rsu Issuance Transaction

**Description:** _The issuance transaction for an RSU award. Represents the initial grant of restricted stock units._

**Referenced By (1):**
- [Rsu Transaction Item](rsu_transaction_item.md)

**References (2):**
- [Decimal](decimal.md)
- [Iso8601 Complete Calendar Date Time](iso8601_complete_calendar_date_time.md)

**Example:**
```json
{
  "issueDatetime": {
    "value": "2024-01-15T00:00:00Z"
  },
  "quantity": {
    "value": "5000"
  },
  "equityPlanId": "42",
  "shareClassId": "10",
  "vestingScheduleTemplateId": "7"
}
```

**Properties:**

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| `equityPlanId` | `STRING` | The identifier of the equity plan from which the RSU award was issued. <br/>**Constraints:** Max length: 50 | - |
| `issueDatetime` | [Iso8601 Complete Calendar Date Time](iso8601_complete_calendar_date_time.md) | The date and time the RSU award was issued. | - |
| `quantity` | [Decimal](decimal.md) | The number of restricted stock units granted. | - |
| `shareClassId` | `STRING` | The identifier of the share class. May be absent if the plan has no associated share class. <br/>**Constraints:** Max length: 50 | - |
| `vestingScheduleTemplateId` | `STRING` | The identifier of the vesting schedule template. May be absent if the award has no vesting schedule. <br/>**Constraints:** Max length: 50 | - |