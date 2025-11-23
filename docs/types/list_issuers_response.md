### List Issuers Response

**Description:** _The response for the ListIssuers endpoint._

**References (1):**
- [Issuer](../objects/issuer.md)

**Properties:**

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| `issuers` | [`Array` of [Issuer](../objects/issuer.md)] |  | - |
| `nextPageToken` | `STRING` | Submit the `nextPageToken` string as `pageToken` in a subsequent request to retrieve the next page.  If the List Issuers response omits `nextPageToken`, then there are no subsequent pages. | - |