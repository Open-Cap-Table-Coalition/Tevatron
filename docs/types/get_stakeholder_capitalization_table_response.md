### Get Stakeholder Capitalization Table Response

**Description:** _The response for the GetStakeholderCapitalizationTable endpoint._

**Properties:**
| Property | Type | Description | Required |
| --- | --- | --- | --- |
| `nextPageToken` | `STRING` | A page token, which can be provided as the value of the `pageToken` query parameter to retrieve the next page. If this field is omitted, there are no subsequent pages. | - |
| `stakeholderCapitalizationTable` | [Stakeholder Capitalization Table](stakeholder_capitalization_table.md) | Stakeholder Capitalization table. | `REQUIRED` |