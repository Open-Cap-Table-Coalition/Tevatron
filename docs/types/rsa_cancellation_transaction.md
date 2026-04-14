### Rsa Cancellation Transaction

**Description:** _A cancellation or termination transaction for an RSA._

**Referenced By (1):**
- [Rsa Transaction Item](rsa_transaction_item.md)

**References (3):**
- [Decimal](decimal.md)
- [Iso8601 Complete Calendar Date Time](iso8601_complete_calendar_date_time.md)
- [Rsa Cancellation Reason](rsa_cancellation_reason.md)

**Example:**
```json
{
  "effectiveDatetime": {
    "value": "2025-06-01T00:00:00Z"
  },
  "reason": "RSA_CANCELLATION_REASON_TERMINATED",
  "quantity": {
    "value": "3000"
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
| `reason` | [Rsa Cancellation Reason](rsa_cancellation_reason.md) | The reason for the cancellation. | - |
| `terminationDatetime` | [Iso8601 Complete Calendar Date Time](iso8601_complete_calendar_date_time.md) | The date and time the holder's relationship with the issuer was terminated. | - |