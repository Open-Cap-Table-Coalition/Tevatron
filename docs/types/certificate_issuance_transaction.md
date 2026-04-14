### Certificate Issuance Transaction

**Description:** _The issuance transaction for a certificate. Represents the initial issuance of stock._

**Referenced By (1):**
- [Certificate Transaction Item](certificate_transaction_item.md)

**References (4):**
- [Certificate Issuance Reason](certificate_issuance_reason.md)
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
    "value": "10000"
  },
  "acquisitionCost": {
    "currencyCode": {
      "value": "USD"
    },
    "amount": {
      "value": "1.50"
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
| `acquisitionCost` | [Money](money.md) | The total acquisition cost paid by the holder for the shares. | - |
| `equityPlanId` | `STRING` | The identifier of the equity plan from which the certificate was issued. <br/>**Constraints:** Max length: 50 | - |
| `issuanceReason` | [Certificate Issuance Reason](certificate_issuance_reason.md) | How the certificate was created. See `CertificateIssuanceReason` for all supported values. | - |
| `issueDatetime` | [Iso8601 Complete Calendar Date Time](iso8601_complete_calendar_date_time.md) | The date and time the certificate was issued. | - |
| `precededBySecurityId` | `STRING` | The identifier of the security that preceded this certificate (e.g. the option grant that was exercised). May be absent if the certificate was issued directly from the share reserve. <br/>**Constraints:** Max length: 50 | - |
| `quantity` | [Decimal](decimal.md) | The number of shares issued. | - |
| `shareClassId` | `STRING` | The identifier of the share class. May be absent if the plan has no associated share class. <br/>**Constraints:** Max length: 50 | - |
| `vestingScheduleTemplateId` | `STRING` | The identifier of the vesting schedule template. May be absent if the certificate has no vesting schedule. <br/>**Constraints:** Max length: 50 | - |