### Fair Market Value

**Endpoints:** `GET /v1alpha1/issuers/{issuerId}/fairMarketValues`

**Description:** _The fair market value contains the accepted values of an issuer's stock, specified on a per-share class basis. These values come from the 409A reports that Carta has for the issuer._

**Example:**
```json
{
  "id": "string",
  "effectiveDate": {
    "value": "2014-03-17"
  },
  "expirationDate": {
    "value": "2015-03-16"
  },
  "staleDate": {
    "value": "2015-03-16"
  },
  "shareClassValuations": [
    {
      "shareClassId": "9",
      "shareClassName": "Common",
      "common": true,
      "price": {
        "currencyCode": {
          "value": "USD"
        },
        "amount": {
          "value": "0.20"
        }
      }
    }
  ]
}
```

**Properties:**
| Property | Type | Description | Required |
| --- | --- | --- | --- |
| `effectiveDate` | [Iso8601 Complete Calendar Date](../types/iso8601_complete_calendar_date.md) | The date that this fair market valuation takes effect. | - |
| `expirationDate` | [Iso8601 Complete Calendar Date](../types/iso8601_complete_calendar_date.md) | The date that this fair market valuation will expire. | - |
| `id` | `STRING` | An identifier for the 409A fair market values. <br/>**Constraints:** Max length: 50 | - |
| `shareClassValuations` | [`Array` of [Share Class Valuation](../types/share_class_valuation.md)] | A list of fair market values for each share class. | - |
| `staleDate` | [Iso8601 Complete Calendar Date](../types/iso8601_complete_calendar_date.md) | The date that this fair market valuation becomes stale. | - |