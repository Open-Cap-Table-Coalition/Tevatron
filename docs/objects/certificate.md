### Certificate

**Endpoints:** `GET /v1alpha1/issuers/{issuerId}/certificates`

**Description:** _A certificate is a record of ownership of a company's shares._

**Referenced By (2):**
- [Get Certificate Response](../types/get_certificate_response.md)
- [List Certificates Response](../types/list_certificates_response.md)

**References (4):**
- [Decimal](../types/decimal.md)
- [Iso8601 Complete Calendar Date](../types/iso8601_complete_calendar_date.md)
- [Iso8601 Complete Calendar Date Time](../types/iso8601_complete_calendar_date_time.md)
- [Money](../types/money.md)

**Example:**
```json
{
  "id": "34",
  "issuerId": "7",
  "stakeholderId": "4903",
  "shareClassName": "Series Seed Preferred",
  "issueDate": {
    "value": "2013-04-10"
  },
  "quantity": {
    "value": "150000"
  },
  "securityLabel": "PS-2",
  "pricePerShare": {
    "currencyCode": {
      "value": "USD"
    },
    "amount": {
      "value": "0.27"
    }
  },
  "lastModifiedDatetime": {
    "value": "2024-07-30T09:31:57.000000Z"
  }
}
```

**Properties:**

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| `canceledDate` | [Iso8601 Complete Calendar Date](../types/iso8601_complete_calendar_date.md) | The date the certificate was canceled. | - |
| `canceledQuantity` | [Decimal](../types/decimal.md) | The number of shares in the certificate that were canceled. | - |
| `id` | `STRING` | The identifier of the certificate. <br/>**Constraints:** Max length: 50 | - |
| `issueDate` | [Iso8601 Complete Calendar Date](../types/iso8601_complete_calendar_date.md) | The date the certificate was issued. | - |
| `issuerId` | `STRING` | The identifier of the issuer owning the certificate. <br/>**Constraints:** Min length: 1, Max length: 50 | - |
| `lastModifiedDatetime` | [Iso8601 Complete Calendar Date Time](../types/iso8601_complete_calendar_date_time.md) | The date and time when the certificate was last modified. | - |
| `pricePerShare` | [Money](../types/money.md) | The cost of each share in the certificate. | - |
| `quantity` | [Decimal](../types/decimal.md) | The number of shares in the certificate. | - |
| `returnedToPoolQuantity` | [Decimal](../types/decimal.md) | The number of shares in the certificate that were returned to the pool. | - |
| `returnedToTreasuryQuantity` | [Decimal](../types/decimal.md) | The number of shares in the certificate that were annulled, but not returned to the pool. | - |
| `securityLabel` | `STRING` | The label representing this security (certificate). <br/>**Constraints:** Max length: 50 | - |
| `shareClassName` | `STRING` | The name of the share class for the shares held in this certificate. <br/>**Constraints:** Max length: 100 | - |
| `stakeholderId` | `STRING` | The identifier of the stakeholder holding the certificate. <br/>**Constraints:** Max length: 50 | - |