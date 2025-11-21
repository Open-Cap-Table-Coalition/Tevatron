### List Option Grants Response

**Description:** _The response for the ListOptionGrants endpoint._

**Properties:**
| Property | Type | Description | Required |
| --- | --- | --- | --- |
| `nextPageToken` | `STRING` | Submit the `nextPageToken` string as `pageToken` in a subsequent request to retrieve the next page.  If the response omits `nextPageToken`, then there are no subsequent pages. | - |
| `optionGrants` | [`Array` of [Option Grant](../objects/option_grant.md)] | The vesting schedules from the specified issuer. | - |