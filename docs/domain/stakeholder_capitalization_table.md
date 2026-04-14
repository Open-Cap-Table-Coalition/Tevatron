# Stakeholder Capitalization Table

The top-level object that encapsulates an issuer's stakeholder capitalization information.

## Endpoints

- `GET /v1alpha1/issuers/{issuerId}/stakeholderCapitalizationTable` — single


## Properties

| Property | Type | Required | Description |
|---|---|---|---|
| `issuerId` | string | ✓ | The identifier of the issuer. |
| `asOfDate` | [`v1alpha1Iso8601CompleteCalendarDate`](../types/iso8601_complete_calendar_date.md) | ✓ | Data returned in the response reflects the state of the capitalization table as of this date, specified as an [ISO 8601 extended format calendar date](https://en.wikipedia.org/wiki/ISO_8601#Calendar_dates), i.e. 'YYYY-MM-DD'. |
| `stakeholderGroups` | [`v1alpha1StakeholderGroup`](../types/stakeholder_group.md)[] |  | List of stakeholder groups. |


## Referenced by

_(not embedded in other domain objects)_


---

_Underlying schema: [`v1alpha1StakeholderCapitalizationTable`](../types/stakeholder_capitalization_table.md)_


[← Back to Domain Index](index.md)
