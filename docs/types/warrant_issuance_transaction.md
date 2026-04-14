### Warrant Issuance Transaction

**Description:** _The issuance transaction for a warrant. Represents the initial issuance of a warrant._

**Referenced By (1):**
- [Warrant Transaction Item](warrant_transaction_item.md)

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
    "value": "50000"
  },
  "exercisePrice": {
    "currencyCode": {
      "value": "USD"
    },
    "amount": {
      "value": "2.00"
    }
  },
  "purchasePrice": {
    "currencyCode": {
      "value": "USD"
    },
    "amount": {
      "value": "0.25"
    }
  },
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
| `exercisePrice` | [Money](money.md) | The per-share price at which the holder can purchase the underlying shares upon exercise. | - |
| `expirationDatetime` | [Iso8601 Complete Calendar Date Time](iso8601_complete_calendar_date_time.md) | The date and time the warrant expires. May be absent if the warrant has no expiration. | - |
| `issueDatetime` | [Iso8601 Complete Calendar Date Time](iso8601_complete_calendar_date_time.md) | The date and time the warrant was issued. | - |
| `purchasePrice` | [Money](money.md) | The upfront cost paid by the holder to acquire the warrant itself. May be absent if no purchase price was paid. | - |
| `quantity` | [Decimal](decimal.md) | The number of shares the warrant entitles the holder to purchase. | - |
| `shareClassId` | `STRING` | The identifier of the share class associated with the warrant. <br/>**Constraints:** Max length: 50 | - |
| `vestingScheduleTemplateId` | `STRING` | The identifier of the vesting schedule template. May be absent if the warrant has no vesting schedule. <br/>**Constraints:** Max length: 50 | - |