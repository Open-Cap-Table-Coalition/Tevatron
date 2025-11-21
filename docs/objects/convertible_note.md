### Convertible Note

**Endpoints:** `GET /v1alpha1/issuers/{issuerId}/convertibleNotes`

**Description:** _A convertible note._

**Example:**
```json
{
  "id": "1",
  "issuerId": "7",
  "stakeholderId": "4903",
  "securityLabel": "CN-3",
  "issueDatetime": {
    "value": "2024-05-24T09:00:00.000000Z"
  },
  "conversionDatetime": {
    "value": "2024-06-24T09:00:00.000000Z"
  },
  "canceledDatetime": {
    "value": "2024-05-24T09:00:00.000000Z"
  },
  "cashPaid": {
    "currencyCode": {
      "value": "USD"
    },
    "amount": {
      "value": "10000.0"
    }
  },
  "maturityDatetime": {
    "value": "2024-05-24T09:00:00.000000Z"
  },
  "interest": {
    "currencyCode": {
      "value": "USD"
    },
    "amount": {
      "value": "50.0"
    }
  },
  "noteBlock": {
    "id": "4",
    "name": "Bridge 2014",
    "prefix": "CN",
    "noteType": "CONVERTIBLE_DEBT",
    "status": "EXECUTED"
  },
  "interestAccrualPeriod": "INTEREST_ACCRUAL_PERIOD_MONTHLY_FIRST_OF_MONTH",
  "interestRate": {
    "value": "3.0"
  },
  "interestCompoundingPeriod": "ANNUALLY",
  "dayCountBasis": "COUNT_ACTUAL_360",
  "priceCap": {
    "currencyCode": {
      "value": "USD"
    },
    "amount": {
      "value": "12000.0"
    }
  },
  "discountPercentage": {
    "value": "0.5"
  },
  "changeInControlPercent": {
    "value": "0.5"
  },
  "conversionTrigger": {
    "currencyCode": {
      "value": "USD"
    },
    "amount": {
      "value": "500.0"
    }
  },
  "canceledQuantity": {
    "value": "500.0"
  }
}
```

**Properties:**
| Property | Type | Description | Required |
| --- | --- | --- | --- |
| `canceledDatetime` | [Iso8601 Complete Calendar Date Time](../types/iso8601_complete_calendar_date_time.md) | The date and time the convertible note was canceled. | - |
| `canceledQuantity` | [Decimal](../types/decimal.md) | The quantity of shares in this convertible note that were canceled | - |
| `cashPaid` | [Money](../types/money.md) | The amount of cash that the stakeholder paid for the convertible note.  For example, if the stakeholder invested $10,000, then $10,000 is the `cash_paid`. This field is also known as `principal`. | `REQUIRED` |
| `changeInControlPercent` | [Decimal](../types/decimal.md) |  Denotes any premium or multiplier applied to the `cash_paid` in the event of a change in control prior to the maturity date. 1 represents 1%. | - |
| `conversionDatetime` | [Iso8601 Complete Calendar Date Time](../types/iso8601_complete_calendar_date_time.md) | The date and time the convertible note was converted to a certificate. | - |
| `conversionTrigger` | [Money](../types/money.md) | For convertibles to convert into the next equity round, terms may be included that specify that the round be of a certain size for the convertible to convert. | - |
| `dayCountBasis` | [Day Count Basis](../types/day_count_basis.md) | The standardized way of counting the number of days between two dates. | `REQUIRED` |
| `discountPercentage` | [Decimal](../types/decimal.md) | The discount applied to the price per share when the note holder will purchase shares in the next fundraising round. 1 represents 1%. | - |
| `id` | `STRING` | The identifier of the convertible note. <br/>**Constraints:** Min length: 1, Max length: 50 | - |
| `interest` | [Money](../types/money.md) | The accrued interest for the convertible note. | `REQUIRED` |
| `interestAccrualPeriod` | [Interest Accrual Period](../types/interest_accrual_period.md) | The length of time over which the interest due to the lender is calculated. | - |
| `interestCompoundingPeriod` | [Interest Compounding Period](../types/interest_compounding_period.md) | The interest compounding period of the convertible note. | `REQUIRED` |
| `interestRate` | [Decimal](../types/decimal.md) | The annual interest rate that the note accrues. | - |
| `issueDatetime` | [Iso8601 Complete Calendar Date Time](../types/iso8601_complete_calendar_date_time.md) | The date and time the convertible note was issued. | `REQUIRED` |
| `issuerId` | `STRING` | The identifier of the issuer owning the convertible note. <br/>**Constraints:** Min length: 1, Max length: 50 | - |
| `maturityDatetime` | [Iso8601 Complete Calendar Date Time](../types/iso8601_complete_calendar_date_time.md) | The date and time on which the convertible note matures.  At maturity, the convertible note's `cash_paid` and `interest` must be paid back if the convertible note hasn't converted into equity. | - |
| `noteBlock` | [Note Block](../types/note_block.md) | The note block associated with the convertible note. | `REQUIRED` |
| `priceCap` | [Money](../types/money.md) | The valuation cap sets a maximum value at which a convertible security will convert into equity in the financing round.  This valuation cap stands regardless of the valuation of the financing round. | - |
| `securityLabel` | `STRING` | The label representing this security (convertible note). <br/>**Constraints:** Min length: 1, Max length: 50 | - |
| `stakeholderId` | `STRING` | The identifier of the stakeholder holding the convertible note. <br/>**Constraints:** Max length: 50 | - |