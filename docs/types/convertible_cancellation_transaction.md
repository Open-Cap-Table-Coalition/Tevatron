### Convertible Cancellation Transaction

**Description:** _A cancellation transaction for a convertible note._

**Referenced By (1):**
- [Convertible Transaction Item](convertible_transaction_item.md)

**References (3):**
- [Convertible Cancellation Reason](convertible_cancellation_reason.md)
- [Iso8601 Complete Calendar Date Time](iso8601_complete_calendar_date_time.md)
- [Money](money.md)

**Example:**
```json
{
  "effectiveDatetime": {
    "value": "2025-10-02T00:00:00Z"
  },
  "reason": "CONVERTIBLE_CANCELLATION_REASON_CONVERTED",
  "principal": {
    "currencyCode": {
      "value": "USD"
    },
    "amount": {
      "value": "500000"
    }
  }
}
```

**Properties:**

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| `effectiveDatetime` | [Iso8601 Complete Calendar Date Time](iso8601_complete_calendar_date_time.md) | The effective date and time of the cancellation. | - |
| `principal` | [Money](money.md) | The principal amount cancelled. May be less than the original note principal if this is a partial cancellation. | - |
| `reason` | [Convertible Cancellation Reason](convertible_cancellation_reason.md) | The reason for the cancellation. | - |