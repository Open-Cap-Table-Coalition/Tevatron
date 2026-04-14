### Iso8601 Complete Calendar Date

**Description:** _A complete calendar date defined as per the ISO 8601 standard._

**Referenced By (17):**
- [Issuersinterests Vesting Schedule](issuersinterests_vesting_schedule.md)
- [Issuerssecurities Vesting Schedule](issuerssecurities_vesting_schedule.md)
- [Capitalization Table](capitalization_table.md)
- [Certificate](../objects/certificate.md)
- [Exercise](exercise.md)
- [Fair Market Value](../objects/fair_market_value.md)
- [Interest](../objects/interest.md)
- [List Interests Response](list_interests_response.md)
- [Option Grant](../objects/option_grant.md)
- [Option Grant Vesting Event](option_grant_vesting_event.md)
- [Performance Condition](performance_condition.md)
- [Restricted Stock Award](../objects/restricted_stock_award.md)
- [Restricted Stock Award Vesting Event](restricted_stock_award_vesting_event.md)
- [Restricted Stock Unit](../objects/restricted_stock_unit.md)
- [Restricted Stock Unit Settlement](restricted_stock_unit_settlement.md)
- [Restricted Stock Unit Vesting Event](restricted_stock_unit_vesting_event.md)
- [Stakeholder Capitalization Table](stakeholder_capitalization_table.md)

**Example:**
```json
{
  "value": "2021-01-01"
}
```

**Properties:**

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| `value` | `STRING` | **Constraints:** Pattern: `[0-9]{4}-[0-9]{2}-[0-9]{2}`, Min length: 10, Max length: 10 | - |