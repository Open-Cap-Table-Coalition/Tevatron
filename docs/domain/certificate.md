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
