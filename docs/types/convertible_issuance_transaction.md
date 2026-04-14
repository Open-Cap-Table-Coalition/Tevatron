### Convertible Issuance Transaction

**Description:** _The issuance transaction for a convertible note. Represents the initial issuance of the note._

**Referenced By (1):**
- [Convertible Transaction Item](convertible_transaction_item.md)

**References (6):**
- [Convertible Day Count Basis](convertible_day_count_basis.md)
- [Convertible Interest Accrual Period](convertible_interest_accrual_period.md)
- [Convertible Interest Compounding Period](convertible_interest_compounding_period.md)
- [Decimal](decimal.md)
- [Iso8601 Complete Calendar Date Time](iso8601_complete_calendar_date_time.md)
- [Money](money.md)

**Example:**
```json
{
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
}
```

**Properties:**

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| `conversionTrigger` | [Money](money.md) | The qualifying financing threshold that triggers automatic conversion. May be absent if no conversion trigger was set. | - |
| `dayCountBasis` | [Convertible Day Count Basis](convertible_day_count_basis.md) | The standardized way of counting the number of days between two dates. | - |
| `discountPercentage` | [Decimal](decimal.md) | The discount percentage applied at conversion, expressed as a percentage (e.g., `20` for a 20% discount). May be absent if no discount was set. | - |
| `interestAccrualPeriod` | [Convertible Interest Accrual Period](convertible_interest_accrual_period.md) | The length of time over which the interest due to the lender is calculated. | - |
| `interestCompoundingPeriod` | [Convertible Interest Compounding Period](convertible_interest_compounding_period.md) | The interest compounding period of the convertible note. | - |
| `interestRate` | [Decimal](decimal.md) | The annual interest rate that the convertible note accrues, expressed as a percentage (e.g., `5` for 5%). May be absent if no interest rate was set. | - |
| `issueDatetime` | [Iso8601 Complete Calendar Date Time](iso8601_complete_calendar_date_time.md) | The date and time the convertible note was issued. | - |
| `maturityDatetime` | [Iso8601 Complete Calendar Date Time](iso8601_complete_calendar_date_time.md) | The maturity date and time of the convertible note. May be absent if no maturity date was set. | - |
| `noteBlockId` | `STRING` | The identifier of the note block from which the convertible note was issued. <br/>**Constraints:** Max length: 50 | - |
| `precededBySecurityId` | `STRING` | The identifier of the security that preceded this convertible note (e.g. the note that was transferred). May be absent if the note was issued directly. <br/>**Constraints:** Max length: 50 | - |
| `principal` | [Money](money.md) | The principal amount of the convertible note. | - |
| `valuationCap` | [Money](money.md) | The valuation cap for conversion. May be absent if no cap was set. | - |