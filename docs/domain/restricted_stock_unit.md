# Restricted Stock Unit

A restricted stock unit is a grant of company shares.

## OCF Equivalent

RSUs in OCF are modeled as equity compensation issuances (the same family as options),
distinguished by the compensation type on the issuance transaction itself. Settlement
(the moment shares transfer to the holder) is captured by `EquityCompensationRelease`.


- [`EquityCompensationIssuance`](https://open-cap-table-coalition.github.io/Open-Cap-Format-OCF/schema_markdown/schema/objects/transactions/issuance/EquityCompensationIssuance/) — _issuance_ tx. RSUs are issued via the equity-compensation family.

**Related:**

- [`EquityCompensationRelease`](https://open-cap-table-coalition.github.io/Open-Cap-Format-OCF/schema_markdown/schema/objects/transactions/release/EquityCompensationRelease/) — _release_ tx. Carta's "settlement" ≈ OCF's release.

## Endpoints

- `GET /v1alpha1/issuers/{issuerId}/restrictedStockUnits` — list
- `GET /v1alpha1/issuers/{issuerId}/restrictedStockUnits/{id}` — single


## Shape at a glance

_Quick comparison of field names, types, and required-ness. See the full Carta properties below, or follow the OCF link for full OCF field documentation._

<div class="domain-compare" markdown="1">
<div class="domain-compare__col" markdown="1">
**Carta** — [`v1alpha1RestrictedStockUnit`](../objects/restricted_stock_unit.md)

_A restricted stock unit is a grant of company shares._

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
| `quantity` | [`v1alpha1Decimal`](../types/decimal.md) |  |
| `vestedQuantity` | [`v1alpha1Decimal`](../types/decimal.md) |  |
| `releasedQuantity` | [`v1alpha1Decimal`](../types/decimal.md) |  |
| `releasePricePerShare` | [`v1alpha1Money`](../types/money.md) |  |
| `netSettledQuantity` | [`v1alpha1Decimal`](../types/decimal.md) |  |
| `securityLabel` | string |  |
| `vestingEvents` | [`v1alpha1RestrictedStockUnitVestingEvent`](../types/restricted_stock_unit_vesting_event.md)[] |  |
| `canceledDate` | [`v1alpha1Iso8601CompleteCalendarDate`](../types/iso8601_complete_calendar_date.md) |  |
| `terminationDate` | [`v1alpha1Iso8601CompleteCalendarDate`](../types/iso8601_complete_calendar_date.md) |  |
| `settlements` | [`v1alpha1RestrictedStockUnitSettlement`](../types/restricted_stock_unit_settlement.md)[] |  |
| `vestingSchedule` | [`issuerssecuritiesv1alpha1VestingSchedule`](../types/issuerssecurities_vesting_schedule.md) |  |
| `canceledQuantity` | [`v1alpha1Decimal`](../types/decimal.md) |  |
| `forfeitedQuantity` | [`v1alpha1Decimal`](../types/decimal.md) |  |
| `expiredQuantity` | [`v1alpha1Decimal`](../types/decimal.md) |  |
| `returnedToPoolQuantity` | [`v1alpha1Decimal`](../types/decimal.md) |  |
| `returnedToTreasuryQuantity` | [`v1alpha1Decimal`](../types/decimal.md) |  |
| `lastModifiedDatetime` | [`v1alpha1Iso8601CompleteCalendarDateTime`](../types/iso8601_complete_calendar_date_time.md) |  |

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
| `id` | string |  | The identifier of the restricted stock unit. |
| `issuerId` | string |  | The identifier of the issuer owning the restricted stock unit. |
| `stakeholderId` | string |  | The identifier of the stakeholder that received the restricted stock unit. |
| `equityIncentivePlanName` | string |  | The name of the equity incentive plan (i.e., option plan) associated with the restricted stock unit. |
| `issueDate` | [`v1alpha1Iso8601CompleteCalendarDate`](../types/iso8601_complete_calendar_date.md) |  | The date the restricted stock unit was issued. |
| `vestingStartDate` | [`v1alpha1Iso8601CompleteCalendarDate`](../types/iso8601_complete_calendar_date.md) |  | The start date of the vesting period for the restricted stock unit, specified as an [ISO 8601 extended format calendar date](https://en.wikipedia.org/wiki/ISO_8601#Calendar_dates), i.e. 'YYYY-MM-DD'. |
| `boardApprovalDate` | [`v1alpha1Iso8601CompleteCalendarDate`](../types/iso8601_complete_calendar_date.md) |  | The date the restricted stock unit received board approval. |
| `stakeholderAcceptanceDate` | [`v1alpha1Iso8601CompleteCalendarDate`](../types/iso8601_complete_calendar_date.md) |  | The date the restricted stock unit was accepted by the stakeholder, specified as an [ISO 8601 extended format calendar date](https://en.wikipedia.org/wiki/ISO_8601#Calendar_dates), i.e. 'YYYY-MM-DD'. |
| `quantity` | [`v1alpha1Decimal`](../types/decimal.md) |  | The total quantity of shares in the restricted stock unit grant. |
| `vestedQuantity` | [`v1alpha1Decimal`](../types/decimal.md) |  | The total quantity of restricted stock units in the grant that have been vested. |
| `releasedQuantity` | [`v1alpha1Decimal`](../types/decimal.md) |  | The total quantity of restricted stock units in the grant that has been settled. |
| `releasePricePerShare` | [`v1alpha1Money`](../types/money.md) |  | The price of each share that has been released from the restricted stock unit grant. |
| `netSettledQuantity` | [`v1alpha1Decimal`](../types/decimal.md) |  | The total quantity of restricted stock units in this grant that have been released to the stakeholder. |
| `securityLabel` | string |  | The label representing this security (restricted stock unit). |
| `vestingEvents` | [`v1alpha1RestrictedStockUnitVestingEvent`](../types/restricted_stock_unit_vesting_event.md)[] |  | The list of all vesting events associated with these restricted stock units. |
| `canceledDate` | [`v1alpha1Iso8601CompleteCalendarDate`](../types/iso8601_complete_calendar_date.md) |  | The date the restricted stock unit was canceled. |
| `terminationDate` | [`v1alpha1Iso8601CompleteCalendarDate`](../types/iso8601_complete_calendar_date.md) |  | The date the restricted stock unit was terminated. |
| `settlements` | [`v1alpha1RestrictedStockUnitSettlement`](../types/restricted_stock_unit_settlement.md)[] |  | The list of all settlements associated with these restricted stock units. |
| `vestingSchedule` | [`issuerssecuritiesv1alpha1VestingSchedule`](../types/issuerssecurities_vesting_schedule.md) |  | The vesting schedule information associated with the restricted stock unit. |
| `canceledQuantity` | [`v1alpha1Decimal`](../types/decimal.md) |  | The number of shares in the restricted stock unit that were canceled. |
| `forfeitedQuantity` | [`v1alpha1Decimal`](../types/decimal.md) |  | The number of shares in the restricted stock unit that were forfeited. |
| `expiredQuantity` | [`v1alpha1Decimal`](../types/decimal.md) |  | The number of shares in the restricted stock unit that expired. |
| `returnedToPoolQuantity` | [`v1alpha1Decimal`](../types/decimal.md) |  | The number of shares in the restricted stock unit that were returned to the pool. |
| `returnedToTreasuryQuantity` | [`v1alpha1Decimal`](../types/decimal.md) |  | The number of shares in the restricted stock unit that were annulled, but not returned to the pool. |
| `lastModifiedDatetime` | [`v1alpha1Iso8601CompleteCalendarDateTime`](../types/iso8601_complete_calendar_date_time.md) |  | The date and time when the restricted stock unit was last modified. |


## Referenced by

_(not embedded in other domain objects)_


---

_Underlying schema: [`v1alpha1RestrictedStockUnit`](../objects/restricted_stock_unit.md)_


[← Back to Domain Index](index.md)
