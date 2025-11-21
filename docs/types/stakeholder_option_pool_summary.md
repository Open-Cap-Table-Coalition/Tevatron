### Stakeholder Option Pool Summary

**Description:** _Option pool summary scoped to a specific stakeholder._

**Example:**
```json
{
  "optionPoolId": "3",
  "name": "Equity Incentive Plan",
  "shareClassId": "10",
  "outstandingEquityAwardDerivatives": {
    "value": "3725634.0"
  },
  "outstandingCommittedRestrictedStockAwards": {
    "value": "0"
  }
}
```

**Properties:**
| Property | Type | Description | Required |
| --- | --- | --- | --- |
| `name` | `STRING` | The name of the option pool. <br/>**Constraints:** Min length: 1, Max length: 100 | `REQUIRED` |
| `optionPoolId` | `STRING` | The identifier of the option pool. <br/>**Constraints:** Min length: 1, Max length: 50 | `REQUIRED` |
| `outstandingCommittedRestrictedStockAwards` | [Decimal](decimal.md) | Board approved but unissued Restricted Stock Awards (RSAs). | `REQUIRED` |
| `outstandingEquityAwardDerivatives` | [Decimal](decimal.md) | Outstanding equity award derivatives. This includes:  - Option Grants  - Restricted Stock Units (RSUs)  - Stock Appreciation Rights (SARs)  - Cash Bonus Unit (CBUs)  - International equity awards | `REQUIRED` |
| `shareClassId` | `STRING` | The identifier of the share class used by the option pool to issue equity. <br/>**Constraints:** Min length: 1, Max length: 50 | `REQUIRED` |