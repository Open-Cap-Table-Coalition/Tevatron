### Decimal

**Description:** _A string-based representation of the decimal type._

**Referenced By (50):**
- [Benchmark Value](benchmark_value.md)
- [Capitalization Table Summary](capitalization_table_summary.md)
- [Certificate](../objects/certificate.md)
- [Certificate Cancellation Transaction](certificate_cancellation_transaction.md)
- [Certificate Issuance Transaction](certificate_issuance_transaction.md)
- [Convertible Issuance Transaction](convertible_issuance_transaction.md)
- [Convertible Note](../objects/convertible_note.md)
- [Dividend Details](dividend_details.md)
- [Draft Option Grant](draft_option_grant.md)
- [Exercise](exercise.md)
- [Interest](../objects/interest.md)
- [Money](money.md)
- [Option Cancellation Transaction](option_cancellation_transaction.md)
- [Option Exercise](../objects/option_exercise.md)
- [Option Exercise Tax Withholding Line Item](option_exercise_tax_withholding_line_item.md)
- [Option Exercise Transaction](option_exercise_transaction.md)
- [Option Grant](../objects/option_grant.md)
- [Option Grant Vesting Event](option_grant_vesting_event.md)
- [Option Issuance Transaction](option_issuance_transaction.md)
- [Option Pool Summary](option_pool_summary.md)
- [Performance Condition](performance_condition.md)
- [Piu Cancellation Transaction](piu_cancellation_transaction.md)
- [Piu Issuance Transaction](piu_issuance_transaction.md)
- [Restricted Stock Award](../objects/restricted_stock_award.md)
- [Restricted Stock Award Vesting Event](restricted_stock_award_vesting_event.md)
- [Restricted Stock Unit](../objects/restricted_stock_unit.md)
- [Restricted Stock Unit Settlement](restricted_stock_unit_settlement.md)
- [Restricted Stock Unit Vesting Event](restricted_stock_unit_vesting_event.md)
- [Rsa Cancellation Transaction](rsa_cancellation_transaction.md)
- [Rsa Issuance Transaction](rsa_issuance_transaction.md)
- [Rsu Cancellation Transaction](rsu_cancellation_transaction.md)
- [Rsu Issuance Transaction](rsu_issuance_transaction.md)
- [Rsu Settlement Transaction](rsu_settlement_transaction.md)
- [Sar Cancellation Transaction](sar_cancellation_transaction.md)
- [Sar Exercise Transaction](sar_exercise_transaction.md)
- [Sar Issuance Transaction](sar_issuance_transaction.md)
- [Share Class](../objects/share_class.md)
- [Share Class Rights And Preferences](share_class_rights_and_preferences.md)
- [Share Class Summary](share_class_summary.md)
- [Stakeholder Capitalization Table Summary](stakeholder_capitalization_table_summary.md)
- [Stakeholder Option Pool Summary](stakeholder_option_pool_summary.md)
- [Stakeholder Share Class Summary](stakeholder_share_class_summary.md)
- [Stakeholder Warrant Block Summary](stakeholder_warrant_block_summary.md)
- [Threshold Details](threshold_details.md)
- [Vesting Period](vesting_period.md)
- [Warrant Block Summary](warrant_block_summary.md)
- [Warrant Cancellation Transaction](warrant_cancellation_transaction.md)
- [Warrant Exercise Transaction](warrant_exercise_transaction.md)
- [Warrant Issuance Transaction](warrant_issuance_transaction.md)
- [Warrant Transfer Transaction](warrant_transfer_transaction.md)

**Example:**
```json
{
  "value": "100.57"
}
```

**Properties:**

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| `value` | `STRING` | A decimal amount represented in string form.  Examples: 0 0.0 1.00 123.45 -456.0 .321 +1.23456e-3 1e-05 <br/>**Constraints:** Pattern: `^[\+\-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([eE][\+\-]?[0-9]+)?$`, Min length: 1, Max length: 100 | - |