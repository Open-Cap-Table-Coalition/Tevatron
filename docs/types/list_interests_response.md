### List Interests Response

**Description:** _The response from the List Interests endpoint._

**Properties:**
| Property | Type | Description | Required |
| --- | --- | --- | --- |
| `asOfDate` | [Iso8601 Complete Calendar Date](iso8601_complete_calendar_date.md) | The date as of which the interests information was requested. This field will default to the date when the interest information was retrieved (i.e., today's date). | `REQUIRED` |
| `interests` | [`Array` of [Interest](../objects/interest.md)] | The interests for the specified issuer. | `REQUIRED` |
| `nextPageToken` | `STRING` | Submit the `nextPageToken` string as `pageToken` in a subsequent request to retrieve the next page.  If the response omits `nextPageToken`, then there are no subsequent pages. | - |