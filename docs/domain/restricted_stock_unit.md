# Restricted Stock Unit

A restricted stock unit is a grant of company shares.

## Endpoints

- `GET /v1alpha1/issuers/{issuerId}/restrictedStockUnits` — list
- `GET /v1alpha1/issuers/{issuerId}/restrictedStockUnits/{id}` — single


## Properties

| Property | Type | Required | Description |
|---|---|---|---|
| `id` | string |  | The identifier of the restricted stock unit. |
| `issuerId` | string |  | The identifier of the issuer owning the restricted stock unit. |
| `stakeholderId` | string |  | The identifier of the stakeholder that received the restricted stock unit. |
| `equityIncentivePlanName` | string |  | The name of the equity incentive plan (i.e., option plan) associated with the restricted stock unit. |
| `issueDate` | [`v1alpha1Iso8601CompleteCalendarDate`](../types/iso8601_complete_calendar_date.md) |  | The date the restricted stock unit was issued. |
| `vestingStartDate` | [`v1alpha1Iso8601CompleteCalendarDate`](../types/iso8601_complete_calendar_date.md) |  | The start date of the vesting period for the restricted stock unit, specified as an [ISO 8601 extended format calendar date](https://en.wikipedia.org/wiki/ISO_8601#Calendar_dates), i.e. 'YYYY-MM-DD'. |
| `boardApprovalDate` | [`v1alpha1Iso8601CompleteCalendarDate`](../types/iso8601_complete_calendar_date.md) |  | The date the restricted stock unit received board approval. |
| `stakeholderAcceptanceDate` | [`v1alpha1Iso8601CompleteCalendarDate`](../types/iso8601_complete_calendar_date.md) |  | The date the restricted stock unit was accepted by the stakeholder, specified as an [ISO 8601 extended format calendar date](https://en.wikipedia.org/wiki/ISO_8601#Calendar_dates), i.e. 'YYYY-MM-DD'. |
| `quantity` | [`v1alpha1Decimal`](../types/decimal.md) |  | The total quantity of shares in the restricted stock unit grant. |
| `vestedQuantity` | [`v1alpha1Decimal`](../types/decimal.md) |  | The total quantity of restricted stock units in the grant that have been vested. |
| `releasedQuantity` | [`v1alpha1Decimal`](../types/decimal.md) |  | The total quantity of restricted stock units in the grant that has been settled. |
| `releasePricePerShare` | [`v1alpha1Money`](../types/money.md) |  | The price of each share that has been released from the restricted stock unit grant. |
| `netSettledQuantity` | [`v1alpha1Decimal`](../types/decimal.md) |  | The total quantity of restricted stock units in this grant that have been released to the stakeholder. |
| `securityLabel` | string |  | The label representing this security (restricted stock unit). |
| `vestingEvents` | [`v1alpha1RestrictedStockUnitVestingEvent`](../types/restricted_stock_unit_vesting_event.md)[] |  | The list of all vesting events associated with these restricted stock units. |
| `canceledDate` | [`v1alpha1Iso8601CompleteCalendarDate`](../types/iso8601_complete_calendar_date.md) |  | The date the restricted stock unit was canceled. |
| `terminationDate` | [`v1alpha1Iso8601CompleteCalendarDate`](../types/iso8601_complete_calendar_date.md) |  | The date the restricted stock unit was terminated. |
| `settlements` | [`v1alpha1RestrictedStockUnitSettlement`](../types/restricted_stock_unit_settlement.md)[] |  | The list of all settlements associated with these restricted stock units. |
| `vestingSchedule` | [`issuerssecuritiesv1alpha1VestingSchedule`](../types/issuerssecurities_vesting_schedule.md) |  | The vesting schedule information associated with the restricted stock unit. |
| `canceledQuantity` | [`v1alpha1Decimal`](../types/decimal.md) |  | The number of shares in the restricted stock unit that were canceled. |
| `forfeitedQuantity` | [`v1alpha1Decimal`](../types/decimal.md) |  | The number of shares in the restricted stock unit that were forfeited. |
| `expiredQuantity` | [`v1alpha1Decimal`](../types/decimal.md) |  | The number of shares in the restricted stock unit that expired. |
| `returnedToPoolQuantity` | [`v1alpha1Decimal`](../types/decimal.md) |  | The number of shares in the restricted stock unit that were returned to the pool. |
| `returnedToTreasuryQuantity` | [`v1alpha1Decimal`](../types/decimal.md) |  | The number of shares in the restricted stock unit that were annulled, but not returned to the pool. |
| `lastModifiedDatetime` | [`v1alpha1Iso8601CompleteCalendarDateTime`](../types/iso8601_complete_calendar_date_time.md) |  | The date and time when the restricted stock unit was last modified. |


## Referenced by

_(not embedded in other domain objects)_


---

_Underlying schema: [`v1alpha1RestrictedStockUnit`](../objects/restricted_stock_unit.md)_


[← Back to Domain Index](index.md)
