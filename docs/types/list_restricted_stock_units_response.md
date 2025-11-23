### List Restricted Stock Units Response

**Description:** _The response from the List Restricted Stock Units endpoint._

**References (1):**
- [Restricted Stock Unit](../objects/restricted_stock_unit.md)

**Properties:**

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| `nextPageToken` | `STRING` | Submit the `nextPageToken` string as `pageToken` in a subsequent request to retrieve the next page.  If the response omits `nextPageToken`, then there are no subsequent pages. | - |
| `restrictedStockUnits` | [`Array` of [Restricted Stock Unit](../objects/restricted_stock_unit.md)] | The restricted stock units from the specified issuer. | - |