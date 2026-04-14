# Issuer

An issuer.

## OCF Equivalent

Direct equivalent — both represent the issuing company.


- [`Issuer`](https://open-cap-table-coalition.github.io/Open-Cap-Format-OCF/schema_markdown/schema/objects/Issuer/) — object

## Endpoints

- `GET /v1alpha1/issuers` — list
- `GET /v1alpha1/issuers/{id}` — single


## Shape at a glance

_Quick comparison of field names, types, and required-ness. See the full Carta properties below, or follow the OCF link for full OCF field documentation._

<div class="domain-compare" markdown="1">
<div class="domain-compare__col" markdown="1">
**Carta** — [`v1alpha1Issuer`](../objects/issuer.md)

_An issuer._

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
| `id` | string |  | The identifier of the issuer. |
| `legalName` | string |  | The legal name of the issuer. |
| `doingBusinessAsName` | string |  | The operating, or doing business as (DBA), name of the issuer. |
| `website` | string |  | The URL of the issuer’s website. |


## Referenced by

_(not embedded in other domain objects)_


---

_Underlying schema: [`v1alpha1Issuer`](../objects/issuer.md)_


[← Back to Domain Index](index.md)
