### Stakeholder Capitalization Table Summary

**Description:** _Summary information about the capitalization table._

**Referenced By (2):**
- [Issuerscapitalization Stakeholder](issuerscapitalization_stakeholder.md)
- [Stakeholder Group](stakeholder_group.md)

**References (2):**
- [Decimal](decimal.md)
- [Money](money.md)

**Example:**
```json
{
  "fullyDilutedShares": {
    "value": "61399310.00"
  },
  "outstandingShares": {
    "value": "16328224.00"
  },
  "cashRaised": {
    "currencyCode": {
      "value": "USD"
    },
    "amount": {
      "value": "20261050.79"
    }
  }
}
```

**Properties:**

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| `cashRaised` | [Money](money.md) | Total cash amount raised. | `REQUIRED` |
| `fullyDilutedShares` | [Decimal](decimal.md) | Total common share equivalent of the company for this stakeholder. This includes all outstanding and issued shares, and those that would be included if all options and warrants were exercised. | `REQUIRED` |
| `outstandingShares` | [Decimal](decimal.md) | Undiluted outstanding shares quantity. This is the sum of all `outstandingShares` across all `ShareClassSummary` objects. | `REQUIRED` |