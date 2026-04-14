### Certificate Cancellation Transaction

**Description:** _A cancellation or termination transaction for a certificate._

**Referenced By (1):**
- [Certificate Transaction Item](certificate_transaction_item.md)

**References (3):**
- [Certificate Cancellation Reason](certificate_cancellation_reason.md)
- [Decimal](decimal.md)
- [Iso8601 Complete Calendar Date Time](iso8601_complete_calendar_date_time.md)

**Example:**
```json
{
  "effectiveDatetime": {
    "value": "2025-06-01T00:00:00Z"
  },
  "reason": "CERTIFICATE_CANCELLATION_REASON_TERMINATED",
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
| `forfeitureDatetime` | [Iso8601 Complete Calendar Date Time](iso8601_complete_calendar_date_time.md) | The date and time unvested shares were forfeited. | - |
| `quantity` | [Decimal](decimal.md) | The number of shares affected by the cancellation. | - |
| `reason` | [Certificate Cancellation Reason](certificate_cancellation_reason.md) | The reason for the cancellation. | - |
| `terminationDatetime` | [Iso8601 Complete Calendar Date Time](iso8601_complete_calendar_date_time.md) | The date and time the holder's relationship with the issuer was terminated. | - |