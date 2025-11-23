### Restricted Stock Unit Settlement

**Description:** _Restricted stock unit settlement information._

**Referenced By (1):**
- [Restricted Stock Unit](../objects/restricted_stock_unit.md)

**References (3):**
- [Decimal](decimal.md)
- [Iso8601 Complete Calendar Date](iso8601_complete_calendar_date.md)
- [Money](money.md)

**Example:**
```json
{
  "settlementDate": {
    "value": "2016-08-19"
  },
  "releaseQuantity": {
    "value": "200"
  },
  "saleQuantity": {
    "value": "200"
  },
  "withholdingQuantity": {
    "value": "55"
  },
  "netSettlementQuantity": {
    "value": "145"
  },
  "settlementPrice": {
    "currencyCode": {
      "value": "USD"
    },
    "amount": {
      "value": "0.78"
    }
  },
  "certificateId": "78",
  "certificateLabel": "CS-124"
}
```

**Properties:**

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| `certificateId` | `STRING` | The resource identifier for the certificate that was generated as part of the transaction. <br/>**Constraints:** Min length: 1, Max length: 1000 | - |
| `certificateLabel` | `STRING` | The label of the certificate that was generated as part of the transaction (e.g. CS-107). | - |
| `netSettlementQuantity` | [Decimal](decimal.md) | The net quantity settled after quantities are sold or withheld. | - |
| `releaseQuantity` | [Decimal](decimal.md) | The quantity released during the settlement. | - |
| `saleQuantity` | [Decimal](decimal.md) | The quantity sold in a cashless transaction to cover the cost of the settlement. | - |
| `settlementDate` | [Iso8601 Complete Calendar Date](iso8601_complete_calendar_date.md) | The date of the settlement. | - |
| `settlementPrice` | [Money](money.md) | The price to settle one unit of the RSU. | - |
| `withholdingQuantity` | [Decimal](decimal.md) | The quantity withheld during the settlement. | - |