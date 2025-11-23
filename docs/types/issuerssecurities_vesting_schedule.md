### Issuerssecurities Vesting Schedule

**Description:** _Restricted stock award vesting event information._

**Referenced By (3):**
- [Option Grant](../objects/option_grant.md)
- [Restricted Stock Award](../objects/restricted_stock_award.md)
- [Restricted Stock Unit](../objects/restricted_stock_unit.md)

**References (1):**
- [Iso8601 Complete Calendar Date](iso8601_complete_calendar_date.md)

**Example:**
```json
{
  "name": "1/24 Cliff",
  "lastModifiedDate": {
    "value": "2022-01-31"
  },
  "startDate": {
    "value": "2022-01-31"
  },
  "endDate": {
    "value": "2024-01-31"
  }
}
```

**Properties:**

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| `endDate` | [Iso8601 Complete Calendar Date](iso8601_complete_calendar_date.md) | The end date of the vesting schedule. | - |
| `lastModifiedDate` | [Iso8601 Complete Calendar Date](iso8601_complete_calendar_date.md) | The date the vesting schedule was last modified. | - |
| `name` | `STRING` | The name of the vesting schedule. <br/>**Constraints:** Max length: 500 | - |
| `startDate` | [Iso8601 Complete Calendar Date](iso8601_complete_calendar_date.md) | The start date of the vesting schedule. | - |