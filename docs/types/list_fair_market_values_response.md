### List Fair Market Values Response

**Description:** _The response from the List Fair Market Values endpoint._

**References (1):**
- [Fair Market Value](../objects/fair_market_value.md)

**Properties:**

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| `fairMarketValues` | [`Array` of [Fair Market Value](../objects/fair_market_value.md)] | The fair market values from the specified issuer. | - |
| `nextPageToken` | `STRING` | Submit the `nextPageToken` string as `pageToken` in a subsequent request to retrieve the next page.  If the List Fair Market Values response omits `nextPageToken`, then there are no subsequent pages. | - |