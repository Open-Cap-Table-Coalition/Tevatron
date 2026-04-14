# Corporation

A corporation.

## OCF Equivalent

Carta's `Corporation` is the legal-entity parent of one or more issuers.
OCF has no separate corporation concept — in OCF the legal entity **is** the `Issuer`.


- [`Issuer`](https://open-cap-table-coalition.github.io/Open-Cap-Format-OCF/schema_markdown/schema/objects/Issuer/) — object. OCF collapses corporation and issuer into a single `Issuer` object.

## Endpoints

- `GET /v1alpha1/corporations` — list


## Shape at a glance

_Quick comparison of field names, types, and required-ness. See the full Carta properties below, or follow the OCF link for full OCF field documentation._

<div class="domain-compare" markdown="1">
<div class="domain-compare__col" markdown="1">
**Carta** — [`v1alpha1Corporation`](../objects/corporation.md)

_A corporation._

| Property | Type | Req |
|---|---|---|
| `id` | string |  |
| `legalName` | string |  |
| `doingBusinessAsName` | string |  |
| `website` | string |  |

</div>
<div class="domain-compare__col" markdown="1">
**OCF** — [`Issuer`](https://open-cap-table-coalition.github.io/Open-Cap-Format-OCF/schema_markdown/schema/objects/Issuer/)

_Object describing the issuer of the cap table (the company whose cap table this is)_

| Property | Type | Required |
| ------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| id | `STRING` | `REQUIRED` |
| comments | [`STRING`] | - |
| object_type | **Constant:** `ISSUER`</br>_Defined in [schema/enums/ObjectType](https://open-cap-table-coalition.github.io/Open-Cap-Format-OCF/schema_markdown/schema/enums/ObjectType/)_ | `REQUIRED` |
| legal_name | `STRING` | `REQUIRED` |
| dba | `STRING` | - |
| formation_date | [schema/types/Date](https://open-cap-table-coalition.github.io/Open-Cap-Format-OCF/schema_markdown/schema/types/Date/) | `REQUIRED` |
| country_of_formation | [schema/types/CountryCode](https://open-cap-table-coalition.github.io/Open-Cap-Format-OCF/schema_markdown/schema/types/CountryCode/) | `REQUIRED` |
| country_subdivision_of_formation | [schema/types/CountrySubdivisionCode](https://open-cap-table-coalition.github.io/Open-Cap-Format-OCF/schema_markdown/schema/types/CountrySubdivisionCode/) | - |
| country_subdivision_name_of_formation | `STRING` | - |
| tax_ids | [ [schema/types/TaxID](https://open-cap-table-coalition.github.io/Open-Cap-Format-OCF/schema_markdown/schema/types/TaxID/) ] | - |
| email | [schema/types/Email](https://open-cap-table-coalition.github.io/Open-Cap-Format-OCF/schema_markdown/schema/types/Email/) | - |
| phone | [schema/types/Phone](https://open-cap-table-coalition.github.io/Open-Cap-Format-OCF/schema_markdown/schema/types/Phone/) | - |
| address | [schema/types/Address](https://open-cap-table-coalition.github.io/Open-Cap-Format-OCF/schema_markdown/schema/types/Address/) | - |
| initial_shares_authorized | **ONE OF the Following Types/Objs:**</br>&bull; `Enum - Authorized Shares Types`</br></br>_Description:_ Enumeration of authorized shares types</br></br>**ONE OF:** </br>&bull; NOT APPLICABLE </br>&bull; UNLIMITED</br>&bull; [schema/types/Numeric](https://open-cap-table-coalition.github.io/Open-Cap-Format-OCF/schema_markdown/schema/types/Numeric/) | - |
</div>
</div>


## Properties

| Property | Type | Required | Description |
|---|---|---|---|
| `id` | string |  | The identifier of the corporation. |
| `legalName` | string |  | The legal name of the corporation. |
| `doingBusinessAsName` | string |  | The operating, or doing business as (DBA), name of the corporation. |
| `website` | string |  | The URL of the corporation’s website. |


## Referenced by

_(not embedded in other domain objects)_


---

_Underlying schema: [`v1alpha1Corporation`](../objects/corporation.md)_


[← Back to Domain Index](index.md)
