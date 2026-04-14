### Rsa Issuance Transaction

**Description:** _The issuance transaction for an RSA. Represents the initial grant of restricted stock._

**Referenced By (1):**
- [Rsa Transaction Item](rsa_transaction_item.md)

**References (3):**
- [Decimal](decimal.md)
- [Iso8601 Complete Calendar Date Time](iso8601_complete_calendar_date_time.md)
- [Money](money.md)

**Example:**
```json
{
  "issueDatetime": {
    "value": "2024-01-15T00:00:00Z"
  },
  "quantity": {
    "value": "5000"
  },
  "acquisitionCost": {
    "currencyCode": {
      "value": "USD"
    },
    "amount": {
      "value": "0.001"
    }
  },
  "equityPlanId": "42",
  "shareClassId": "10",
  "vestingScheduleTemplateId": "7"
}
```

**Properties:**

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| `acquisitionCost` | [Money](money.md) | The total acquisition cost paid by the holder for the restricted shares. | - |
| `equityPlanId` | `STRING` | The identifier of the equity plan from which the RSA was issued. <br/>**Constraints:** Max length: 50 | - |
| `issueDatetime` | [Iso8601 Complete Calendar Date Time](iso8601_complete_calendar_date_time.md) | The date and time the RSA was issued. | - |
| `quantity` | [Decimal](decimal.md) | The number of restricted shares granted. | - |
| `shareClassId` | `STRING` | The identifier of the share class. May be absent if the plan has no associated share class. <br/>**Constraints:** Max length: 50 | - |
| `vestingScheduleTemplateId` | `STRING` | The identifier of the vesting schedule template. May be absent if the RSA has no vesting schedule. <br/>**Constraints:** Max length: 50 | - |