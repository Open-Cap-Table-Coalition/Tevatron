# Convertible Note

A convertible note.

## OCF Equivalent

Maps to OCF's `ConvertibleIssuance`, plus cancellation/transfer events.


- [`ConvertibleIssuance`](https://open-cap-table-coalition.github.io/Open-Cap-Format-OCF/schema_markdown/schema/objects/transactions/issuance/ConvertibleIssuance/) — _issuance_ tx

**Related:**

- [`ConvertibleCancellation`](https://open-cap-table-coalition.github.io/Open-Cap-Format-OCF/schema_markdown/schema/objects/transactions/cancellation/ConvertibleCancellation/) — _cancellation_ tx
- [`ConvertibleTransfer`](https://open-cap-table-coalition.github.io/Open-Cap-Format-OCF/schema_markdown/schema/objects/transactions/transfer/ConvertibleTransfer/) — _transfer_ tx

## Endpoints

- `GET /v1alpha1/issuers/{issuerId}/convertibleNotes` — list
- `GET /v1alpha1/issuers/{issuerId}/convertibleNotes/{id}` — single


## Shape at a glance

_Quick comparison of field names, types, and required-ness. See the full Carta properties below, or follow the OCF link for full OCF field documentation._

<div class="domain-compare" markdown="1">
<div class="domain-compare__col" markdown="1">
**Carta** — [`v1alpha1ConvertibleNote`](../objects/convertible_note.md)

_A convertible note._

| Property | Type | Req |
|---|---|---|
| `id` | string |  |
| `issuerId` | string |  |
| `stakeholderId` | string |  |
| `securityLabel` | string |  |
| `issueDatetime` | [`v1alpha1Iso8601CompleteCalendarDateTime`](../types/iso8601_complete_calendar_date_time.md) | ✓ |
| `conversionDatetime` | [`v1alpha1Iso8601CompleteCalendarDateTime`](../types/iso8601_complete_calendar_date_time.md) |  |
| `canceledDatetime` | [`v1alpha1Iso8601CompleteCalendarDateTime`](../types/iso8601_complete_calendar_date_time.md) |  |
| `cashPaid` | [`v1alpha1Money`](../types/money.md) | ✓ |
| `maturityDatetime` | [`v1alpha1Iso8601CompleteCalendarDateTime`](../types/iso8601_complete_calendar_date_time.md) |  |
| `interest` | [`v1alpha1Money`](../types/money.md) | ✓ |
| `noteBlock` | [`v1alpha1NoteBlock`](../types/note_block.md) | ✓ |
| `interestAccrualPeriod` | [`v1alpha1InterestAccrualPeriod`](../types/interest_accrual_period.md) |  |
| `interestRate` | [`v1alpha1Decimal`](../types/decimal.md) |  |
| `interestCompoundingPeriod` | [`v1alpha1InterestCompoundingPeriod`](../types/interest_compounding_period.md) | ✓ |
| `dayCountBasis` | [`v1alpha1DayCountBasis`](../types/day_count_basis.md) | ✓ |
| `priceCap` | [`v1alpha1Money`](../types/money.md) |  |
| `discountPercentage` | [`v1alpha1Decimal`](../types/decimal.md) |  |
| `changeInControlPercent` | [`v1alpha1Decimal`](../types/decimal.md) |  |
| `conversionTrigger` | [`v1alpha1Money`](../types/money.md) |  |
| `canceledQuantity` | [`v1alpha1Decimal`](../types/decimal.md) |  |

</div>
<div class="domain-compare__col" markdown="1">
**OCF** — [`ConvertibleIssuance`](https://open-cap-table-coalition.github.io/Open-Cap-Format-OCF/schema_markdown/schema/objects/transactions/issuance/ConvertibleIssuance/)

_Object describing convertible instrument issuance transaction by the issuer and held by a stakeholder_

| Property | Type | Required |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| id | `STRING` | `REQUIRED` |
| comments | [`STRING`] | - |
| object_type | **Constant:** `TX_CONVERTIBLE_ISSUANCE`</br>_Defined in [schema/enums/ObjectType](https://open-cap-table-coalition.github.io/Open-Cap-Format-OCF/schema_markdown/schema/enums/ObjectType/)_ | `REQUIRED` |
| date | [schema/types/Date](https://open-cap-table-coalition.github.io/Open-Cap-Format-OCF/schema_markdown/schema/types/Date/) | `REQUIRED` |
| security_id | `STRING` | `REQUIRED` |
| custom_id | `STRING` | `REQUIRED` |
| stakeholder_id | `STRING` | `REQUIRED` |
| board_approval_date | [schema/types/Date](https://open-cap-table-coalition.github.io/Open-Cap-Format-OCF/schema_markdown/schema/types/Date/) | - |
| stockholder_approval_date | [schema/types/Date](https://open-cap-table-coalition.github.io/Open-Cap-Format-OCF/schema_markdown/schema/types/Date/) | - |
| consideration_text | `STRING` | - |
| security_law_exemptions | [ [schema/types/SecurityExemption](https://open-cap-table-coalition.github.io/Open-Cap-Format-OCF/schema_markdown/schema/types/SecurityExemption/) ] | `REQUIRED` |
| investment_amount | [schema/types/Monetary](https://open-cap-table-coalition.github.io/Open-Cap-Format-OCF/schema_markdown/schema/types/Monetary/) | `REQUIRED` |
| convertible_type | `Enum - Convertible Type`</br></br>_Description:_ Enumeration of convertible instrument types</br></br>**ONE OF:** </br>&bull; NOTE </br>&bull; SAFE </br>&bull; CONVERTIBLE_SECURITY | `REQUIRED` |
| conversion_triggers | **Array of Any Of Following Types/Objs:**</br>&bull; [schema/types/conversion_triggers/AutomaticConversionOnConditionTrigger](https://open-cap-table-coalition.github.io/Open-Cap-Format-OCF/schema_markdown/schema/types/conversion_triggers/AutomaticConversionOnConditionTrigger/)</br>&bull; [schema/types/conversion_triggers/AutomaticConversionOnDateTrigger](https://open-cap-table-coalition.github.io/Open-Cap-Format-OCF/schema_markdown/schema/types/conversion_triggers/AutomaticConversionOnDateTrigger/)</br>&bull; [schema/types/conversion_triggers/ElectiveConversionAtWillTrigger](https://open-cap-table-coalition.github.io/Open-Cap-Format-OCF/schema_markdown/schema/types/conversion_triggers/ElectiveConversionAtWillTrigger/)</br>&bull; [schema/types/conversion_triggers/ElectiveConversionInDateRangeTrigger](https://open-cap-table-coalition.github.io/Open-Cap-Format-OCF/schema_markdown/schema/types/conversion_triggers/ElectiveConversionInDateRangeTrigger/)</br>&bull; [schema/types/conversion_triggers/ElectiveConversionOnConditionTrigger](https://open-cap-table-coalition.github.io/Open-Cap-Format-OCF/schema_markdown/schema/types/conversion_triggers/ElectiveConversionOnConditionTrigger/)</br>&bull; [schema/types/conversion_triggers/UnspecifiedConversionTrigger](https://open-cap-table-coalition.github.io/Open-Cap-Format-OCF/schema_markdown/schema/types/conversion_triggers/UnspecifiedConversionTrigger/) | `REQUIRED` |
| pro_rata | [schema/types/Numeric](https://open-cap-table-coalition.github.io/Open-Cap-Format-OCF/schema_markdown/schema/types/Numeric/) | - |
| seniority | `INTEGER` | `REQUIRED` |
</div>
</div>


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
