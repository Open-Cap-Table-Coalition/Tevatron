### Convertible Transaction Item

**Description:** _A convertible note with its full transaction history. Groups all lifecycle events (issuance, cancellation) for a single convertible note._

**Referenced By (1):**
- [List Transactions Response](list_transactions_response.md)

**References (2):**
- [Convertible Cancellation Transaction](convertible_cancellation_transaction.md)
- [Convertible Issuance Transaction](convertible_issuance_transaction.md)

**Example:**
```json
{
  "securityId": "4501",
  "stakeholderId": "4923",
  "securityLabel": "CN-3",
  "issuance": {
    "issueDatetime": {
      "value": "2024-01-15T00:00:00Z"
    },
    "principal": {
      "currencyCode": {
        "value": "USD"
      },
      "amount": {
        "value": "500000"
      }
    },
    "valuationCap": {
      "currencyCode": {
        "value": "USD"
      },
      "amount": {
        "value": "10000000"
      }
    },
    "discountPercentage": {
      "value": "20"
    },
    "conversionTrigger": {
      "currencyCode": {
        "value": "USD"
      },
      "amount": {
        "value": "1000000"
      }
    },
    "maturityDatetime": {
      "value": "2026-01-15T00:00:00Z"
    },
    "noteBlockId": "42",
    "interestRate": {
      "value": "5.0"
    },
    "interestAccrualPeriod": "CONVERTIBLE_INTEREST_ACCRUAL_PERIOD_MONTHLY",
    "interestCompoundingPeriod": "CONVERTIBLE_INTEREST_COMPOUNDING_PERIOD_SIMPLE",
    "dayCountBasis": "CONVERTIBLE_DAY_COUNT_BASIS_COUNT_ACTUAL_365"
  },
  "cancellations": [
    {
      "effectiveDatetime": {
        "value": "2025-10-02T00:00:00Z"
      },
      "reason": "CONVERTIBLE_CANCELLATION_REASON_CONVERTED",
      "principal": {
        "currencyCode": {
          "value": "USD"
        },
        "amount": {
          "value": "500000"
        }
      }
    }
  ]
}
```

**Properties:**

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| `cancellations` | [`Array` of [Convertible Cancellation Transaction](convertible_cancellation_transaction.md)] | All cancellation transactions for the convertible note, in chronological order. | - |
| `issuance` | [Convertible Issuance Transaction](convertible_issuance_transaction.md) | The issuance transaction for the convertible note. | - |
| `securityId` | `STRING` | The identifier of the convertible note. <br/>**Constraints:** Max length: 50 | - |
| `securityLabel` | `STRING` | The human-readable label for the convertible note (e.g. "CN-3"). <br/>**Constraints:** Max length: 50 | - |
| `stakeholderId` | `STRING` | The identifier of the current holder of the convertible note. <br/>**Constraints:** Max length: 50 | - |