### Issuersinterests Vesting Schedule

**Description:** _Vesting Schedule Details for the interest._

**Example:**
```json
{
  "name": "Split 50% 1/5 yearly, 50% annual performance goal",
  "startDate": {
    "value": "2019-08-20"
  }
}
```

**Properties:**
| Property | Type | Description | Required |
| --- | --- | --- | --- |
| `name` | `STRING` | The vesting plan name associated with the interest. | - |
| `startDate` | [Iso8601 Complete Calendar Date](iso8601_complete_calendar_date.md) | The vesting start date for the interest. | - |