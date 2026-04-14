### Option Issuance Transaction

**Description:** _The issuance transaction for an option grant. Represents the initial grant of options._

**Referenced By (1):**
- [Option Transaction Item](../objects/option_transaction_item.md)

**References (4):**
- [Issuerstransactions Stock Option Type](issuerstransactions_stock_option_type.md)
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
  "stockOptionType": "STOCK_OPTION_TYPE_ISO",
  "exercisePrice": {
    "currencyCode": {
      "value": "USD"
    },
    "amount": {
      "value": "1.50"
    }
  },
  "equityPlanId": "42",
  "expirationDatetime": {
    "value": "2034-01-15T00:00:00Z"
  }
}
```

**Properties:**

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| `equityPlanId` | `STRING` | The identifier of the equity plan from which the option grant was issued. <br/>**Constraints:** Max length: 50 | - |
| `exercisePrice` | [Money](money.md) | The per-share price at which the holder can purchase the underlying shares. | - |
| `expirationDatetime` | [Iso8601 Complete Calendar Date Time](iso8601_complete_calendar_date_time.md) | The date and time the option grant expires. | - |
| `issueDatetime` | [Iso8601 Complete Calendar Date Time](iso8601_complete_calendar_date_time.md) | The date and time the option grant was issued. | - |
| `quantity` | [Decimal](decimal.md) | The number of shares reserved from the equity plan share reserve. | - |
| `shareClassId` | `STRING` | The identifier of the share class. May be absent if the plan has no associated share class. <br/>**Constraints:** Max length: 50 | - |
| `stockOptionType` | [Issuerstransactions Stock Option Type](issuerstransactions_stock_option_type.md) | The tax classification of the option grant. Determines the tax treatment based on the jurisdiction and plan type. See `StockOptionType` for all supported values. | - |
| `vestingScheduleTemplateId` | `STRING` | The identifier of the vesting schedule template. May be absent if the grant has no vesting schedule. <br/>**Constraints:** Max length: 50 | - |