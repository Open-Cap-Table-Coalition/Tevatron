### Iso8601 Complete Calendar Date Time

**Description:** _A complete calendar UTC date and time defined as per the ISO 8601 standard._

**Referenced By (11):**
- [Benchmarks Metadata](benchmarks_metadata.md)
- [Certificate](../objects/certificate.md)
- [Convertible Note](../objects/convertible_note.md)
- [Draft Option Grant](draft_option_grant.md)
- [Interest](../objects/interest.md)
- [Option Exercise](../objects/option_exercise.md)
- [Option Exercise Money Movement](option_exercise_money_movement.md)
- [Option Grant](../objects/option_grant.md)
- [Option Pool Summary](option_pool_summary.md)
- [Restricted Stock Award](../objects/restricted_stock_award.md)
- [Restricted Stock Unit](../objects/restricted_stock_unit.md)

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