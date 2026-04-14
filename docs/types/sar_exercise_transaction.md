### Sar Exercise Transaction

**Description:** _An exercise transaction for a SAR. Supports both stock-settled (resulting in shares) and cash-settled (resulting in a cash payment) outcomes._

**Referenced By (1):**
- [Sar Transaction Item](sar_transaction_item.md)

**References (3):**
- [Decimal](decimal.md)
- [Iso8601 Complete Calendar Date Time](iso8601_complete_calendar_date_time.md)
- [Money](money.md)

**Example:**
```json
{
  "sharesAcquiredDatetime": {
    "value": "2025-03-15T00:00:00Z"
  },
  "quantity": {
    "value": "1000"
  },
  "withheldQuantity": {
    "value": "0"
  },
  "settledQuantity": {
    "value": "1000"
  },
  "resultingSecurityId": "3051",
  "resultingSecurityType": "certificate",
  "resultingSecurityLabel": "CS-55"
}
```

**Properties:**

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| `cashAcquired` | [Money](money.md) | The cash amount received by the holder for a cash-settled exercise. Empty for stock-settled exercises. | - |
| `quantity` | [Decimal](decimal.md) | The number of SAR units exercised. | - |
| `resultingSecurityId` | `STRING` | The identifier of the security produced as a result of a stock-settled exercise. Empty for cash-settled exercises. <br/>**Constraints:** Max length: 50 | - |
| `resultingSecurityLabel` | `STRING` | The human-readable label of the security produced as a result of a stock-settled exercise (e.g. "CS-55"). Empty for cash-settled exercises. <br/>**Constraints:** Max length: 50 | - |
| `resultingSecurityType` | `STRING` | The type of the security produced as a result of a stock-settled exercise (e.g. "certificate"). Empty for cash-settled exercises. <br/>**Constraints:** Max length: 50 | - |
| `settledQuantity` | [Decimal](decimal.md) | The number of shares actually delivered to the holder. Only applicable to stock-settled exercises. | - |
| `sharesAcquiredDatetime` | [Iso8601 Complete Calendar Date Time](iso8601_complete_calendar_date_time.md) | The date and time the shares were acquired (stock-settled) or cash was received (cash-settled). | - |
| `withheldQuantity` | [Decimal](decimal.md) | The number of shares withheld by the issuer to cover tax or other obligations. Only applicable to stock-settled exercises. | - |