### Rsu Settlement Transaction

**Description:** _A settlement transaction for an RSU award. Represents the conversion of vested units into shares._

**Referenced By (1):**
- [Rsu Transaction Item](rsu_transaction_item.md)

**References (2):**
- [Decimal](decimal.md)
- [Iso8601 Complete Calendar Date Time](iso8601_complete_calendar_date_time.md)

**Example:**
```json
{
  "id": "34JdU5jWgsrhZbKG0uyIUbI",
  "settlementDatetime": {
    "value": "2025-01-15T00:00:00Z"
  },
  "settledQuantity": {
    "value": "700"
  },
  "withheldQuantity": {
    "value": "300"
  },
  "resultingSecurityId": "3051",
  "resultingSecurityType": "certificate",
  "resultingSecurityLabel": "CS-55"
}
```

**Properties:**

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| `id` | `STRING` | The identifier of the settlement transaction. <br/>**Constraints:** Max length: 50 | - |
| `resultingSecurityId` | `STRING` | The identifier of the security produced as a result of the settlement. <br/>**Constraints:** Max length: 50 | - |
| `resultingSecurityLabel` | `STRING` | The human-readable label of the security produced as a result of the settlement (e.g. "CS-55"). <br/>**Constraints:** Max length: 50 | - |
| `resultingSecurityType` | `STRING` | The type of the security produced as a result of the settlement (e.g. "certificate"). <br/>**Constraints:** Max length: 50 | - |
| `settledQuantity` | [Decimal](decimal.md) | The number of shares actually delivered to the holder, net of shares withheld for tax obligations. | - |
| `settlementDatetime` | [Iso8601 Complete Calendar Date Time](iso8601_complete_calendar_date_time.md) | The date and time the units were settled and shares were delivered. | - |
| `withheldQuantity` | [Decimal](decimal.md) | The number of shares withheld by the issuer to cover tax obligations. | - |