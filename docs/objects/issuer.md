### Issuer

**Endpoints:** `GET /v1alpha1/issuers`

**Description:** _An issuer._

**Referenced By (2):**
- [Get Issuer Response](../types/get_issuer_response.md)
- [List Issuers Response](../types/list_issuers_response.md)

**Example:**
```json
{
  "id": "611",
  "legalName": "MangoCart, Inc.",
  "doingBusinessAsName": "MangoCart",
  "website": "http://www.example.com/mangocart"
}
```

**Properties:**

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| `doingBusinessAsName` | `STRING` | The operating, or doing business as (DBA), name of the issuer. <br/>**Constraints:** Max length: 1000 | - |
| `id` | `STRING` | The identifier of the issuer. <br/>**Constraints:** Max length: 50 | - |
| `legalName` | `STRING` | The legal name of the issuer. <br/>**Constraints:** Max length: 1000 | - |
| `website` | `STRING` | The URL of the issuer’s website. <br/>**Constraints:** Max length: 1000 | - |