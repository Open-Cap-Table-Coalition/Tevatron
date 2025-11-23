### Stakeholder Warrant Block Summary

**Description:** _Warrant block summary scoped to a specific stakeholder._

**Referenced By (2):**
- [Issuerscapitalization Stakeholder](issuerscapitalization_stakeholder.md)
- [Stakeholder Group](stakeholder_group.md)

**References (2):**
- [Decimal](decimal.md)
- [Money](money.md)

**Example:**
```json
{
  "warrantBlockId": "1",
  "name": "Series Seed Warrants",
  "shareClassId": "10",
  "fullyDilutedShares": {
    "value": "3029344.00"
  },
  "outstandingWarrants": {
    "value": "3029344.00"
  },
  "cashRaised": {
    "currencyCode": {
      "value": "USD"
    },
    "amount": {
      "value": "1075000.00"
    }
  }
}
```

**Properties:**

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| `cashRaised` | [Money](money.md) | The cash raised across all warrants. | `REQUIRED` |
| `fullyDilutedShares` | [Decimal](decimal.md) | Common share equivalents if all warrants converted to shares. | `REQUIRED` |
| `name` | `STRING` | The name of the warrant block. <br/>**Constraints:** Min length: 1, Max length: 1000 | `REQUIRED` |
| `outstandingWarrants` | [Decimal](decimal.md) | Outstanding warrants quantity. | `REQUIRED` |
| `shareClassId` | `STRING` | The identifier of the share class for this warrant block. <br/>**Constraints:** Min length: 1, Max length: 50 | `REQUIRED` |
| `warrantBlockId` | `STRING` | The identifier of the warrant block. <br/>**Constraints:** Min length: 1, Max length: 50 | `REQUIRED` |