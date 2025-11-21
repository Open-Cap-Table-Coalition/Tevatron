### Share Class Valuation

**Description:** _The fair market valuation price for a share class._

**Example:**
```json
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
```

**Properties:**
| Property | Type | Description | Required |
| --- | --- | --- | --- |
| `common` | `BOOLEAN` | True if this is a common share class; otherwise, false if this is a preferred share class. | - |
| `price` | [Money](money.md) | The fair market value for the share class. | - |
| `shareClassId` | `STRING` | The identifier of the share class. <br/>**Constraints:** Min length: 1, Max length: 50 | - |
| `shareClassName` | `STRING` | The name of the share class. <br/>**Constraints:** Min length: 1, Max length: 60 | - |