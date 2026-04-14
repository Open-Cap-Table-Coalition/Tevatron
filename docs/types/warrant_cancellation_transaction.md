### Warrant Cancellation Transaction

**Description:** _A cancellation transaction for a warrant._

**Referenced By (1):**
- [Warrant Transaction Item](warrant_transaction_item.md)

**References (3):**
- [Decimal](decimal.md)
- [Iso8601 Complete Calendar Date Time](iso8601_complete_calendar_date_time.md)
- [Warrant Cancellation Reason](warrant_cancellation_reason.md)

**Example:**
```json
{
  "effectiveDatetime": {
    "value": "2025-06-01T00:00:00Z"
  },
  "reason": "WARRANT_CANCELLATION_REASON_LIFETIME_ENDED",
  "quantity": {
    "value": "40000"
  }
}
```

**Properties:**

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| `effectiveDatetime` | [Iso8601 Complete Calendar Date Time](iso8601_complete_calendar_date_time.md) | The effective date and time of the cancellation. | - |
| `quantity` | [Decimal](decimal.md) | The number of warrant shares affected by the cancellation. | - |
| `reason` | [Warrant Cancellation Reason](warrant_cancellation_reason.md) | The reason for the cancellation. See `WarrantCancellationReason` for all supported values. | - |