### Exercise

**Description:** _The list of all exercises associated with this grant._

**Referenced By (1):**
- [Option Grant](../objects/option_grant.md)

**References (4):**
- [Decimal](decimal.md)
- [Exercise Status](exercise_status.md)
- [Exercise Type](exercise_type.md)
- [Iso8601 Complete Calendar Date](iso8601_complete_calendar_date.md)

**Example:**
```json
{
  "quantity": {
    "value": "2400"
  },
  "fairMarketValueAsOfDate": {
    "value": "2017-10-25"
  },
  "exerciseDate": {
    "value": "2017-10-25"
  },
  "status": "STATUS_COMPLETE",
  "certificateId": "2951",
  "exerciseType": "CASH_EXERCISE",
  "exerciseId": "23HcT4iVfrgYUaJF9txHTaH"
}
```

**Properties:**

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| `certificateId` | `STRING` | The identifier of the certificate that was issued. This field is set if the exercise has been completed and a certificate has been issued. | - |
| `exerciseDate` | [Iso8601 Complete Calendar Date](iso8601_complete_calendar_date.md) | The date when the exercise request was initiated. | - |
| `exerciseId` | `STRING` | The identifier of the exercise. <br/>**Constraints:** Max length: 50 | - |
| `exerciseType` | [Exercise Type](exercise_type.md) | The type of exercise request. | - |
| `fairMarketValueAsOfDate` | [Iso8601 Complete Calendar Date](iso8601_complete_calendar_date.md) | The date of the fair market value relevant to this exercise. | - |
| `qualified` | `BOOLEAN` | *Deprecated*  True if the exercise option grant type is ISO. False otherwise. | - |
| `quantity` | [Decimal](decimal.md) | The number of shares requested to be exercised. | - |
| `status` | [Exercise Status](exercise_status.md) | The status of the exercise request. | - |