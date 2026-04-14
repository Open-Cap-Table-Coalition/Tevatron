# Draft Option Grant

A draft option grant is an object that is the precursor of an option grant before it is approved, signed, and issued. The "draft" prefix is used to differentiate it from the final option grant object.

## OCF Equivalent

OCF has no "draft" state for equity grants — it only models finalized transactions.
A Carta draft maps to a pending `EquityCompensationIssuance` that hasn't been committed.


- [`EquityCompensationIssuance`](https://open-cap-table-coalition.github.io/Open-Cap-Format-OCF/schema_markdown/schema/objects/transactions/issuance/EquityCompensationIssuance/) — _issuance_ tx. OCF models only finalized grants; there is no "draft" equivalent.

## Endpoints

- `POST /v1alpha1/issuers/{issuerId}/draftOptionGrantSets/{draftOptionGrantSetId}/draftOptionGrants` — single _(request body)_
- `POST /v1alpha1/issuers/{issuerId}/draftOptionGrantSets/{draftOptionGrantSetId}/draftOptionGrants` — single
- `GET /v1alpha1/issuers/{issuerId}/draftOptionGrantSets/{draftOptionGrantSetId}/draftOptionGrants/{draftOptionGrantId}` — single


## Shape at a glance

_Quick comparison of field names, types, and required-ness. See the full Carta properties below, or follow the OCF link for full OCF field documentation._

<div class="domain-compare" markdown="1">
<div class="domain-compare__col" markdown="1">
**Carta** — [`v1alpha1DraftOptionGrant`](../types/draft_option_grant.md)

_A draft option grant is an object that is the precursor of an option grant before it is approved, signed, and issued. The "draft" prefix is used to differentiate it from the final option grant object._

| Property | Type | Req |
|---|---|---|
| `id` | string |  |
| `draftOptionGrantSetId` | string |  |
| `issuerId` | string |  |
| `optionGrantId` | string |  |
| `state` | [`v1alpha1DraftSecurityState`](../types/draft_security_state.md) |  |
| `stockOptionType` | [`issuersdraftsecuritiesv1alpha1StockOptionType`](../types/issuersdraftsecurities_stock_option_type.md) |  |
| `grantReason` | [`v1alpha1GrantReason`](../types/grant_reason.md) |  |
| `quantity` | [`v1alpha1Decimal`](../types/decimal.md) |  |
| `earlyExercise` | boolean |  |
| `exercisePrice` | [`v1alpha1Money`](../types/money.md) |  |
| `stakeholder` | [`issuersdraftsecuritiesv1alpha1Stakeholder`](../types/issuersdraftsecurities_stakeholder.md) |  |
| `compliance` | [`v1alpha1Compliance`](../types/compliance.md) |  |
| `vesting` | [`v1alpha1Vesting`](../types/vesting.md) |  |
| `notes` | string |  |
| `createTime` | [`v1alpha1Iso8601CompleteCalendarDateTime`](../types/iso8601_complete_calendar_date_time.md) |  |
| `updateTime` | [`v1alpha1Iso8601CompleteCalendarDateTime`](../types/iso8601_complete_calendar_date_time.md) |  |
| `customLabel` | string |  |
| `boardApproval` | [`v1alpha1BoardApproval`](../types/board_approval.md) |  |
| `boardApprovalDate` | [`v1alpha1Date`](../types/date.md) |  |
| `grantDate` | [`v1alpha1Date`](../types/date.md) |  |
| `expirationDate` | [`v1alpha1Date`](../types/date.md) |  |
| `exercisePeriods` | [`issuersdraftsecuritiesv1alpha1ExercisePeriods`](../types/issuersdraftsecurities_exercise_periods.md) |  |
| `documents` | [`v1alpha1OptionGrantDocuments`](../types/option_grant_documents.md) |  |

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
| `id` | string |  | Output only. The unique identifier of the draft option grant. |
| `draftOptionGrantSetId` | string |  | Output only. The unique identifier of the draft option grant set. |
| `issuerId` | string |  | Output only. The unique identifier of the issuer. |
| `optionGrantId` | string |  | Output only. The unique identifier of the option grant that is originated by this draft once it is issued. |
| `state` | [`v1alpha1DraftSecurityState`](../types/draft_security_state.md) |  | Output only. The state of the draft option grant. Certain states are read-only and the draft option grant cannot be modified in those states. |
| `stockOptionType` | [`issuersdraftsecuritiesv1alpha1StockOptionType`](../types/issuersdraftsecurities_stock_option_type.md) |  | The type of the option grant. |
| `grantReason` | [`v1alpha1GrantReason`](../types/grant_reason.md) |  | The reason for granting the option. |
| `quantity` | [`v1alpha1Decimal`](../types/decimal.md) |  | The quantity of shares awarded in the option grant. |
| `earlyExercise` | boolean |  | Whether the option grant allows for early exercise. |
| `exercisePrice` | [`v1alpha1Money`](../types/money.md) |  | The exercise price of the option grant. |
| `stakeholder` | [`issuersdraftsecuritiesv1alpha1Stakeholder`](../types/issuersdraftsecurities_stakeholder.md) |  | The stakeholder to whom this security will be issued. |
| `compliance` | [`v1alpha1Compliance`](../types/compliance.md) |  | The compliance details of the stakeholder. |
| `vesting` | [`v1alpha1Vesting`](../types/vesting.md) |  | The vesting details of the option grant. |
| `notes` | string |  | Additional notes about the option grant. |
| `createTime` | [`v1alpha1Iso8601CompleteCalendarDateTime`](../types/iso8601_complete_calendar_date_time.md) |  | Output only. The timestamp when the option grant was created. |
| `updateTime` | [`v1alpha1Iso8601CompleteCalendarDateTime`](../types/iso8601_complete_calendar_date_time.md) |  | Output only. The timestamp when the option grant was last updated. |
| `customLabel` | string |  | A custom identifier for the draft option grant. |
| `boardApproval` | [`v1alpha1BoardApproval`](../types/board_approval.md) |  | The board approval status for the draft option grant. |
| `boardApprovalDate` | [`v1alpha1Date`](../types/date.md) |  | The board approval date for the draft option grant. Only provide if the board_approval status is approved. |
| `grantDate` | [`v1alpha1Date`](../types/date.md) |  | The grant date for the draft option grant. |
| `expirationDate` | [`v1alpha1Date`](../types/date.md) |  | The expiration date for the draft option grant. |
| `exercisePeriods` | [`issuersdraftsecuritiesv1alpha1ExercisePeriods`](../types/issuersdraftsecurities_exercise_periods.md) |  | The exercise periods for the draft option grant. |
| `documents` | [`v1alpha1OptionGrantDocuments`](../types/option_grant_documents.md) |  | Optional documents that are relevant to a draft option grant. |


## Referenced by

_(not embedded in other domain objects)_


---

_Underlying schema: [`v1alpha1DraftOptionGrant`](../types/draft_option_grant.md)_


[← Back to Domain Index](index.md)
