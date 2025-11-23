### List Stakeholders Response

**Description:** _The response from the List Stakeholders endpoint._

**References (1):**
- [Publicapiissuers Stakeholder](../objects/publicapiissuers_stakeholder.md)

**Properties:**

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| `nextPageToken` | `STRING` | Submit the `nextPageToken` string as `pageToken` in a subsequent request to retrieve the next page.  If the List Stakeholders response omits `nextPageToken`, then there are no subsequent pages. | - |
| `stakeholders` | [`Array` of [Publicapiissuers Stakeholder](../objects/publicapiissuers_stakeholder.md)] | The stakeholders from the specified issuer. | - |