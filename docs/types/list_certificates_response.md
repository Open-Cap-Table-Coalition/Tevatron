### List Certificates Response

**Description:** _The response from the List Certificates endpoint._

**Properties:**
| Property | Type | Description | Required |
| --- | --- | --- | --- |
| `certificates` | [`Array` of [Certificate](../objects/certificate.md)] | The vesting schedules from the specified issuer. | - |
| `nextPageToken` | `STRING` | Submit the `nextPageToken` string as `pageToken` in a subsequent request to retrieve the next page.  If the response omits `nextPageToken`, then there are no subsequent pages. | - |