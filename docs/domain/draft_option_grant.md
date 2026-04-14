# Draft Option Grant

A draft option grant is an object that is the precursor of an option grant before it is approved, signed, and issued. The "draft" prefix is used to differentiate it from the final option grant object.

## Endpoints

- `POST /v1alpha1/issuers/{issuerId}/draftOptionGrantSets/{draftOptionGrantSetId}/draftOptionGrants` — single _(request body)_
- `POST /v1alpha1/issuers/{issuerId}/draftOptionGrantSets/{draftOptionGrantSetId}/draftOptionGrants` — single
- `GET /v1alpha1/issuers/{issuerId}/draftOptionGrantSets/{draftOptionGrantSetId}/draftOptionGrants/{draftOptionGrantId}` — single


## Properties

| Property | Type | Required | Description |
|---|---|---|---|
| `id` | string |  | Output only. The unique identifier of the draft option grant. |
| `draftOptionGrantSetId` | string |  | Output only. The unique identifier of the draft option grant set. |
| `issuerId` | string |  | Output only. The unique identifier of the issuer. |
| `optionGrantId` | string |  | Output only. The unique identifier of the option grant that is originated by this draft once it is issued. |
| `state` | [`v1alpha1DraftSecurityState`](../types/draft_security_state.md) |  | Output only. The state of the draft option grant. Certain states are read-only and the draft option grant cannot be modified in those states. |
| `stockOptionType` | [`issuersdraftsecuritiesv1alpha1StockOptionType`](../types/issuersdraftsecurities_stock_option_type.md) |  | The type of the option grant. |
| `grantReason` | [`v1alpha1GrantReason`](../types/grant_reason.md) |  | The reason for granting the option. |
| `quantity` | [`v1alpha1Decimal`](../types/decimal.md) |  | The quantity of shares awarded in the option grant. |
| `earlyExercise` | boolean |  | Whether the option grant allows for early exercise. |
| `exercisePrice` | [`v1alpha1Money`](../types/money.md) |  | The exercise price of the option grant. |
| `stakeholder` | [`issuersdraftsecuritiesv1alpha1Stakeholder`](../types/issuersdraftsecurities_stakeholder.md) |  | The stakeholder to whom this security will be issued. |
| `compliance` | [`v1alpha1Compliance`](../types/compliance.md) |  | The compliance details of the stakeholder. |
| `vesting` | [`v1alpha1Vesting`](../types/vesting.md) |  | The vesting details of the option grant. |
| `notes` | string |  | Additional notes about the option grant. |
| `createTime` | [`v1alpha1Iso8601CompleteCalendarDateTime`](../types/iso8601_complete_calendar_date_time.md) |  | Output only. The timestamp when the option grant was created. |
| `updateTime` | [`v1alpha1Iso8601CompleteCalendarDateTime`](../types/iso8601_complete_calendar_date_time.md) |  | Output only. The timestamp when the option grant was last updated. |
| `customLabel` | string |  | A custom identifier for the draft option grant. |
| `boardApproval` | [`v1alpha1BoardApproval`](../types/board_approval.md) |  | The board approval status for the draft option grant. |
| `boardApprovalDate` | [`v1alpha1Date`](../types/date.md) |  | The board approval date for the draft option grant. Only provide if the board_approval status is approved. |
| `grantDate` | [`v1alpha1Date`](../types/date.md) |  | The grant date for the draft option grant. |
| `expirationDate` | [`v1alpha1Date`](../types/date.md) |  | The expiration date for the draft option grant. |
| `exercisePeriods` | [`issuersdraftsecuritiesv1alpha1ExercisePeriods`](../types/issuersdraftsecurities_exercise_periods.md) |  | The exercise periods for the draft option grant. |
| `documents` | [`v1alpha1OptionGrantDocuments`](../types/option_grant_documents.md) |  | Optional documents that are relevant to a draft option grant. |


## Referenced by

_(not embedded in other domain objects)_


---

_Underlying schema: [`v1alpha1DraftOptionGrant`](../types/draft_option_grant.md)_


[← Back to Domain Index](index.md)
