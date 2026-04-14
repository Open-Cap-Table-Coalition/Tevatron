### Option Exercise Transaction

**Description:** _An exercise transaction for an option grant. Represents the conversion of options into shares._

**Referenced By (1):**
- [Option Transaction Item](../objects/option_transaction_item.md)

**References (4):**
- [Issuerstransactions Stock Option Type](issuerstransactions_stock_option_type.md)
- [Decimal](decimal.md)
- [Iso8601 Complete Calendar Date Time](iso8601_complete_calendar_date_time.md)
- [Option Exercise Method](option_exercise_method.md)

**Example:**
```json
{
  "id": "23HcT4iVfrgYUaJF9txHTaH",
  "sharesAcquiredDatetime": {
    "value": "2025-01-15T00:00:00Z"
  },
  "quantity": {
    "value": "200"
  },
  "exerciseMethod": "OPTION_EXERCISE_METHOD_CASH",
  "recordType": "STOCK_OPTION_TYPE_ISO",
  "resultingSecurityId": "2951",
  "resultingSecurityType": "certificate",
  "resultingSecurityLabel": "CS-42"
}
```

**Properties:**

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| `exerciseMethod` | [Option Exercise Method](option_exercise_method.md) | How the exercise cost was funded. May be absent if the exercise method could not be determined. See `OptionExerciseMethod` for all supported values. | - |
| `id` | `STRING` | The identifier of the exercise request that initiated the exercise. <br/>**Constraints:** Max length: 50 | - |
| `quantity` | [Decimal](decimal.md) | The number of shares converted as part of exercising the option. | - |
| `recordType` | [Issuerstransactions Stock Option Type](issuerstransactions_stock_option_type.md) | The tax classification of the exercise. May differ from the grant's stock option type (e.g., an ISO grant may have an NSO exercise due to a disqualifying disposition). See `StockOptionType` for all supported values. | - |
| `resultingSecurityId` | `STRING` | The identifier of the security produced as a result of the exercise. <br/>**Constraints:** Max length: 50 | - |
| `resultingSecurityLabel` | `STRING` | The human-readable label of the security produced as a result of the exercise (e.g. "CS-42"). <br/>**Constraints:** Max length: 50 | - |
| `resultingSecurityType` | `STRING` | The type of the security produced as a result of the exercise (e.g. "certificate"). <br/>**Constraints:** Max length: 50 | - |
| `sharesAcquiredDatetime` | [Iso8601 Complete Calendar Date Time](iso8601_complete_calendar_date_time.md) | The date and time the shares were acquired by the beneficial owner. | - |