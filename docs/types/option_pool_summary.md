### Option Pool Summary

**Description:** _Option pool summary._

**Example:**
```json
{
  "optionPoolId": "3",
  "shareClassId": "9",
  "fullyDilutedShares": {
    "value": "44871088.00"
  },
  "outstandingEquityAwardDerivatives": {
    "value": "3725634.0"
  },
  "outstandingCommittedRestrictedStockAwards": {
    "value": "0"
  },
  "name": "Employee Option Pool",
  "authorizedShares": {
    "value": "44871088.00"
  }
}
```

**Properties:**
| Property | Type | Description | Required |
| --- | --- | --- | --- |
| `authorizedShares` | [Decimal](decimal.md) | The amount of shares authorized to be issued from the option pool. | `REQUIRED` |
| `fullyDilutedShares` | [Decimal](decimal.md) | Total common shares of an option pool if all outstanding grants and available equity in the option pool were exercised. | `REQUIRED` |
| `name` | `STRING` | The name of the option pool. <br/>**Constraints:** Min length: 1, Max length: 100 | `REQUIRED` |
| `optionPoolId` | `STRING` | The identifier of the option pool. <br/>**Constraints:** Min length: 1, Max length: 50 | `REQUIRED` |
| `outstandingCommittedRestrictedStockAwards` | [Decimal](decimal.md) | Board approved but unissued Restricted Stock Awards (RSAs). | `REQUIRED` |
| `outstandingEquityAwardDerivatives` | [Decimal](decimal.md) | Outstanding equity award derivatives. This includes:  - Option Grants  - Restricted Stock Units (RSU)  - Stock Appreciation Rights (SAR)  - Cash Bonus Unit (CBU)  - International equity awards | `REQUIRED` |
| `shareClassId` | `STRING` | The identifier of the share class used by the option pool to issue equity. <br/>**Constraints:** Min length: 1, Max length: 50 | `REQUIRED` |
| `terminatedDatetime` | [Iso8601 Complete Calendar Date Time](iso8601_complete_calendar_date_time.md) | The timestamp when the option pool was terminated. | - |