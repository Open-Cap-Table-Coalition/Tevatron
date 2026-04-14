# Capitalization Table

The top-level capitalization table object.

## Endpoints

- `GET /v1alpha1/issuers/{issuerId}/capitalizationTable` — single


## Properties

| Property | Type | Required | Description |
|---|---|---|---|
| `issuerId` | string | ✓ | The identifier of the issuer. |
| `asOfDate` | [`v1alpha1Iso8601CompleteCalendarDate`](../types/iso8601_complete_calendar_date.md) |  | Data returned in the response reflects the state of the capitalization table as of this date, specified as an [ISO 8601 extended format calendar date](https://en.wikipedia.org/wiki/ISO_8601#Calendar_dates), i.e. 'YYYY-MM-DD'. |
| `summary` | [`v1alpha1CapitalizationTableSummary`](../types/capitalization_table_summary.md) | ✓ | Summary information about the capitalization table. |
| `shareClassSummaries` | [`v1alpha1ShareClassSummary`](../types/share_class_summary.md)[] |  | Per share class summary information. |
| `optionPoolSummaries` | [`v1alpha1OptionPoolSummary`](../types/option_pool_summary.md)[] |  | Per option pool summary information. |
| `warrantBlockSummaries` | [`v1alpha1WarrantBlockSummary`](../types/warrant_block_summary.md)[] |  | Per warrant block summary information. |
| `noteBlockSummaries` | [`v1alpha1NoteBlockSummary`](../types/note_block_summary.md)[] |  | Per note block summary information. |


## Referenced by

_(not embedded in other domain objects)_


---

_Underlying schema: [`v1alpha1CapitalizationTable`](../types/capitalization_table.md)_


[← Back to Domain Index](index.md)
