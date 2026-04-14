### Iso8601 Complete Calendar Date Time

**Description:** _A complete calendar UTC date and time defined as per the ISO 8601 standard._

**Referenced By (32):**
- [Benchmarks Metadata](benchmarks_metadata.md)
- [Certificate](../objects/certificate.md)
- [Certificate Cancellation Transaction](certificate_cancellation_transaction.md)
- [Certificate Issuance Transaction](certificate_issuance_transaction.md)
- [Convertible Cancellation Transaction](convertible_cancellation_transaction.md)
- [Convertible Issuance Transaction](convertible_issuance_transaction.md)
- [Convertible Note](../objects/convertible_note.md)
- [Draft Option Grant](draft_option_grant.md)
- [Interest](../objects/interest.md)
- [Option Cancellation Transaction](option_cancellation_transaction.md)
- [Option Exercise](../objects/option_exercise.md)
- [Option Exercise Money Movement](option_exercise_money_movement.md)
- [Option Exercise Transaction](option_exercise_transaction.md)
- [Option Grant](../objects/option_grant.md)
- [Option Issuance Transaction](option_issuance_transaction.md)
- [Option Pool Summary](option_pool_summary.md)
- [Piu Cancellation Transaction](piu_cancellation_transaction.md)
- [Piu Issuance Transaction](piu_issuance_transaction.md)
- [Restricted Stock Award](../objects/restricted_stock_award.md)
- [Restricted Stock Unit](../objects/restricted_stock_unit.md)
- [Rsa Cancellation Transaction](rsa_cancellation_transaction.md)
- [Rsa Issuance Transaction](rsa_issuance_transaction.md)
- [Rsu Cancellation Transaction](rsu_cancellation_transaction.md)
- [Rsu Issuance Transaction](rsu_issuance_transaction.md)
- [Rsu Settlement Transaction](rsu_settlement_transaction.md)
- [Sar Cancellation Transaction](sar_cancellation_transaction.md)
- [Sar Exercise Transaction](sar_exercise_transaction.md)
- [Sar Issuance Transaction](sar_issuance_transaction.md)
- [Warrant Cancellation Transaction](warrant_cancellation_transaction.md)
- [Warrant Exercise Transaction](warrant_exercise_transaction.md)
- [Warrant Issuance Transaction](warrant_issuance_transaction.md)
- [Warrant Transfer Transaction](warrant_transfer_transaction.md)

**Example:**
```json
{
  "value": "2021-01-01T18:18:00Z"
}
```

**Properties:**

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| `value` | `STRING` | **Constraints:** Pattern: `[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}(?:\.[0-9]{1,3})?Z`, Min length: 20, Max length: 24 | - |