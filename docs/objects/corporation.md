### Corporation

**Endpoints:** `GET /v1alpha1/corporations`

**Description:** _A corporation._

**Referenced By (1):**
- [List Corporations Response](../types/list_corporations_response.md)

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
| `doingBusinessAsName` | `STRING` | The operating, or doing business as (DBA), name of the corporation. <br/>**Constraints:** Max length: 1000 | - |
| `id` | `STRING` | The identifier of the corporation. <br/>**Constraints:** Max length: 50 | - |
| `legalName` | `STRING` | The legal name of the corporation. <br/>**Constraints:** Max length: 1000 | - |
| `website` | `STRING` | The URL of the corporation’s website. <br/>**Constraints:** Max length: 1000 | - |