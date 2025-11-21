### List Option Exercises Response

**Description:** _The response for the ListOptionExercises endpoint._

**Properties:**
| Property | Type | Description | Required |
| --- | --- | --- | --- |
| `nextPageToken` | `STRING` | Submit the `nextPageToken` string as `pageToken` in a subsequent request to retrieve the next page.  If the response omits `nextPageToken`, then there are no subsequent pages. | - |
| `optionExercises` | [`Array` of [Option Exercise](../objects/option_exercise.md)] | The option exercises from the specified issuer. | - |