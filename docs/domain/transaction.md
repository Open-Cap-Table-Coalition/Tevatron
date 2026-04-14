# Transaction

The Carta API does not expose a single `Transaction` type. Instead, `GET /v1alpha1/issuers/{issuerId}/transactions` returns **eight parallel arrays**, one per security type. Conceptually these are variants of the same `Transaction` domain concept; the spec models them as sibling fields rather than as a discriminated union.

## OCF Equivalent

Carta's `ListTransactions` returns eight sibling arrays (one per security type),
where each array holds a discriminated union of events for that security. OCF
models each event type as its own transaction schema under
`schema/objects/transactions/<category>/`. The mapping below lists the
security-family → OCF transaction-category correspondences.


- [`StockIssuance`](https://open-cap-table-coalition.github.io/Open-Cap-Format-OCF/schema_markdown/schema/objects/transactions/issuance/StockIssuance/) — _issuance_ tx. Carta `CertificateTransactionItem` family.
- [`ConvertibleIssuance`](https://open-cap-table-coalition.github.io/Open-Cap-Format-OCF/schema_markdown/schema/objects/transactions/issuance/ConvertibleIssuance/) — _issuance_ tx. Carta `ConvertibleTransactionItem` family.
- [`EquityCompensationIssuance`](https://open-cap-table-coalition.github.io/Open-Cap-Format-OCF/schema_markdown/schema/objects/transactions/issuance/EquityCompensationIssuance/) — _issuance_ tx. Carta `OptionTransactionItem`, `RsuTransactionItem`, `RsaTransactionItem`,
`PiuTransactionItem`, and `SarTransactionItem` families all fold into OCF's
single `EquityCompensationIssuance` family (distinguished by compensation type).
- [`WarrantIssuance`](https://open-cap-table-coalition.github.io/Open-Cap-Format-OCF/schema_markdown/schema/objects/transactions/issuance/WarrantIssuance/) — _issuance_ tx. Carta `WarrantTransactionItem` family.

**Related:**

- [`EquityCompensationExercise`](https://open-cap-table-coalition.github.io/Open-Cap-Format-OCF/schema_markdown/schema/objects/transactions/exercise/EquityCompensationExercise/) — _exercise_ tx. Carta exercise events within the option/RSU/RSA families.
- [`StockCancellation`](https://open-cap-table-coalition.github.io/Open-Cap-Format-OCF/schema_markdown/schema/objects/transactions/cancellation/StockCancellation/) — _cancellation_ tx
- [`EquityCompensationCancellation`](https://open-cap-table-coalition.github.io/Open-Cap-Format-OCF/schema_markdown/schema/objects/transactions/cancellation/EquityCompensationCancellation/) — _cancellation_ tx

## Endpoints

- `GET /v1alpha1/issuers/{issuerId}/transactions` — returns all variants in one response


## Variants

- **Option grants** — [`v1alpha1OptionTransactionItem`](../objects/option_transaction_item.md)
- **Restricted stock units** — [`v1alpha1RsuTransactionItem`](../types/rsu_transaction_item.md)
- **Restricted stock awards** — [`v1alpha1RsaTransactionItem`](../types/rsa_transaction_item.md)
- **Certificates** — [`v1alpha1CertificateTransactionItem`](../types/certificate_transaction_item.md)
- **Warrants** — [`v1alpha1WarrantTransactionItem`](../types/warrant_transaction_item.md)
- **Convertible notes** — [`v1alpha1ConvertibleTransactionItem`](../types/convertible_transaction_item.md)
- **Profits interest units** — [`v1alpha1PiuTransactionItem`](../types/piu_transaction_item.md)
- **Stock appreciation rights** — [`v1alpha1SarTransactionItem`](../types/sar_transaction_item.md)

## Response shape

```
ListTransactionsResponse {
  optionTransactions:      OptionTransactionItem[]
  rsuTransactions:         RsuTransactionItem[]
  rsaTransactions:         RsaTransactionItem[]
  certificateTransactions: CertificateTransactionItem[]
  warrantTransactions:     WarrantTransactionItem[]
  convertibleTransactions: ConvertibleTransactionItem[]
  piuTransactions:         PiuTransactionItem[]
  sarTransactions:         SarTransactionItem[]
}
```


## Modeling note

If you are building a client-side domain model, you will likely want to merge these eight variants into a single polymorphic `Transaction` type with a discriminator field. The wire format does not provide one.


[← Back to Domain Index](index.md)
