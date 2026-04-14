# Fair Market Value

The fair market value contains the accepted values of an issuer's stock, specified on a per-share class basis. These values come from the 409A reports that Carta has for the issuer.

## Endpoints

- `GET /v1alpha1/issuers/{issuerId}/fairMarketValues` — list


## Properties

| Property | Type | Required | Description |
|---|---|---|---|
| `id` | string |  | An identifier for the 409A fair market values. |
| `effectiveDate` | [`v1alpha1Iso8601CompleteCalendarDate`](../types/iso8601_complete_calendar_date.md) |  | The date that this fair market valuation takes effect. |
| `expirationDate` | [`v1alpha1Iso8601CompleteCalendarDate`](../types/iso8601_complete_calendar_date.md) |  | The date that this fair market valuation will expire. |
| `staleDate` | [`v1alpha1Iso8601CompleteCalendarDate`](../types/iso8601_complete_calendar_date.md) |  | The date that this fair market valuation becomes stale. |
| `shareClassValuations` | [`v1alpha1ShareClassValuation`](../types/share_class_valuation.md)[] |  | A list of fair market values for each share class. |


## Referenced by

_(not embedded in other domain objects)_


---

_Underlying schema: [`v1alpha1FairMarketValue`](../objects/fair_market_value.md)_


[← Back to Domain Index](index.md)
