### Warrant Transfer Transaction

**Description:** _A transfer transaction for a warrant. Represents the transfer of warrant shares to a new warrant._

**Referenced By (1):**
- [Warrant Transaction Item](warrant_transaction_item.md)

**References (2):**
- [Decimal](decimal.md)
- [Iso8601 Complete Calendar Date Time](iso8601_complete_calendar_date_time.md)

**Example:**
```json
{
  "transferredDatetime": {
    "value": "2025-02-01T00:00:00Z"
  },
  "quantity": {
    "value": "5000"
  },
  "resultingSecurityId": "5102",
  "resultingSecurityLabel": "W-8"
}
```

**Properties:**

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| `quantity` | [Decimal](decimal.md) | The number of warrant shares transferred. | - |
| `resultingSecurityId` | `STRING` | The identifier of the new warrant created as a result of the transfer. <br/>**Constraints:** Max length: 50 | - |
| `resultingSecurityLabel` | `STRING` | The human-readable label of the new warrant created as a result of the transfer (e.g. "W-8"). <br/>**Constraints:** Max length: 50 | - |
| `transferredDatetime` | [Iso8601 Complete Calendar Date Time](iso8601_complete_calendar_date_time.md) | The date and time the transfer was executed. | - |