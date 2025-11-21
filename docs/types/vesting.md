### Vesting

**Description:** _Vesting details of the option grant_

**Example:**
```json
{
  "templateId": "6eeb0b6f-84c4-4071-8d94-9f0cefd59230",
  "startDate": {
    "year": 2024,
    "month": 2,
    "day": 29
  },
  "acceleration": {
    "name": "Change in control",
    "terms": "All unvested shares shall vest upon a change of control."
  }
}
```

**Properties:**
| Property | Type | Description | Required |
| --- | --- | --- | --- |
| `acceleration` | [Acceleration](acceleration.md) | Details of accelerated vesting of the draft option grant. | - |
| `startDate` | [Date](date.md) | The effective start date of vesting. | - |
| `templateId` | `STRING` | The template id of the vesting schedule. <br/>**Constraints:** Max length: 100 | - |