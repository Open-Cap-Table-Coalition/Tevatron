### Interest

**Endpoints:** `GET /v1alpha1/issuers/{issuerId}/interests`

**Description:** _Interest information._

**Example:**
```json
{
  "id": "123e4567-e89b-12d3-a456-426614174000",
  "issuerId": "123e4567-e89b-12d3-a456-426614174001",
  "stakeholderId": "123e4567-e89b-12d3-a456-426614174002",
  "interestLabel": "MIU-1",
  "interestTypeName": "Management Incentive Unit",
  "issueDate": {
    "value": "2024-01-01"
  },
  "acceptanceDate": {
    "value": "2024-01-02T00:00:00Z"
  },
  "thresholdDetail": {
    "amount": {
      "value": "1000.0"
    },
    "type": "THRESHOLD_TYPE_PER_UNIT"
  },
  "exercisePrice": {
    "currencyCode": {
      "value": "USD"
    },
    "amount": {
      "value": "50.0"
    }
  },
  "originalIssuePrice": {
    "currencyCode": {
      "value": "USD"
    },
    "amount": {
      "value": "45.0"
    }
  },
  "investedCapital": {
    "currencyCode": {
      "value": "USD"
    },
    "amount": {
      "value": "100.0"
    }
  },
  "accruedValue": {
    "currencyCode": {
      "value": "USD"
    },
    "amount": {
      "value": "200.0"
    }
  },
  "issuedQuantity": {
    "value": "100.0"
  },
  "outstandingQuantity": {
    "value": "100.0"
  },
  "outstandingVestedQuantity": {
    "value": "100.0"
  },
  "exercisedQuantity": {
    "value": "0"
  },
  "repurchasedQuantity": {
    "value": "0"
  },
  "cancelledQuantity": {
    "value": "0"
  },
  "forfeitedQuantity": {
    "value": "0"
  },
  "vestingSchedule": {
    "name": "Standard Vesting",
    "startDate": {
      "value": "2024-01-01"
    }
  }
}
```

**Properties:**
| Property | Type | Description | Required |
| --- | --- | --- | --- |
| `acceptanceDate` | [Iso8601 Complete Calendar Date Time](../types/iso8601_complete_calendar_date_time.md) | The date the interest was accepted by the holder. | - |
| `accruedValue` | [Money](../types/money.md) | Value accrued on principal amount as of the effective date. | - |
| `cancelledQuantity` | [Decimal](../types/decimal.md) | The number of cancelled units. | - |
| `exercisePrice` | [Money](../types/money.md) | The strike price at which units of this interest type can be exercised. | - |
| `exercisedQuantity` | [Decimal](../types/decimal.md) | The number of exercised units. | - |
| `forfeitedQuantity` | [Decimal](../types/decimal.md) | The number of forfeited units. | - |
| `id` | `STRING` | The unique identifier for the interest. | - |
| `interestLabel` | `STRING` | The label of the interest. | - |
| `interestTypeName` | `STRING` | The name of the interest type. | - |
| `investedCapital` | [Money](../types/money.md) | The amount invested by an investor to secure an interest. | - |
| `issueDate` | [Iso8601 Complete Calendar Date](../types/iso8601_complete_calendar_date.md) | The effective date of the interest. | - |
| `issuedQuantity` | [Decimal](../types/decimal.md) | The number of units represented by this interest. | - |
| `issuerId` | `STRING` | The unique identifier for the issuer of the interest. | - |
| `originalIssuePrice` | [Money](../types/money.md) | The price at which units of the interest type were issued. | - |
| `outstandingQuantity` | [Decimal](../types/decimal.md) | The number of outstanding units, units that are 'active' for the interest. | - |
| `outstandingVestedQuantity` | [Decimal](../types/decimal.md) | The number of outstanding vested units. | - |
| `repurchasedQuantity` | [Decimal](../types/decimal.md) | The number of repurchased units. | - |
| `stakeholderId` | `STRING` | The unique identifier for the stakeholder that the interest is issued to. | - |
| `thresholdDetails` | [Threshold Details](../types/threshold_details.md) | Threshold details for the interest. | - |
| `vestingSchedule` | [Vesting Schedule](../types/vesting_schedule.md) | Vesting Schedule for the interest if it has vesting behaviour enabled. | - |