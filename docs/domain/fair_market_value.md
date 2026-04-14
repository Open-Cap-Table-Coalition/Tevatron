# Fair Market Value

The fair market value contains the accepted values of an issuer's stock, specified on a per-share class basis. These values come from the 409A reports that Carta has for the issuer.

## OCF Equivalent

Maps to OCF's `Valuation` — specifically valuations with `valuation_type = "409A"`
(or similar). OCF's Valuation is broader: it also covers post-money/pre-money
financing valuations, not just FMVs.


- [`Valuation`](https://open-cap-table-coalition.github.io/Open-Cap-Format-OCF/schema_markdown/schema/objects/Valuation/) — object. OCF's Valuation covers both 409A FMVs and financing-round valuations.

## Endpoints

- `GET /v1alpha1/issuers/{issuerId}/fairMarketValues` — list


## Shape at a glance

_Quick comparison of field names, types, and required-ness. See the full Carta properties below, or follow the OCF link for full OCF field documentation._

<div class="domain-compare" markdown="1">
<div class="domain-compare__col" markdown="1">
**Carta** — [`v1alpha1FairMarketValue`](../objects/fair_market_value.md)

_The fair market value contains the accepted values of an issuer's stock, specified on a per-share class basis. These values come from the 409A reports that Carta has for the issuer._

| Property | Type | Req |
|---|---|---|
| `id` | string |  |
| `effectiveDate` | [`v1alpha1Iso8601CompleteCalendarDate`](../types/iso8601_complete_calendar_date.md) |  |
| `expirationDate` | [`v1alpha1Iso8601CompleteCalendarDate`](../types/iso8601_complete_calendar_date.md) |  |
| `staleDate` | [`v1alpha1Iso8601CompleteCalendarDate`](../types/iso8601_complete_calendar_date.md) |  |
| `shareClassValuations` | [`v1alpha1ShareClassValuation`](../types/share_class_valuation.md)[] |  |

</div>
<div class="domain-compare__col" markdown="1">
**OCF** — [`Valuation`](https://open-cap-table-coalition.github.io/Open-Cap-Format-OCF/schema_markdown/schema/objects/Valuation/)

_Object describing a valuation used in the cap table_

| Property | Type | Required |
| ------------------------- | -------------------------------------------------------------------------------------------------------------------- | ---------- |
| id | `STRING` | `REQUIRED` |
| comments | [`STRING`] | - |
| object_type | **Constant:** `VALUATION`</br>_Defined in [schema/enums/ObjectType](https://open-cap-table-coalition.github.io/Open-Cap-Format-OCF/schema_markdown/schema/enums/ObjectType/)_ | `REQUIRED` |
| provider | `STRING` | - |
| board_approval_date | [schema/types/Date](https://open-cap-table-coalition.github.io/Open-Cap-Format-OCF/schema_markdown/schema/types/Date/) | - |
| stockholder_approval_date | [schema/types/Date](https://open-cap-table-coalition.github.io/Open-Cap-Format-OCF/schema_markdown/schema/types/Date/) | - |
| price_per_share | [schema/types/Monetary](https://open-cap-table-coalition.github.io/Open-Cap-Format-OCF/schema_markdown/schema/types/Monetary/) | `REQUIRED` |
| effective_date | [schema/types/Date](https://open-cap-table-coalition.github.io/Open-Cap-Format-OCF/schema_markdown/schema/types/Date/) | `REQUIRED` |
| stock_class_id | `STRING` | `REQUIRED` |
| valuation_type | `Enum - Valuation Type`</br></br>_Description:_ Enumeration of valuation types</br></br>**ONE OF:** </br>&bull; 409A | `REQUIRED` |
</div>
</div>


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
