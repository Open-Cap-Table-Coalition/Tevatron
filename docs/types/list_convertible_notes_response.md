### List Convertible Notes Response

**Description:** _The response from the `ListConvertibleNotes` endpoint._

**Properties:**
| Property | Type | Description | Required |
| --- | --- | --- | --- |
| `convertibleNotes` | [`Array` of [Convertible Note](../objects/convertible_note.md)] | The convertible notes returned in the `ListConvertibleNotes` response. | - |
| `nextPageToken` | `STRING` | Submit the `nextPageToken` string as `pageToken` in a subsequent request to retrieve the next page. If the `ListConvertibleNotes` response omits `nextPageToken`, then there are no subsequent pages. | - |