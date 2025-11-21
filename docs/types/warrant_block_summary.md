### Warrant Block Summary

**Description:** _Warrant block summary._

**Example:**
```json
{
  "warrantBlockId": "1",
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
| `cashRaised` | [Money](money.md) | The cash raised for the warrants. | `REQUIRED` |
| `fullyDilutedShares` | [Decimal](decimal.md) | Number of shares if all warrants converted to shares. | `REQUIRED` |
| `outstandingWarrants` | [Decimal](decimal.md) | Outstanding warrants quantity. | `REQUIRED` |
| `shareClassId` | `STRING` | The identifier of the share class for this warrant block. <br/>**Constraints:** Min length: 1, Max length: 50 | `REQUIRED` |
| `warrantBlockId` | `STRING` | The identifier of the warrant block. <br/>**Constraints:** Min length: 1, Max length: 50 | `REQUIRED` |