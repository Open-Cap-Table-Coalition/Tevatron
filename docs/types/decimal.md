### Decimal

**Description:** _A string-based representation of the decimal type._

**Referenced By (28):**
- [Benchmark Value](benchmark_value.md)
- [Capitalization Table Summary](capitalization_table_summary.md)
- [Certificate](../objects/certificate.md)
- [Convertible Note](../objects/convertible_note.md)
- [Dividend Details](dividend_details.md)
- [Draft Option Grant](draft_option_grant.md)
- [Exercise](exercise.md)
- [Interest](../objects/interest.md)
- [Money](money.md)
- [Option Exercise](../objects/option_exercise.md)
- [Option Exercise Tax Withholding Line Item](option_exercise_tax_withholding_line_item.md)
- [Option Grant](../objects/option_grant.md)
- [Option Grant Vesting Event](option_grant_vesting_event.md)
- [Option Pool Summary](option_pool_summary.md)
- [Restricted Stock Award](../objects/restricted_stock_award.md)
- [Restricted Stock Award Vesting Event](restricted_stock_award_vesting_event.md)
- [Restricted Stock Unit](../objects/restricted_stock_unit.md)
- [Restricted Stock Unit Settlement](restricted_stock_unit_settlement.md)
- [Restricted Stock Unit Vesting Event](restricted_stock_unit_vesting_event.md)
- [Share Class](../objects/share_class.md)
- [Share Class Rights And Preferences](share_class_rights_and_preferences.md)
- [Share Class Summary](share_class_summary.md)
- [Stakeholder Capitalization Table Summary](stakeholder_capitalization_table_summary.md)
- [Stakeholder Option Pool Summary](stakeholder_option_pool_summary.md)
- [Stakeholder Share Class Summary](stakeholder_share_class_summary.md)
- [Stakeholder Warrant Block Summary](stakeholder_warrant_block_summary.md)
- [Threshold Details](threshold_details.md)
- [Warrant Block Summary](warrant_block_summary.md)

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