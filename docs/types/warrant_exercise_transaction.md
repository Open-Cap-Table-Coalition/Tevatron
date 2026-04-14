### Warrant Exercise Transaction

**Description:** _An exercise transaction for a warrant. Represents the conversion of warrant rights into shares._

**Referenced By (1):**
- [Warrant Transaction Item](warrant_transaction_item.md)

**References (2):**
- [Decimal](decimal.md)
- [Iso8601 Complete Calendar Date Time](iso8601_complete_calendar_date_time.md)

**Example:**
```json
{
  "sharesAcquiredDatetime": {
    "value": "2025-03-15T00:00:00Z"
  },
  "quantity": {
    "value": "10000"
  },
  "withheldQuantity": {
    "value": "0"
  },
  "settledQuantity": {
    "value": "10000"
  },
  "resultingSecurityId": "3051",
  "resultingSecurityType": "certificate",
  "resultingSecurityLabel": "CS-55"
}
```

**Properties:**

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| `quantity` | [Decimal](decimal.md) | The number of warrant shares exercised. | - |
| `resultingSecurityId` | `STRING` | The identifier of the security produced as a result of the exercise. <br/>**Constraints:** Max length: 50 | - |
| `resultingSecurityLabel` | `STRING` | The human-readable label of the security produced as a result of the exercise (e.g. "CS-55"). <br/>**Constraints:** Max length: 50 | - |
| `resultingSecurityType` | `STRING` | The type of the security produced as a result of the exercise (e.g. "certificate"). <br/>**Constraints:** Max length: 50 | - |
| `settledQuantity` | [Decimal](decimal.md) | The number of shares actually delivered to the holder, net of withheld shares. | - |
| `sharesAcquiredDatetime` | [Iso8601 Complete Calendar Date Time](iso8601_complete_calendar_date_time.md) | The date and time the shares were acquired by the holder. | - |
| `withheldQuantity` | [Decimal](decimal.md) | The number of shares withheld by the issuer to cover tax or other obligations. | - |