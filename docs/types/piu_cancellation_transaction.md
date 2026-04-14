### Piu Cancellation Transaction

**Description:** _A cancellation or termination transaction for a PIU._

**Referenced By (1):**
- [Piu Transaction Item](piu_transaction_item.md)

**References (3):**
- [Decimal](decimal.md)
- [Iso8601 Complete Calendar Date Time](iso8601_complete_calendar_date_time.md)
- [Piu Cancellation Reason](piu_cancellation_reason.md)

**Example:**
```json
{
  "effectiveDatetime": {
    "value": "2025-06-01T00:00:00Z"
  },
  "reason": "PIU_CANCELLATION_REASON_TERMINATED",
  "quantity": {
    "value": "5000"
  },
  "terminationDatetime": {
    "value": "2025-05-15T00:00:00Z"
  }
}
```

**Properties:**

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| `effectiveDatetime` | [Iso8601 Complete Calendar Date Time](iso8601_complete_calendar_date_time.md) | The effective date and time of the cancellation. | - |
| `quantity` | [Decimal](decimal.md) | The number of units affected by the cancellation. | - |
| `reason` | [Piu Cancellation Reason](piu_cancellation_reason.md) | The reason for the cancellation. See `PiuCancellationReason` for all supported values. | - |
| `terminationDatetime` | [Iso8601 Complete Calendar Date Time](iso8601_complete_calendar_date_time.md) | The date and time the holder's relationship with the issuer was terminated. Only present for TERMINATED cancellation events. | - |