### Date

**Description:** _* A full date, with non-zero year, month and day values
* A month and day value, with a zero year, e.g. an anniversary
* A year on its own, with zero month and day values
* A year and month value, with a zero day, e.g. a credit card expiration date_

**Referenced By (2):**
- [Draft Option Grant](draft_option_grant.md)
- [Vesting](vesting.md)

**Properties:**

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| `day` | `INTEGER` | Day of month. Must be from 1 to 31 and valid for the year and month, or 0 if specifying a year by itself or a year and month where the day is not significant. <br/>**Constraints:** Format: `int32` | - |
| `month` | `INTEGER` | Month of year. Use 0 if specifying a year without a month and day. <br/>**Constraints:** Format: `int32` | - |
| `year` | `INTEGER` | Year of date. Use 0 if specifying a date without a year. <br/>**Constraints:** Format: `int32` | - |