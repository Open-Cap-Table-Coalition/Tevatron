# Interest

Interest information.

## Endpoints

- `GET /v1alpha1/issuers/{issuerId}/interests` — list


## Properties

| Property | Type | Required | Description |
|---|---|---|---|
| `id` | string |  | The unique identifier for the interest. |
| `issuerId` | string |  | The unique identifier for the issuer of the interest. |
| `stakeholderId` | string |  | The unique identifier for the stakeholder that the interest is issued to. |
| `interestLabel` | string |  | The label of the interest. |
| `interestTypeName` | string |  | The name of the interest type. |
| `issueDate` | [`v1alpha1Iso8601CompleteCalendarDate`](../types/iso8601_complete_calendar_date.md) |  | The effective date of the interest. |
| `acceptanceDate` | [`v1alpha1Iso8601CompleteCalendarDateTime`](../types/iso8601_complete_calendar_date_time.md) |  | The date the interest was accepted by the holder. |
| `thresholdDetails` | [`v1alpha1ThresholdDetails`](../types/threshold_details.md) |  | Threshold details for the interest. |
| `exercisePrice` | [`v1alpha1Money`](../types/money.md) |  | The strike price at which units of this interest type can be exercised. |
| `originalIssuePrice` | [`v1alpha1Money`](../types/money.md) |  | The price at which units of the interest type were issued. |
| `investedCapital` | [`v1alpha1Money`](../types/money.md) |  | The amount invested by an investor to secure an interest. |
| `accruedValue` | [`v1alpha1Money`](../types/money.md) |  | Value accrued on principal amount as of the effective date. |
| `issuedQuantity` | [`v1alpha1Decimal`](../types/decimal.md) |  | The number of units represented by this interest. |
| `outstandingQuantity` | [`v1alpha1Decimal`](../types/decimal.md) |  | The number of outstanding units, units that are 'active' for the interest. |
| `outstandingVestedQuantity` | [`v1alpha1Decimal`](../types/decimal.md) |  | The number of outstanding vested units. |
| `exercisedQuantity` | [`v1alpha1Decimal`](../types/decimal.md) |  | The number of exercised units. |
| `repurchasedQuantity` | [`v1alpha1Decimal`](../types/decimal.md) |  | The number of repurchased units. |
| `cancelledQuantity` | [`v1alpha1Decimal`](../types/decimal.md) |  | The number of cancelled units. |
| `forfeitedQuantity` | [`v1alpha1Decimal`](../types/decimal.md) |  | The number of forfeited units. |
| `vestingSchedule` | [`issuersinterestsv1alpha1VestingSchedule`](../types/issuersinterests_vesting_schedule.md) |  | Vesting Schedule for the interest if it has vesting behaviour enabled. |


## Referenced by

_(not embedded in other domain objects)_


---

_Underlying schema: [`v1alpha1Interest`](../objects/interest.md)_


[← Back to Domain Index](index.md)
