### Vesting Period

**Description:** _A vesting period defines a portion of shares that vest._

**Referenced By (1):**
- [Vesting Schedule Template](../objects/vesting_schedule_template.md)

**References (5):**
- [Decimal](decimal.md)
- [Performance Condition](performance_condition.md)
- [Period Unit](period_unit.md)
- [Vesting Method](vesting_method.md)
- [Vesting Occurs](vesting_occurs.md)

**Example:**
```json
{
  "order": 1,
  "percentage": "25",
  "vestingMethod": "MONTHLY",
  "vestingOccurs": "SAME_DAY_AS_START_DATE",
  "length": 12,
  "lengthUnit": "MONTH"
}
```

**Properties:**

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| `cliffLength` | `INTEGER` | The duration until the cliff. <br/>**Constraints:** Format: `int32` | - |
| `cliffLengthUnit` | [Period Unit](period_unit.md) | The unit of the cliff duration (days, months, years). | - |
| `cliffPercentage` | [Decimal](decimal.md) | The percentage of shares that vest at the cliff. | - |
| `immediatePercentage` | [Decimal](decimal.md) | The percentage of shares that vest immediately on the vesting start date. | - |
| `length` | `INTEGER` | The duration of the vesting period. <br/>**Constraints:** Format: `int32` | - |
| `lengthUnit` | [Period Unit](period_unit.md) | The unit of the duration (days, months, years). | - |
| `milestoneName` | `STRING` | The name of the milestone for milestone-based periods. <br/>**Constraints:** Max length: 500 | - |
| `order` | `INTEGER` | The order of this period in the vesting schedule. <br/>**Constraints:** Format: `int32` | - |
| `percentage` | [Decimal](decimal.md) | The percentage of shares that vest in this period. | - |
| `performanceCondition` | [Performance Condition](performance_condition.md) | The performance condition associated with this period. | - |
| `vestingMethod` | [Vesting Method](vesting_method.md) | The frequency at which shares vest. | - |
| `vestingOccurs` | [Vesting Occurs](vesting_occurs.md) | When vesting occurs within each period (e.g., same day as start date, first of month, last of month). | - |