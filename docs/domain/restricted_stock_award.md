# Restricted Stock Award

A restricted stock award is a grant of company shares.

## OCF Equivalent

OCF does not distinguish RSAs from regular stock issuances at the transaction level —
an RSA is modeled as a `StockIssuance` with vesting terms attached, and subsequent
events use the stock-transaction family.


- [`StockIssuance`](https://open-cap-table-coalition.github.io/Open-Cap-Format-OCF/schema_markdown/schema/objects/transactions/issuance/StockIssuance/) — _issuance_ tx. RSAs in OCF are stock issuances with vesting terms attached.

**Related:**

- [`VestingTerms`](https://open-cap-table-coalition.github.io/Open-Cap-Format-OCF/schema_markdown/schema/objects/VestingTerms/) — object

## Endpoints

- `GET /v1alpha1/issuers/{issuerId}/restrictedStockAwards` — list
- `GET /v1alpha1/issuers/{issuerId}/restrictedStockAwards/{id}` — single


## Shape at a glance

_Quick comparison of field names, types, and required-ness. See the full Carta properties below, or follow the OCF link for full OCF field documentation._

<div class="domain-compare" markdown="1">
<div class="domain-compare__col" markdown="1">
**Carta** — [`v1alpha1RestrictedStockAward`](../objects/restricted_stock_award.md)

_A restricted stock award is a grant of company shares._

| Property | Type | Req |
|---|---|---|
| `id` | string |  |
| `issuerId` | string |  |
| `stakeholderId` | string |  |
| `equityIncentivePlanName` | string |  |
| `shareClassName` | string |  |
| `issueDate` | [`v1alpha1Iso8601CompleteCalendarDate`](../types/iso8601_complete_calendar_date.md) |  |
| `vestingStartDate` | [`v1alpha1Iso8601CompleteCalendarDate`](../types/iso8601_complete_calendar_date.md) |  |
| `boardApprovalDate` | [`v1alpha1Iso8601CompleteCalendarDate`](../types/iso8601_complete_calendar_date.md) |  |
| `stakeholderAcceptanceDate` | [`v1alpha1Iso8601CompleteCalendarDate`](../types/iso8601_complete_calendar_date.md) |  |
| `canceledDate` | [`v1alpha1Iso8601CompleteCalendarDate`](../types/iso8601_complete_calendar_date.md) |  |
| `terminationDate` | [`v1alpha1Iso8601CompleteCalendarDate`](../types/iso8601_complete_calendar_date.md) |  |
| `quantity` | [`v1alpha1Decimal`](../types/decimal.md) |  |
| `vestedQuantity` | [`v1alpha1Decimal`](../types/decimal.md) |  |
| `securityLabel` | string |  |
| `pricePerShare` | [`v1alpha1Money`](../types/money.md) |  |
| `vestingEvents` | [`v1alpha1RestrictedStockAwardVestingEvent`](../types/restricted_stock_award_vesting_event.md)[] |  |
| `vestingSchedule` | [`issuerssecuritiesv1alpha1VestingSchedule`](../types/issuerssecurities_vesting_schedule.md) |  |
| `canceledQuantity` | [`v1alpha1Decimal`](../types/decimal.md) |  |
| `returnedToPoolQuantity` | [`v1alpha1Decimal`](../types/decimal.md) |  |
| `returnedToTreasuryQuantity` | [`v1alpha1Decimal`](../types/decimal.md) |  |
| `lastModifiedDatetime` | [`v1alpha1Iso8601CompleteCalendarDateTime`](../types/iso8601_complete_calendar_date_time.md) |  |

</div>
<div class="domain-compare__col" markdown="1">
**OCF** — [`StockIssuance`](https://open-cap-table-coalition.github.io/Open-Cap-Format-OCF/schema_markdown/schema/objects/transactions/issuance/StockIssuance/)

_Object describing a stock issuance transaction by the issuer and held by a stakeholder_

| Property | Type | Required |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------- |
| id | `STRING` | `REQUIRED` |
| comments | [`STRING`] | - |
| object_type | **Constant:** `TX_STOCK_ISSUANCE`</br>_Defined in [schema/enums/ObjectType](https://open-cap-table-coalition.github.io/Open-Cap-Format-OCF/schema_markdown/schema/enums/ObjectType/)_ | `REQUIRED` |
| date | [schema/types/Date](https://open-cap-table-coalition.github.io/Open-Cap-Format-OCF/schema_markdown/schema/types/Date/) | `REQUIRED` |
| security_id | `STRING` | `REQUIRED` |
| custom_id | `STRING` | `REQUIRED` |
| stakeholder_id | `STRING` | `REQUIRED` |
| board_approval_date | [schema/types/Date](https://open-cap-table-coalition.github.io/Open-Cap-Format-OCF/schema_markdown/schema/types/Date/) | - |
| stockholder_approval_date | [schema/types/Date](https://open-cap-table-coalition.github.io/Open-Cap-Format-OCF/schema_markdown/schema/types/Date/) | - |
| consideration_text | `STRING` | - |
| security_law_exemptions | [ [schema/types/SecurityExemption](https://open-cap-table-coalition.github.io/Open-Cap-Format-OCF/schema_markdown/schema/types/SecurityExemption/) ] | `REQUIRED` |
| stock_class_id | `STRING` | `REQUIRED` |
| stock_plan_id | `STRING` | - |
| share_numbers_issued | [ [schema/types/ShareNumberRange](https://open-cap-table-coalition.github.io/Open-Cap-Format-OCF/schema_markdown/schema/types/ShareNumberRange/) ] | - |
| share_price | [schema/types/Monetary](https://open-cap-table-coalition.github.io/Open-Cap-Format-OCF/schema_markdown/schema/types/Monetary/) | `REQUIRED` |
| quantity | [schema/types/Numeric](https://open-cap-table-coalition.github.io/Open-Cap-Format-OCF/schema_markdown/schema/types/Numeric/) | `REQUIRED` |
| vesting_terms_id | `STRING` | - |
| vestings | [ [schema/types/Vesting](https://open-cap-table-coalition.github.io/Open-Cap-Format-OCF/schema_markdown/schema/types/Vesting/) ] | - |
| cost_basis | [schema/types/Monetary](https://open-cap-table-coalition.github.io/Open-Cap-Format-OCF/schema_markdown/schema/types/Monetary/) | - |
| stock_legend_ids | [`STRING`] | `REQUIRED` |
| issuance_type | `Enum - Stock Issuance Type`</br></br>_Description:_ Enumeration of issuance types where we want to draw attention to some unique aspect of a stock issuance (e.g. is it an RSA)</br></br>**ONE OF:** </br>&bull; RSA </br>&bull; FOUNDERS_STOCK | - |
</div>
</div>


## Properties

| Property | Type | Required | Description |
|---|---|---|---|
| `id` | string |  | The identifier of the restricted stock award. |
| `issuerId` | string |  | The identifier of the issuer owning the restricted stock award. |
| `stakeholderId` | string |  | The identifier of the stakeholder that holds the restricted stock award. |
| `equityIncentivePlanName` | string |  | The name of the equity incentive plan (i.e., option plan) associated with this restricted stock award. |
| `shareClassName` | string |  | The name of the share class that this restricted stock award belongs to. |
| `issueDate` | [`v1alpha1Iso8601CompleteCalendarDate`](../types/iso8601_complete_calendar_date.md) |  | The date the restricted stock award was issued. |
| `vestingStartDate` | [`v1alpha1Iso8601CompleteCalendarDate`](../types/iso8601_complete_calendar_date.md) |  | The start date of the vesting period for the restricted stock award. |
| `boardApprovalDate` | [`v1alpha1Iso8601CompleteCalendarDate`](../types/iso8601_complete_calendar_date.md) |  | The date the restricted stock award received board approval. |
| `stakeholderAcceptanceDate` | [`v1alpha1Iso8601CompleteCalendarDate`](../types/iso8601_complete_calendar_date.md) |  | The date the restricted stock award was accepted by the stakeholder. |
| `canceledDate` | [`v1alpha1Iso8601CompleteCalendarDate`](../types/iso8601_complete_calendar_date.md) |  | The date the restricted stock award was canceled. |
| `terminationDate` | [`v1alpha1Iso8601CompleteCalendarDate`](../types/iso8601_complete_calendar_date.md) |  | The date the restricted stock award was terminated. This commonly matches the date the company's relationship with the stakeholder was terminated. |
| `quantity` | [`v1alpha1Decimal`](../types/decimal.md) |  | The number of restricted stock units in the award. |
| `vestedQuantity` | [`v1alpha1Decimal`](../types/decimal.md) |  | The number of vested shares in the stock award. |
| `securityLabel` | string |  | The label representing this security (restricted stock award). |
| `pricePerShare` | [`v1alpha1Money`](../types/money.md) |  | The cost of each share in the restricted stock award. |
| `vestingEvents` | [`v1alpha1RestrictedStockAwardVestingEvent`](../types/restricted_stock_award_vesting_event.md)[] |  | The list of all vesting events associated with the restricted stock award. |
| `vestingSchedule` | [`issuerssecuritiesv1alpha1VestingSchedule`](../types/issuerssecurities_vesting_schedule.md) |  | The vesting schedule information associated with the restricted stock award. |
| `canceledQuantity` | [`v1alpha1Decimal`](../types/decimal.md) |  | The number of shares in the restricted stock award that were canceled. |
| `returnedToPoolQuantity` | [`v1alpha1Decimal`](../types/decimal.md) |  | The number of shares in the restricted stock award that were returned to the pool. |
| `returnedToTreasuryQuantity` | [`v1alpha1Decimal`](../types/decimal.md) |  | The number of shares in the restricted stock award that were annulled, but not returned to the pool. |
| `lastModifiedDatetime` | [`v1alpha1Iso8601CompleteCalendarDateTime`](../types/iso8601_complete_calendar_date_time.md) |  | The date and time when the restricted stock award was last modified. |


## Referenced by

_(not embedded in other domain objects)_


---

_Underlying schema: [`v1alpha1RestrictedStockAward`](../objects/restricted_stock_award.md)_


[← Back to Domain Index](index.md)
