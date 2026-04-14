# Option Grant

An option grant is a contract that gives an employee the right to purchase a company's stock at a set price.

## Endpoints

- `GET /v1alpha1/issuers/{issuerId}/optionGrants` — list
- `GET /v1alpha1/issuers/{issuerId}/optionGrants/{id}` — single


## Properties

| Property | Type | Required | Description |
|---|---|---|---|
| `id` | string |  | The identifier of the option grant. |
| `issuerId` | string |  | The identifier of the issuer that issued the option grant. |
| `stakeholderId` | string |  | The identifier of the stakeholder that holds the option grant. |
| `equityIncentivePlanName` | string |  | The name of the equity incentive plan (i.e., option plan) associated with this option grant. |
| `issueDate` | [`v1alpha1Iso8601CompleteCalendarDate`](../types/iso8601_complete_calendar_date.md) |  | The date the option grant was issued. |
| `vestingStartDate` | [`v1alpha1Iso8601CompleteCalendarDate`](../types/iso8601_complete_calendar_date.md) |  | The date the option grant began vesting. |
| `boardApprovalDate` | [`v1alpha1Iso8601CompleteCalendarDate`](../types/iso8601_complete_calendar_date.md) |  | The date the option grant received board approval. |
| `stakeholderAcceptanceDate` | [`v1alpha1Iso8601CompleteCalendarDate`](../types/iso8601_complete_calendar_date.md) |  | The date the option grant was accepted by the stakeholder. |
| `canceledDate` | [`v1alpha1Iso8601CompleteCalendarDate`](../types/iso8601_complete_calendar_date.md) |  | The date when this option grant was canceled. |
| `grantExpirationDate` | [`v1alpha1Iso8601CompleteCalendarDate`](../types/iso8601_complete_calendar_date.md) |  | The expiration date of the option grant (commonly 10 years from the grant issuance date). |
| `lastExercisableDate` | [`v1alpha1Iso8601CompleteCalendarDate`](../types/iso8601_complete_calendar_date.md) |  | The last date the stakeholder can exercise the option grant. |
| `disqualificationDate` | [`v1alpha1Iso8601CompleteCalendarDate`](../types/iso8601_complete_calendar_date.md) |  | The date this option grant became disqualified. |
| `isoNsoSplit` | boolean |  | True if the grant has ISO/NSO split. False otherwise. Learn more about [the ISO $100K limit and ISO/NSO splits](https://support.carta.com/s/article/100k-rule). |
| `stockOptionType` | [`issuerssecuritiesv1alpha1StockOptionType`](../types/issuerssecurities_stock_option_type.md) |  | The stock option type at time of issuance. For grants issued as ISO that subsequently failed to meet ISO qualifications, the type will remain ISO. Refer to the disqualification date for information regarding the disqualification of the grant's ISO shares. |
| `quantity` | [`v1alpha1Decimal`](../types/decimal.md) |  | The total number of options in the grant. |
| `outstandingQuantity` | [`v1alpha1Decimal`](../types/decimal.md) |  | The total quantity of stock options from this grant that have not been exercised, expired, forfeited, or canceled |
| `vestedQuantity` | [`v1alpha1Decimal`](../types/decimal.md) |  | The total quantity of stock options from this grant that have vested. |
| `exercisedQuantity` | [`v1alpha1Decimal`](../types/decimal.md) |  | The total quantity of stock options from this grant that have been exercised into shares. |
| `exercisePrice` | [`v1alpha1Money`](../types/money.md) |  | The exercise price of the options in the grant. |
| `securityLabel` | string |  | The label representing this security (option grant). |
| `earlyExercisable` | boolean |  | True if the option grant is eligible for early exercising; false if the option grant is not eligible for early exercising. |
| `vestingEvents` | [`v1alpha1OptionGrantVestingEvent`](../types/option_grant_vesting_event.md)[] |  | The list of all vesting events associated with this grant. For time based vesting events, both past and future vesting details will be available. For performance and milestone based vesting, only achieved vesting events will be available. |
| `exercises` | [`v1alpha1Exercise`](../types/exercise.md)[] |  | The list of all exercises associated with this grant. |
| `terminationDate` | [`v1alpha1Iso8601CompleteCalendarDate`](../types/iso8601_complete_calendar_date.md) |  | The date that the option grant was terminated. This commonly matches the date the company's relationship with the stakeholder was terminated. |
| `vestingSchedule` | [`issuerssecuritiesv1alpha1VestingSchedule`](../types/issuerssecurities_vesting_schedule.md) |  | The vesting schedule information associated with the restricted stock award. |
| `canceledQuantity` | [`v1alpha1Decimal`](../types/decimal.md) |  | The number of options in the grant that were canceled. |
| `forfeitedQuantity` | [`v1alpha1Decimal`](../types/decimal.md) |  | The number of options in the grant that were forfeited. |
| `expiredQuantity` | [`v1alpha1Decimal`](../types/decimal.md) |  | The number of options in the grant that expired. |
| `returnedToPoolQuantity` | [`v1alpha1Decimal`](../types/decimal.md) |  | The number of options in the grant that were returned to the pool. |
| `returnedToTreasuryQuantity` | [`v1alpha1Decimal`](../types/decimal.md) |  | The number of options in the grant that were annulled, but not returned to the pool. |
| `lastModifiedDatetime` | [`v1alpha1Iso8601CompleteCalendarDateTime`](../types/iso8601_complete_calendar_date_time.md) |  | The date and time when the option grant was last modified. |
| `exercisePeriods` | [`issuerssecuritiesv1alpha1ExercisePeriods`](../types/issuerssecurities_exercise_periods.md) |  | The exercise periods for the option grant. Unset values within this field will be inherited from the equity plan from with the option was granted. |


## Referenced by

_(not embedded in other domain objects)_


---

_Underlying schema: [`v1alpha1OptionGrant`](../objects/option_grant.md)_


[← Back to Domain Index](index.md)
