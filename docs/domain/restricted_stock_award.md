# Restricted Stock Award

A restricted stock award is a grant of company shares.

## Endpoints

- `GET /v1alpha1/issuers/{issuerId}/restrictedStockAwards` — list
- `GET /v1alpha1/issuers/{issuerId}/restrictedStockAwards/{id}` — single


## Properties

| Property | Type | Required | Description |
|---|---|---|---|
| `id` | string |  | The identifier of the restricted stock award. |
| `issuerId` | string |  | The identifier of the issuer owning the restricted stock award. |
| `stakeholderId` | string |  | The identifier of the stakeholder that holds the restricted stock award. |
| `equityIncentivePlanName` | string |  | The name of the equity incentive plan (i.e., option plan) associated with this restricted stock award. |
| `shareClassName` | string |  | The name of the share class that this restricted stock award belongs to. |
| `issueDate` | [`v1alpha1Iso8601CompleteCalendarDate`](../types/iso8601_complete_calendar_date.md) |  | The date the restricted stock award was issued. |
| `vestingStartDate` | [`v1alpha1Iso8601CompleteCalendarDate`](../types/iso8601_complete_calendar_date.md) |  | The start date of the vesting period for the restricted stock award. |
| `boardApprovalDate` | [`v1alpha1Iso8601CompleteCalendarDate`](../types/iso8601_complete_calendar_date.md) |  | The date the restricted stock award received board approval. |
| `stakeholderAcceptanceDate` | [`v1alpha1Iso8601CompleteCalendarDate`](../types/iso8601_complete_calendar_date.md) |  | The date the restricted stock award was accepted by the stakeholder. |
| `canceledDate` | [`v1alpha1Iso8601CompleteCalendarDate`](../types/iso8601_complete_calendar_date.md) |  | The date the restricted stock award was canceled. |
| `terminationDate` | [`v1alpha1Iso8601CompleteCalendarDate`](../types/iso8601_complete_calendar_date.md) |  | The date the restricted stock award was terminated. This commonly matches the date the company's relationship with the stakeholder was terminated. |
| `quantity` | [`v1alpha1Decimal`](../types/decimal.md) |  | The number of restricted stock units in the award. |
| `vestedQuantity` | [`v1alpha1Decimal`](../types/decimal.md) |  | The number of vested shares in the stock award. |
| `securityLabel` | string |  | The label representing this security (restricted stock award). |
| `pricePerShare` | [`v1alpha1Money`](../types/money.md) |  | The cost of each share in the restricted stock award. |
| `vestingEvents` | [`v1alpha1RestrictedStockAwardVestingEvent`](../types/restricted_stock_award_vesting_event.md)[] |  | The list of all vesting events associated with the restricted stock award. |
| `vestingSchedule` | [`issuerssecuritiesv1alpha1VestingSchedule`](../types/issuerssecurities_vesting_schedule.md) |  | The vesting schedule information associated with the restricted stock award. |
| `canceledQuantity` | [`v1alpha1Decimal`](../types/decimal.md) |  | The number of shares in the restricted stock award that were canceled. |
| `returnedToPoolQuantity` | [`v1alpha1Decimal`](../types/decimal.md) |  | The number of shares in the restricted stock award that were returned to the pool. |
| `returnedToTreasuryQuantity` | [`v1alpha1Decimal`](../types/decimal.md) |  | The number of shares in the restricted stock award that were annulled, but not returned to the pool. |
| `lastModifiedDatetime` | [`v1alpha1Iso8601CompleteCalendarDateTime`](../types/iso8601_complete_calendar_date_time.md) |  | The date and time when the restricted stock award was last modified. |


## Referenced by

_(not embedded in other domain objects)_


---

_Underlying schema: [`v1alpha1RestrictedStockAward`](../objects/restricted_stock_award.md)_


[← Back to Domain Index](index.md)
