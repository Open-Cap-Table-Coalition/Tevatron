### List Share Classes Response

**Description:** _The response for the ListShareClasses endpoint._

**References (1):**
- [Share Class](../objects/share_class.md)

**Properties:**

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| `nextPageToken` | `STRING` | Submit the `nextPageToken` string as `pageToken` in a subsequent request to retrieve the next page.  If the List Share Classes response omits `nextPageToken`, then there are no subsequent pages. | - |
| `shareClasses` | [`Array` of [Share Class](../objects/share_class.md)] | The vesting schedules from the specified issuer. | - |