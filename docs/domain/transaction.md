# Transaction

The Carta API does not expose a single `Transaction` type. Instead, `GET /v1alpha1/issuers/{issuerId}/transactions` returns **eight parallel arrays**, one per security type. Conceptually these are variants of the same `Transaction` domain concept; the spec models them as sibling fields rather than as a discriminated union.

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
