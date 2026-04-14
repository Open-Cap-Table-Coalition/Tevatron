# Option Grant

An option grant is a contract that gives an employee the right to purchase a company's stock at a set price.

## OCF Equivalent

Maps to OCF's `EquityCompensationIssuance` (the successor to `PlanSecurityIssuance`
in newer OCF versions). Both represent issuing options from a stock plan to a holder.


- [`EquityCompensationIssuance`](https://open-cap-table-coalition.github.io/Open-Cap-Format-OCF/schema_markdown/schema/objects/transactions/issuance/EquityCompensationIssuance/) — _issuance_ tx

**Related:**

- [`PlanSecurityIssuance`](https://open-cap-table-coalition.github.io/Open-Cap-Format-OCF/schema_markdown/schema/objects/transactions/issuance/PlanSecurityIssuance/) — _issuance_ tx. Predecessor schema retained for backward compatibility.
- [`StockPlan`](https://open-cap-table-coalition.github.io/Open-Cap-Format-OCF/schema_markdown/schema/objects/StockPlan/) — object. The plan the grant draws from.
- [`VestingTerms`](https://open-cap-table-coalition.github.io/Open-Cap-Format-OCF/schema_markdown/schema/objects/VestingTerms/) — object. Carta's grant carries its vesting schedule inline; OCF links to shared `VestingTerms`.

## Endpoints

- `GET /v1alpha1/issuers/{issuerId}/optionGrants` — list
- `GET /v1alpha1/issuers/{issuerId}/optionGrants/{id}` — single


## Shape at a glance

_Quick comparison of field names, types, and required-ness. See the full Carta properties below, or follow the OCF link for full OCF field documentation._

<div class="domain-compare" markdown="1">
<div class="domain-compare__col" markdown="1">
**Carta** — [`v1alpha1OptionGrant`](../objects/option_grant.md)

_An option grant is a contract that gives an employee the right to purchase a company's stock at a set price._

| Property | Type | Req |
|---|---|---|
| `id` | string |  |
| `issuerId` | string |  |
| `stakeholderId` | string |  |
| `equityIncentivePlanName` | string |  |
| `issueDate` | [`v1alpha1Iso8601CompleteCalendarDate`](../types/iso8601_complete_calendar_date.md) |  |
| `vestingStartDate` | [`v1alpha1Iso8601CompleteCalendarDate`](../types/iso8601_complete_calendar_date.md) |  |
| `boardApprovalDate` | [`v1alpha1Iso8601CompleteCalendarDate`](../types/iso8601_complete_calendar_date.md) |  |
| `stakeholderAcceptanceDate` | [`v1alpha1Iso8601CompleteCalendarDate`](../types/iso8601_complete_calendar_date.md) |  |
| `canceledDate` | [`v1alpha1Iso8601CompleteCalendarDate`](../types/iso8601_complete_calendar_date.md) |  |
| `grantExpirationDate` | [`v1alpha1Iso8601CompleteCalendarDate`](../types/iso8601_complete_calendar_date.md) |  |
| `lastExercisableDate` | [`v1alpha1Iso8601CompleteCalendarDate`](../types/iso8601_complete_calendar_date.md) |  |
| `disqualificationDate` | [`v1alpha1Iso8601CompleteCalendarDate`](../types/iso8601_complete_calendar_date.md) |  |
| `isoNsoSplit` | boolean |  |
| `stockOptionType` | [`issuerssecuritiesv1alpha1StockOptionType`](../types/issuerssecurities_stock_option_type.md) |  |
| `quantity` | [`v1alpha1Decimal`](../types/decimal.md) |  |
| `outstandingQuantity` | [`v1alpha1Decimal`](../types/decimal.md) |  |
| `vestedQuantity` | [`v1alpha1Decimal`](../types/decimal.md) |  |
| `exercisedQuantity` | [`v1alpha1Decimal`](../types/decimal.md) |  |
| `exercisePrice` | [`v1alpha1Money`](../types/money.md) |  |
| `securityLabel` | string |  |
| `earlyExercisable` | boolean |  |
| `vestingEvents` | [`v1alpha1OptionGrantVestingEvent`](../types/option_grant_vesting_event.md)[] |  |
| `exercises` | [`v1alpha1Exercise`](../types/exercise.md)[] |  |
| `terminationDate` | [`v1alpha1Iso8601CompleteCalendarDate`](../types/iso8601_complete_calendar_date.md) |  |
| `vestingSchedule` | [`issuerssecuritiesv1alpha1VestingSchedule`](../types/issuerssecurities_vesting_schedule.md) |  |
| `canceledQuantity` | [`v1alpha1Decimal`](../types/decimal.md) |  |
| `forfeitedQuantity` | [`v1alpha1Decimal`](../types/decimal.md) |  |
| `expiredQuantity` | [`v1alpha1Decimal`](../types/decimal.md) |  |
| `returnedToPoolQuantity` | [`v1alpha1Decimal`](../types/decimal.md) |  |
| `returnedToTreasuryQuantity` | [`v1alpha1Decimal`](../types/decimal.md) |  |
| `lastModifiedDatetime` | [`v1alpha1Iso8601CompleteCalendarDateTime`](../types/iso8601_complete_calendar_date_time.md) |  |
| `exercisePeriods` | [`issuerssecuritiesv1alpha1ExercisePeriods`](../types/issuerssecurities_exercise_periods.md) |  |

</div>
<div class="domain-compare__col" markdown="1">
**OCF** — [`EquityCompensationIssuance`](https://open-cap-table-coalition.github.io/Open-Cap-Format-OCF/schema_markdown/schema/objects/transactions/issuance/EquityCompensationIssuance/)

_Object describing securities issuance transaction by the issuer and held by a stakeholder as a form of compensation (as noted elsewhere, RSAs are not included here intentionally and should be modelled using Stock Issuances)._

| Property | Type | Required |
| ---------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| id | `STRING` | `REQUIRED` |
| comments | [`STRING`] | - |
| object_type | **Constants (Backwards Compatibility):** `TX_PLAN_SECURITY_ISSUANCE, TX_EQUITY_COMPENSATION_ISSUANCE`</br>_Defined in [schema/enums/ObjectType](https://open-cap-table-coalition.github.io/Open-Cap-Format-OCF/schema_markdown/schema/enums/ObjectType/)_ | `REQUIRED` |
| date | [schema/types/Date](https://open-cap-table-coalition.github.io/Open-Cap-Format-OCF/schema_markdown/schema/types/Date/) | `REQUIRED` |
| security_id | `STRING` | `REQUIRED` |
| custom_id | `STRING` | `REQUIRED` |
| stakeholder_id | `STRING` | `REQUIRED` |
| board_approval_date | [schema/types/Date](https://open-cap-table-coalition.github.io/Open-Cap-Format-OCF/schema_markdown/schema/types/Date/) | - |
| stockholder_approval_date | [schema/types/Date](https://open-cap-table-coalition.github.io/Open-Cap-Format-OCF/schema_markdown/schema/types/Date/) | - |
| consideration_text | `STRING` | - |
| security_law_exemptions | [ [schema/types/SecurityExemption](https://open-cap-table-coalition.github.io/Open-Cap-Format-OCF/schema_markdown/schema/types/SecurityExemption/) ] | `REQUIRED` |
| stock_plan_id | `STRING` | - |
| stock_class_id | `STRING` | - |
| compensation_type | `Enum - Compensation Type`</br></br>_Description:_ Enumeration of equity compensation types (there are some things around the margins like RSAs that don't currently fit under the EquityCompensation umbrella but might arguably fall under this. If you want to create an RSA, create a stock issuance with vesting - you can link it to a plan as well, if you want).</br></br>**The enums stand for:**</br>1. OPTION_ISO (qualified)</br>2. OPTION_NSO (non-qualified)</br>3. OPTION (not NSO or ISO)</br>4. RSU (restricted share units)</br>5. CSAR(cash-settled stock appreciation rights)</br>6. SSAR(stock-settled stock appreciation rights)</br></br>**ONE OF:** </br>&bull; OPTION_NSO </br>&bull; OPTION_ISO </br>&bull; OPTION </br>&bull; RSU </br>&bull; CSAR </br>&bull; SSAR | `REQUIRED` |
| option_grant_type | `Enum - Option Type`</br></br>_Description:_ Enumeration of option types</br></br>**ONE OF:** </br>&bull; NSO </br>&bull; ISO </br>&bull; INTL | - |
| quantity | [schema/types/Numeric](https://open-cap-table-coalition.github.io/Open-Cap-Format-OCF/schema_markdown/schema/types/Numeric/) | `REQUIRED` |
| exercise_price | [schema/types/Monetary](https://open-cap-table-coalition.github.io/Open-Cap-Format-OCF/schema_markdown/schema/types/Monetary/) | - |
| base_price | [schema/types/Monetary](https://open-cap-table-coalition.github.io/Open-Cap-Format-OCF/schema_markdown/schema/types/Monetary/) | - |
| early_exercisable | `BOOLEAN` | - |
| vesting_terms_id | `STRING` | - |
| vestings | [ [schema/types/Vesting](https://open-cap-table-coalition.github.io/Open-Cap-Format-OCF/schema_markdown/schema/types/Vesting/) ] | - |
| expiration_date | **ONE OF the Following Types/Objs:**</br>&bull; `NULL` _()_</br>&bull; [schema/types/Date](https://open-cap-table-coalition.github.io/Open-Cap-Format-OCF/schema_markdown/schema/types/Date/) | `REQUIRED` |
| termination_exercise_windows | [ [schema/types/TerminationWindow](https://open-cap-table-coalition.github.io/Open-Cap-Format-OCF/schema_markdown/schema/types/TerminationWindow/) ] | `REQUIRED` |
</div>
</div>


## Properties

| Property | Type | Required | Description |
|---|---|---|---|
| `id` | string |  | The identifier of the option grant. |
| `issuerId` | string |  | The identifier of the issuer that issued the option grant. |
| `stakeholderId` | string |  | The identifier of the stakeholder that holds the option grant. |
| `equityIncentivePlanName` | string |  | The name of the equity incentive plan (i.e., option plan) associated with this option grant. |
| `issueDate` | [`v1alpha1Iso8601CompleteCalendarDate`](../types/iso8601_complete_calendar_date.md) |  | The date the option grant was issued. |
| `vestingStartDate` | [`v1alpha1Iso8601CompleteCalendarDate`](../types/iso8601_complete_calendar_date.md) |  | The date the option grant began vesting. |
| `boardApprovalDate` | [`v1alpha1Iso8601CompleteCalendarDate`](../types/iso8601_complete_calendar_date.md) |  | The date the option grant received board approval. |
| `stakeholderAcceptanceDate` | [`v1alpha1Iso8601CompleteCalendarDate`](../types/iso8601_complete_calendar_date.md) |  | The date the option grant was accepted by the stakeholder. |
| `canceledDate` | [`v1alpha1Iso8601CompleteCalendarDate`](../types/iso8601_complete_calendar_date.md) |  | The date when this option grant was canceled. |
| `grantExpirationDate` | [`v1alpha1Iso8601CompleteCalendarDate`](../types/iso8601_complete_calendar_date.md) |  | The expiration date of the option grant (commonly 10 years from the grant issuance date). |
| `lastExercisableDate` | [`v1alpha1Iso8601CompleteCalendarDate`](../types/iso8601_complete_calendar_date.md) |  | The last date the stakeholder can exercise the option grant. |
| `disqualificationDate` | [`v1alpha1Iso8601CompleteCalendarDate`](../types/iso8601_complete_calendar_date.md) |  | The date this option grant became disqualified. |
| `isoNsoSplit` | boolean |  | True if the grant has ISO/NSO split. False otherwise. Learn more about [the ISO $100K limit and ISO/NSO splits](https://support.carta.com/s/article/100k-rule). |
| `stockOptionType` | [`issuerssecuritiesv1alpha1StockOptionType`](../types/issuerssecurities_stock_option_type.md) |  | The stock option type at time of issuance. For grants issued as ISO that subsequently failed to meet ISO qualifications, the type will remain ISO. Refer to the disqualification date for information regarding the disqualification of the grant's ISO shares. |
| `quantity` | [`v1alpha1Decimal`](../types/decimal.md) |  | The total number of options in the grant. |
| `outstandingQuantity` | [`v1alpha1Decimal`](../types/decimal.md) |  | The total quantity of stock options from this grant that have not been exercised, expired, forfeited, or canceled |
| `vestedQuantity` | [`v1alpha1Decimal`](../types/decimal.md) |  | The total quantity of stock options from this grant that have vested. |
| `exercisedQuantity` | [`v1alpha1Decimal`](../types/decimal.md) |  | The total quantity of stock options from this grant that have been exercised into shares. |
| `exercisePrice` | [`v1alpha1Money`](../types/money.md) |  | The exercise price of the options in the grant. |
| `securityLabel` | string |  | The label representing this security (option grant). |
| `earlyExercisable` | boolean |  | True if the option grant is eligible for early exercising; false if the option grant is not eligible for early exercising. |
| `vestingEvents` | [`v1alpha1OptionGrantVestingEvent`](../types/option_grant_vesting_event.md)[] |  | The list of all vesting events associated with this grant. For time based vesting events, both past and future vesting details will be available. For performance and milestone based vesting, only achieved vesting events will be available. |
| `exercises` | [`v1alpha1Exercise`](../types/exercise.md)[] |  | The list of all exercises associated with this grant. |
| `terminationDate` | [`v1alpha1Iso8601CompleteCalendarDate`](../types/iso8601_complete_calendar_date.md) |  | The date that the option grant was terminated. This commonly matches the date the company's relationship with the stakeholder was terminated. |
| `vestingSchedule` | [`issuerssecuritiesv1alpha1VestingSchedule`](../types/issuerssecurities_vesting_schedule.md) |  | The vesting schedule information associated with the restricted stock award. |
| `canceledQuantity` | [`v1alpha1Decimal`](../types/decimal.md) |  | The number of options in the grant that were canceled. |
| `forfeitedQuantity` | [`v1alpha1Decimal`](../types/decimal.md) |  | The number of options in the grant that were forfeited. |
| `expiredQuantity` | [`v1alpha1Decimal`](../types/decimal.md) |  | The number of options in the grant that expired. |
| `returnedToPoolQuantity` | [`v1alpha1Decimal`](../types/decimal.md) |  | The number of options in the grant that were returned to the pool. |
| `returnedToTreasuryQuantity` | [`v1alpha1Decimal`](../types/decimal.md) |  | The number of options in the grant that were annulled, but not returned to the pool. |
| `lastModifiedDatetime` | [`v1alpha1Iso8601CompleteCalendarDateTime`](../types/iso8601_complete_calendar_date_time.md) |  | The date and time when the option grant was last modified. |
| `exercisePeriods` | [`issuerssecuritiesv1alpha1ExercisePeriods`](../types/issuerssecurities_exercise_periods.md) |  | The exercise periods for the option grant. Unset values within this field will be inherited from the equity plan from with the option was granted. |


## Referenced by

_(not embedded in other domain objects)_


---

_Underlying schema: [`v1alpha1OptionGrant`](../objects/option_grant.md)_


[← Back to Domain Index](index.md)
