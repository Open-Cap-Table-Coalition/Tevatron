### Piu Issuance Transaction

**Description:** _The issuance transaction for a PIU. Represents the initial issuance of the profits interest unit._

**Referenced By (1):**
- [Piu Transaction Item](piu_transaction_item.md)

**References (4):**
- [Decimal](decimal.md)
- [Iso8601 Complete Calendar Date Time](iso8601_complete_calendar_date_time.md)
- [Money](money.md)
- [Piu Issuance Reason](piu_issuance_reason.md)

**Example:**
```json
{
  "issueDatetime": {
    "value": "2024-01-15T00:00:00Z"
  },
  "quantity": {
    "value": "10000"
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
  "vestingScheduleTemplateId": "7",
  "issuanceReason": "PIU_ISSUANCE_REASON_ISSUED_FROM_SHARE_RESERVE"
}
```

**Properties:**

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| `acquisitionCost` | [Money](money.md) | The acquisition cost of the PIU. May be absent if no cost was paid. | - |
| `equityPlanId` | `STRING` | The identifier of the equity plan under which the PIU was issued. May be absent if not plan-associated. <br/>**Constraints:** Max length: 50 | - |
| `issuanceReason` | [Piu Issuance Reason](piu_issuance_reason.md) | The reason the PIU was created. See `PiuIssuanceReason` for all supported values. | - |
| `issueDatetime` | [Iso8601 Complete Calendar Date Time](iso8601_complete_calendar_date_time.md) | The date and time the PIU was issued. | - |
| `precededBySecurityId` | `STRING` | The identifier of the security that preceded this PIU (e.g. the certificate that was transferred). May be absent if the PIU was issued directly from the share reserve. <br/>**Constraints:** Max length: 50 | - |
| `quantity` | [Decimal](decimal.md) | The number of units issued. | - |
| `shareClassId` | `STRING` | The identifier of the share class associated with the PIU. <br/>**Constraints:** Max length: 50 | - |
| `vestingScheduleTemplateId` | `STRING` | The identifier of the vesting schedule template. May be absent if the PIU has no vesting schedule. <br/>**Constraints:** Max length: 50 | - |