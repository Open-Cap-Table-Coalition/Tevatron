### Share Class Summary

**Description:** _Share class summary includes all certificated, non-certificated and RSAs with an issue date._

**Example:**
```json
{
  "shareClassId": "10",
  "optionPoolIds": [
    "3"
  ],
  "fullyDilutedShares": {
    "value": "5603645.00"
  },
  "outstandingShares": {
    "value": "5603645.00"
  },
  "cashRaised": {
    "currencyCode": {
      "value": "USD"
    },
    "amount": {
      "value": "1159354.84"
    }
  }
}
```

**Properties:**
| Property | Type | Description | Required |
| --- | --- | --- | --- |
| `cashRaised` | [Money](money.md) | Total currency amount raised for share class. | `REQUIRED` |
| `fullyDilutedShares` | [Decimal](decimal.md) | See [this Support article](https://support.carta.com/s/article/authorized-outstanding-issued-fully-diluted-shares) for information on fully diluted shares in a share class. | `REQUIRED` |
| `optionPoolIds` | [`Array` of `STRING`] | List of option pool ids that are associated with this share class. | - |
| `outstandingShares` | [Decimal](decimal.md) | See [this Support article](https://support.carta.com/s/article/authorized-outstanding-issued-fully-diluted-shares) for information on outstanding shares in a share class. | `REQUIRED` |
| `shareClassId` | `STRING` | The identifier of the share class. <br/>**Constraints:** Min length: 1, Max length: 50 | `REQUIRED` |