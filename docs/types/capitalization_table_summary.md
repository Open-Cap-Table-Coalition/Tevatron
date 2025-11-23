### Capitalization Table Summary

**Description:** _Summary information about the capitalization table._

**Referenced By (1):**
- [Capitalization Table](capitalization_table.md)

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
| `cashRaised` | [Money](money.md) | Total currency amount raised. | `REQUIRED` |
| `fullyDilutedShares` | [Decimal](decimal.md) | Total common shares of the company. This includes all outstanding and issued shares, and those that would be included if all options/warrants were exercised. | `REQUIRED` |
| `outstandingShares` | [Decimal](decimal.md) | Undiluted outstanding shares quantity. This is the sum of all `outstandingShares` across all `ShareClassSummary` objects. | `REQUIRED` |