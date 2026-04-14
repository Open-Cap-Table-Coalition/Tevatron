### Performance Condition

**Description:** _Details of a performance condition._

**Referenced By (1):**
- [Vesting Period](vesting_period.md)

**References (4):**
- [Decimal](decimal.md)
- [Iso8601 Complete Calendar Date](iso8601_complete_calendar_date.md)
- [Performance Condition Status](performance_condition_status.md)
- [Performance Condition Type](performance_condition_type.md)

**Example:**
```json
{
  "name": "IPO Condition",
  "type": "PERFORMANCE_CONDITION_TYPE_EVENT_NON_MARKET",
  "minPayoutPercentage": "0",
  "maxPayoutPercentage": "100",
  "vestsPostTermination": true,
  "status": "PERFORMANCE_CONDITION_STATUS_NOT_EVALUATED"
}
```

**Properties:**

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| `description` | `STRING` | The description of the performance condition. <br/>**Constraints:** Max length: 2000 | - |
| `evaluationDate` | [Iso8601 Complete Calendar Date](iso8601_complete_calendar_date.md) | The date when the condition was evaluated (ISO 8601 format). | - |
| `maxPayoutPercentage` | [Decimal](decimal.md) | The maximum payout percentage. | - |
| `minPayoutPercentage` | [Decimal](decimal.md) | The minimum payout percentage. | - |
| `name` | `STRING` | The name of the performance condition. <br/>**Constraints:** Max length: 500 | - |
| `payoutPercentage` | [Decimal](decimal.md) | The actual payout percentage after evaluation. | - |
| `status` | [Performance Condition Status](performance_condition_status.md) | The evaluation status of the performance condition. | - |
| `type` | [Performance Condition Type](performance_condition_type.md) | The type of performance condition. | - |
| `vestsPostTermination` | `BOOLEAN` | Whether shares vest after termination if the condition is met. | - |