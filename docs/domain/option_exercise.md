# Option Exercise

An option exercise is an event representing a stakeholder exercising their right to purchase shares of an issuer at a set price, the strike price, defined in the option grant being exercised. The result of a successfully completed exercise is the issuance of a certificate.

## OCF Equivalent

Maps to OCF's `EquityCompensationExercise` (or legacy `PlanSecurityExercise`).


- [`EquityCompensationExercise`](https://open-cap-table-coalition.github.io/Open-Cap-Format-OCF/schema_markdown/schema/objects/transactions/exercise/EquityCompensationExercise/) — _exercise_ tx

**Related:**

- [`PlanSecurityExercise`](https://open-cap-table-coalition.github.io/Open-Cap-Format-OCF/schema_markdown/schema/objects/transactions/exercise/PlanSecurityExercise/) — _exercise_ tx. Predecessor schema retained for backward compatibility.

## Endpoints

- `GET /v1alpha1/issuers/{issuerId}/optionExercises` — list


## Shape at a glance

_Quick comparison of field names, types, and required-ness. See the full Carta properties below, or follow the OCF link for full OCF field documentation._

<div class="domain-compare" markdown="1">
<div class="domain-compare__col" markdown="1">
**Carta** — [`v1alpha1OptionExercise`](../objects/option_exercise.md)

_An option exercise is an event representing a stakeholder exercising their right to purchase shares of an issuer at a set price, the strike price, defined in the option grant being exercised. The result of a successfully completed exercise is the issuance of a certificate._

| Property | Type | Req |
|---|---|---|
| `id` | string |  |
| `issuerId` | string |  |
| `stakeholderId` | string |  |
| `optionGrantId` | string |  |
| `certificateId` | string |  |
| `quantity` | [`v1alpha1Decimal`](../types/decimal.md) |  |
| `exerciseTime` | [`v1alpha1Iso8601CompleteCalendarDateTime`](../types/iso8601_complete_calendar_date_time.md) |  |
| `state` | [`v1alpha1OptionExerciseState`](../types/option_exercise_state.md) |  |
| `exerciseType` | [`v1alpha1OptionExerciseType`](../types/option_exercise_type.md) |  |
| `recordType` | [`securitiesoptionexercisesv1alpha1StockOptionType`](../types/securitiesoptionexercises_stock_option_type.md) |  |
| `taxWithholding` | [`v1alpha1OptionExerciseTaxWithholdingLineItem`](../types/option_exercise_tax_withholding_line_item.md)[] |  |
| `moneyMovement` | [`v1alpha1OptionExerciseMoneyMovement`](../types/option_exercise_money_movement.md) |  |

</div>
<div class="domain-compare__col" markdown="1">
**OCF** — [`EquityCompensationExercise`](https://open-cap-table-coalition.github.io/Open-Cap-Format-OCF/schema_markdown/schema/objects/transactions/exercise/EquityCompensationExercise/)

_Object describing equity compensation exercise transaction_

| Property | Type | Required |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------- |
| id | `STRING` | `REQUIRED` |
| comments | [`STRING`] | - |
| object_type | **Constants (Backwards Compatibility):** `TX_PLAN_SECURITY_EXERCISE, TX_EQUITY_COMPENSATION_EXERCISE`</br>_Defined in [schema/enums/ObjectType](https://open-cap-table-coalition.github.io/Open-Cap-Format-OCF/schema_markdown/schema/enums/ObjectType/)_ | `REQUIRED` |
| date | [schema/types/Date](https://open-cap-table-coalition.github.io/Open-Cap-Format-OCF/schema_markdown/schema/types/Date/) | `REQUIRED` |
| security_id | `STRING` | `REQUIRED` |
| consideration_text | `STRING` | - |
| resulting_security_ids | [`STRING`] | `REQUIRED` |
| quantity | [schema/types/Numeric](https://open-cap-table-coalition.github.io/Open-Cap-Format-OCF/schema_markdown/schema/types/Numeric/) | `REQUIRED` |
</div>
</div>


## Properties

| Property | Type | Required | Description |
|---|---|---|---|
| `id` | string |  | The identifier of the option exercise. Note: It is possible for this ID to not exist for legacy reasons, in which case the value of this field will be `"NO_ID"` |
| `issuerId` | string |  | The identifier of the issuer that issued the option grant. |
| `stakeholderId` | string |  | The identifier of the stakeholder that holds the option grant being exercised. |
| `optionGrantId` | string |  | The identifier of the option grant being exercised. |
| `certificateId` | string |  | The identifier of the certificate issued as a result of the option exercise event completing. |
| `quantity` | [`v1alpha1Decimal`](../types/decimal.md) |  | The number of shares being exercised from the related option grant. |
| `exerciseTime` | [`v1alpha1Iso8601CompleteCalendarDateTime`](../types/iso8601_complete_calendar_date_time.md) |  | The date and time in which the option exercise request was initiated. |
| `state` | [`v1alpha1OptionExerciseState`](../types/option_exercise_state.md) |  | The current state of the exercise request. |
| `exerciseType` | [`v1alpha1OptionExerciseType`](../types/option_exercise_type.md) |  | The type of option exercise being requested. |
| `recordType` | [`securitiesoptionexercisesv1alpha1StockOptionType`](../types/securitiesoptionexercises_stock_option_type.md) |  | The type of the record associated with the option exercise. |
| `taxWithholding` | [`v1alpha1OptionExerciseTaxWithholdingLineItem`](../types/option_exercise_tax_withholding_line_item.md)[] |  | The tax withholding information associated with the option exercise. |
| `moneyMovement` | [`v1alpha1OptionExerciseMoneyMovement`](../types/option_exercise_money_movement.md) |  | The money movement information associated with the option exercise. |


## Referenced by

_(not embedded in other domain objects)_


---

_Underlying schema: [`v1alpha1OptionExercise`](../objects/option_exercise.md)_


[← Back to Domain Index](index.md)
