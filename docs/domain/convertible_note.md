# Convertible Note

A convertible note.

## Endpoints

- `GET /v1alpha1/issuers/{issuerId}/convertibleNotes` — list
- `GET /v1alpha1/issuers/{issuerId}/convertibleNotes/{id}` — single


## Properties

| Property | Type | Required | Description |
|---|---|---|---|
| `id` | string |  | The identifier of the convertible note. |
| `issuerId` | string |  | The identifier of the issuer owning the convertible note. |
| `stakeholderId` | string |  | The identifier of the stakeholder holding the convertible note. |
| `securityLabel` | string |  | The label representing this security (convertible note). |
| `issueDatetime` | [`v1alpha1Iso8601CompleteCalendarDateTime`](../types/iso8601_complete_calendar_date_time.md) | ✓ | The date and time the convertible note was issued. |
| `conversionDatetime` | [`v1alpha1Iso8601CompleteCalendarDateTime`](../types/iso8601_complete_calendar_date_time.md) |  | The date and time the convertible note was converted to a certificate. |
| `canceledDatetime` | [`v1alpha1Iso8601CompleteCalendarDateTime`](../types/iso8601_complete_calendar_date_time.md) |  | The date and time the convertible note was canceled. |
| `cashPaid` | [`v1alpha1Money`](../types/money.md) | ✓ | The amount of cash that the stakeholder paid for the convertible note. For example, if the stakeholder invested $10,000, then $10,000 is the `cash_paid`. This field is also known as `principal`. |
| `maturityDatetime` | [`v1alpha1Iso8601CompleteCalendarDateTime`](../types/iso8601_complete_calendar_date_time.md) |  | The date and time on which the convertible note matures. At maturity, the convertible note's `cash_paid` and `interest` must be paid back if the convertible note hasn't converted into equity. |
| `interest` | [`v1alpha1Money`](../types/money.md) | ✓ | The accrued interest for the convertible note. |
| `noteBlock` | [`v1alpha1NoteBlock`](../types/note_block.md) | ✓ | The note block associated with the convertible note. |
| `interestAccrualPeriod` | [`v1alpha1InterestAccrualPeriod`](../types/interest_accrual_period.md) |  | The length of time over which the interest due to the lender is calculated. |
| `interestRate` | [`v1alpha1Decimal`](../types/decimal.md) |  | The annual interest rate that the note accrues. |
| `interestCompoundingPeriod` | [`v1alpha1InterestCompoundingPeriod`](../types/interest_compounding_period.md) | ✓ | The interest compounding period of the convertible note. |
| `dayCountBasis` | [`v1alpha1DayCountBasis`](../types/day_count_basis.md) | ✓ | The standardized way of counting the number of days between two dates. |
| `priceCap` | [`v1alpha1Money`](../types/money.md) |  | The valuation cap sets a maximum value at which a convertible security will convert into equity in the financing round. This valuation cap stands regardless of the valuation of the financing round. |
| `discountPercentage` | [`v1alpha1Decimal`](../types/decimal.md) |  | The discount applied to the price per share when the note holder will purchase shares in the next fundraising round. 1 represents 1%. |
| `changeInControlPercent` | [`v1alpha1Decimal`](../types/decimal.md) |  | Denotes any premium or multiplier applied to the `cash_paid` in the event of a change in control prior to the maturity date. 1 represents 1%. |
| `conversionTrigger` | [`v1alpha1Money`](../types/money.md) |  | For convertibles to convert into the next equity round, terms may be included that specify that the round be of a certain size for the convertible to convert. |
| `canceledQuantity` | [`v1alpha1Decimal`](../types/decimal.md) |  | The quantity of shares in this convertible note that were canceled |


## Referenced by

_(not embedded in other domain objects)_


---

_Underlying schema: [`v1alpha1ConvertibleNote`](../objects/convertible_note.md)_


[← Back to Domain Index](index.md)
