### Stakeholder Share Class Summary

**Description:** _Share class summary scoped to a specific stakeholder. This includes all certificated, non-certificated and RSAs with an issue date._

**Referenced By (2):**
- [Issuerscapitalization Stakeholder](issuerscapitalization_stakeholder.md)
- [Stakeholder Group](stakeholder_group.md)

**References (2):**
- [Decimal](decimal.md)
- [Money](money.md)

**Example:**
```json
{
  "shareClassId": "10",
  "name": "Common",
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
| `fullyDilutedShares` | [Decimal](decimal.md) | The fully diluted certificated shares for the share class. See [this Support article](https://support.carta.com/s/article/authorized-outstanding-issued-fully-diluted-shares) for information on fully diluted shares in a share class. | `REQUIRED` |
| `name` | `STRING` | The name of the share class. <br/>**Constraints:** Min length: 1, Max length: 1000 | `REQUIRED` |
| `outstandingShares` | [Decimal](decimal.md) | The total outstanding certificates in the share class. See [this Support article](https://support.carta.com/s/article/authorized-outstanding-issued-fully-diluted-shares) for information on outstanding shares in a share class. | `REQUIRED` |
| `shareClassId` | `STRING` | The identifier of the share class. <br/>**Constraints:** Min length: 1, Max length: 50 | `REQUIRED` |