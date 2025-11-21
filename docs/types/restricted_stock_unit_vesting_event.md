### Restricted Stock Unit Vesting Event

**Description:** _Restricted stock unit vesting event information._

**Example:**
```json
{
  "id": "1988",
  "vestDate": {
    "value": "2016-06-01"
  },
  "quantity": {
    "value": "375"
  },
  "performanceCondition": false,
  "vested": true,
  "maxQuantity": {
    "value": "375"
  },
  "targetQuantity": {
    "value": "375"
  },
  "vestedQuantity": {
    "value": "375"
  }
}
```

**Properties:**
| Property | Type | Description | Required |
| --- | --- | --- | --- |
| `id` | `STRING` | The identifier of the restricted stock unit vesting event. <br/>**Constraints:** Max length: 50 | - |
| `maxQuantity` | [Decimal](decimal.md) | The maximum number of shares vested in this vesting event.  For vesting events with performance conditions, this value will be based on the maximum payout defined within the performance condition.  For regular time-based vesting events, this value will be equivalent to the target_payout field. | - |
| `performanceCondition` | `BOOLEAN` | Indicates that this vesting event has associated performance or milestone vesting conditions.  `performanceCondition` will be `true` for milestone- and performance-based vesting events.  For performance-based vesting events, `performanceCondition` indicates that a performance condition exists, not that it has been met. | - |
| `quantity` | [Decimal](decimal.md) | The number of shares being vested in this vesting event by this event’s date.  *Deprecated: use `maxQuantity`, `targetQuantity`, `vestedQuantity` fields instead.*  For vesting events from strictly time-based vesting schedules, this field will be the amount of shares vesting in the tranche represented by this vesting event, regardless of whether the tranche has actually vested.  For vesting events with performance conditions, this field will be set to either: - if the performance condition has not been achieved, the maximum quantity of shares that could be vested - if the performance condition has been achieved, the target quantity of shares that are vested based on the payout details of the performance condition | - |
| `targetQuantity` | [Decimal](decimal.md) | The target number of shares vested in this vesting event.  The target number of shares reflects the number of shares that have vested or should vest within the vesting event independent of any performance condition payout details.  If this vesting event has no performance condition, then this value will reflect the value that is or will be in the `vestedQuantity` field. | - |
| `vestDate` | [Iso8601 Complete Calendar Date](iso8601_complete_calendar_date.md) | The date of the vesting event. For milestone-based vesting events, `vestDate` will be omitted until the security has vested. | - |
| `vested` | `BOOLEAN` | Indicates that this vesting event has vested. | - |
| `vestedQuantity` | [Decimal](decimal.md) | The actual number of shares vested in this vesting event.  This value will only be set if the vesting event is actually vested (i.e., the `vested` field is `true`). Otherwise, if the vesting event is unvested, then this value will be unset. | - |