### Money

**Description:** _Represents an amount of money with its currency type._

**Referenced By (20):**
- [Capitalization Table Summary](capitalization_table_summary.md)
- [Certificate](../objects/certificate.md)
- [Convertible Note](../objects/convertible_note.md)
- [Draft Option Grant](draft_option_grant.md)
- [Interest](../objects/interest.md)
- [Note Block Summary](note_block_summary.md)
- [Option Exercise Tax Withholding Line Item](option_exercise_tax_withholding_line_item.md)
- [Option Grant](../objects/option_grant.md)
- [Restricted Stock Award](../objects/restricted_stock_award.md)
- [Restricted Stock Unit](../objects/restricted_stock_unit.md)
- [Restricted Stock Unit Settlement](restricted_stock_unit_settlement.md)
- [Share Class](../objects/share_class.md)
- [Share Class Rights And Preferences](share_class_rights_and_preferences.md)
- [Share Class Summary](share_class_summary.md)
- [Share Class Valuation](share_class_valuation.md)
- [Stakeholder Capitalization Table Summary](stakeholder_capitalization_table_summary.md)
- [Stakeholder Note Block Summary](stakeholder_note_block_summary.md)
- [Stakeholder Share Class Summary](stakeholder_share_class_summary.md)
- [Stakeholder Warrant Block Summary](stakeholder_warrant_block_summary.md)
- [Warrant Block Summary](warrant_block_summary.md)

**References (2):**
- [Decimal](decimal.md)
- [Iso4217 Currency Alpha Code](iso4217_currency_alpha_code.md)

**Example:**
```json
{
  "currencyCode": "USD",
  "amount": {
    "value": "1000.77"
  }
}
```

**Properties:**

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| `amount` | [Decimal](decimal.md) | Decimal amount of the specified currency. For example if `currencyCode` is `"USD"`, then amount of 1 is one US dollar. | - |
| `currencyCode` | [Iso4217 Currency Alpha Code](iso4217_currency_alpha_code.md) | The 3-letter currency code defined in ISO 4217. | - |