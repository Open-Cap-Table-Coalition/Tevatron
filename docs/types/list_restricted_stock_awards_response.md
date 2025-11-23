### List Restricted Stock Awards Response

**Description:** _The response from the List Restricted Stock Awards endpoint._

**References (1):**
- [Restricted Stock Award](../objects/restricted_stock_award.md)

**Properties:**

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| `nextPageToken` | `STRING` | Submit the `nextPageToken` string as `pageToken` in a subsequent request to retrieve the next page.  If the response omits `nextPageToken`, then there are no subsequent pages. | - |
| `restrictedStockAwards` | [`Array` of [Restricted Stock Award](../objects/restricted_stock_award.md)] | The restricted stock awards from the specified issuer. | - |