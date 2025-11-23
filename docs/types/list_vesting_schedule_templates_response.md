### List Vesting Schedule Templates Response

**Description:** _The response for the ListVestingScheduleTemplates endpoint._

**References (1):**
- [Vesting Schedule Template](../objects/vesting_schedule_template.md)

**Properties:**

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| `nextPageToken` | `STRING` | Submit the `nextPageToken` string as `pageToken` in a subsequent request to retrieve the next page.  If the List Vesting Schedule Templates response omits `nextPageToken`, then there are no subsequent pages. | - |
| `vestingScheduleTemplates` | [`Array` of [Vesting Schedule Template](../objects/vesting_schedule_template.md)] | A list of vesting schedule templates. | - |