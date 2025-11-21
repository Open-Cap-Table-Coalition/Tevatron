### List Corporations Response

**Description:** _The response for the ListCorporations endpoint._

**Properties:**
| Property | Type | Description | Required |
| --- | --- | --- | --- |
| `corporations` | [`Array` of [Corporation](../objects/corporation.md)] |  | - |
| `nextPageToken` | `STRING` | Submit the `nextPageToken` string as `pageToken` in a subsequent request to retrieve the next page.  If the List Corporations response omits `nextPageToken`, then there are no subsequent pages. | - |