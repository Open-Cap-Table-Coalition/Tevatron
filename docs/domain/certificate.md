# Certificate

A certificate is a record of ownership of a company's shares.

## OCF Equivalent

Carta's `Certificate` is a stock certificate (current state). OCF models the
creation of a stock position as a `StockIssuance` transaction; the "certificate"
as a concept is the issuance plus any subsequent cancellation/transfer/repurchase.


- [`StockIssuance`](https://open-cap-table-coalition.github.io/Open-Cap-Format-OCF/schema_markdown/schema/objects/transactions/issuance/StockIssuance/) — _issuance_ tx. Creates the position.

**Related:**

- [`StockCancellation`](https://open-cap-table-coalition.github.io/Open-Cap-Format-OCF/schema_markdown/schema/objects/transactions/cancellation/StockCancellation/) — _cancellation_ tx
- [`StockTransfer`](https://open-cap-table-coalition.github.io/Open-Cap-Format-OCF/schema_markdown/schema/objects/transactions/transfer/StockTransfer/) — _transfer_ tx
- [`StockRepurchase`](https://open-cap-table-coalition.github.io/Open-Cap-Format-OCF/schema_markdown/schema/objects/transactions/repurchase/StockRepurchase/) — _repurchase_ tx

## Endpoints

- `GET /v1alpha1/issuers/{issuerId}/certificates` — list
- `GET /v1alpha1/issuers/{issuerId}/certificates/{id}` — single


## Shape at a glance

_Quick comparison of field names, types, and required-ness. See the full Carta properties below, or follow the OCF link for full OCF field documentation._

<div class="domain-compare" markdown="1">
<div class="domain-compare__col" markdown="1">
**Carta** — [`v1alpha1Certificate`](../objects/certificate.md)

_A certificate is a record of ownership of a company's shares._

| Property | Type | Req |
|---|---|---|
| `id` | string |  |
| `issuerId` | string |  |
| `stakeholderId` | string |  |
| `shareClassName` | string |  |
| `issueDate` | [`v1alpha1Iso8601CompleteCalendarDate`](../types/iso8601_complete_calendar_date.md) |  |
| `quantity` | [`v1alpha1Decimal`](../types/decimal.md) |  |
| `securityLabel` | string |  |
| `pricePerShare` | [`v1alpha1Money`](../types/money.md) |  |
| `canceledDate` | [`v1alpha1Iso8601CompleteCalendarDate`](../types/iso8601_complete_calendar_date.md) |  |
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
| `id` | string |  | The identifier of the certificate. |
| `issuerId` | string |  | The identifier of the issuer owning the certificate. |
| `stakeholderId` | string |  | The identifier of the stakeholder holding the certificate. |
| `shareClassName` | string |  | The name of the share class for the shares held in this certificate. |
| `issueDate` | [`v1alpha1Iso8601CompleteCalendarDate`](../types/iso8601_complete_calendar_date.md) |  | The date the certificate was issued. |
| `quantity` | [`v1alpha1Decimal`](../types/decimal.md) |  | The number of shares in the certificate. |
| `securityLabel` | string |  | The label representing this security (certificate). |
| `pricePerShare` | [`v1alpha1Money`](../types/money.md) |  | The cost of each share in the certificate. |
| `canceledDate` | [`v1alpha1Iso8601CompleteCalendarDate`](../types/iso8601_complete_calendar_date.md) |  | The date the certificate was canceled. |
| `canceledQuantity` | [`v1alpha1Decimal`](../types/decimal.md) |  | The number of shares in the certificate that were canceled. |
| `returnedToPoolQuantity` | [`v1alpha1Decimal`](../types/decimal.md) |  | The number of shares in the certificate that were returned to the pool. |
| `returnedToTreasuryQuantity` | [`v1alpha1Decimal`](../types/decimal.md) |  | The number of shares in the certificate that were annulled, but not returned to the pool. |
| `lastModifiedDatetime` | [`v1alpha1Iso8601CompleteCalendarDateTime`](../types/iso8601_complete_calendar_date_time.md) |  | The date and time when the certificate was last modified. |


## Referenced by

_(not embedded in other domain objects)_


---

_Underlying schema: [`v1alpha1Certificate`](../objects/certificate.md)_


[← Back to Domain Index](index.md)
