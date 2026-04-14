### Sar Issuance Transaction

**Description:** _The issuance transaction for a SAR. Represents the initial issuance of the stock appreciation right._

**Referenced By (1):**
- [Sar Transaction Item](sar_transaction_item.md)

**References (3):**
- [Decimal](decimal.md)
- [Iso8601 Complete Calendar Date Time](iso8601_complete_calendar_date_time.md)
- [Money](money.md)

**Example:**
```json
{
  "issueDatetime": {
    "value": "2024-01-15T00:00:00Z"
  },
  "quantity": {
    "value": "10000"
  },
  "exercisePrice": {
    "currencyCode": {
      "value": "USD"
    },
    "amount": {
      "value": "2.00"
    }
  },
  "equityPlanId": "42",
  "shareClassId": "10",
  "vestingScheduleTemplateId": "7",
  "expirationDatetime": {
    "value": "2034-01-15T00:00:00Z"
  }
}
```

**Properties:**

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| `equityPlanId` | `STRING` | The identifier of the equity plan under which the SAR was issued. <br/>**Constraints:** Max length: 50 | - |
| `exercisePrice` | [Money](money.md) | The per-share exercise price. | - |
| `expirationDatetime` | [Iso8601 Complete Calendar Date Time](iso8601_complete_calendar_date_time.md) | The date and time the SAR expires. | - |
| `issueDatetime` | [Iso8601 Complete Calendar Date Time](iso8601_complete_calendar_date_time.md) | The date and time the SAR was issued. | - |
| `quantity` | [Decimal](decimal.md) | The number of units issued. | - |
| `shareClassId` | `STRING` | The identifier of the share class associated with the SAR. <br/>**Constraints:** Max length: 50 | - |
| `vestingScheduleTemplateId` | `STRING` | The identifier of the vesting schedule template. <br/>**Constraints:** Max length: 50 | - |