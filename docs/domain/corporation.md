# Corporation

A corporation.

## OCF Equivalent

Carta's `Corporation` is the legal-entity parent of one or more issuers.
OCF has no separate corporation concept — in OCF the legal entity **is** the `Issuer`.


- [`Issuer`](https://open-cap-table-coalition.github.io/Open-Cap-Format-OCF/schema_markdown/schema/objects/Issuer/) — object. OCF collapses corporation and issuer into a single `Issuer` object.

## Endpoints

- `GET /v1alpha1/corporations` — list


## Properties side-by-side

<div class="domain-compare" markdown="1">
<div class="domain-compare__col" markdown="1">
**Carta** — [`v1alpha1Corporation`](../objects/corporation.md)

_A corporation._

| Property | Type | Required | Description |
|---|---|---|---|
| `id` | string |  | The identifier of the corporation. |
| `legalName` | string |  | The legal name of the corporation. |
| `doingBusinessAsName` | string |  | The operating, or doing business as (DBA), name of the corporation. |
| `website` | string |  | The URL of the corporation’s website. |

</div>
<div class="domain-compare__col" markdown="1">
**OCF** — [`Issuer`](https://open-cap-table-coalition.github.io/Open-Cap-Format-OCF/schema_markdown/schema/objects/Issuer/)

_Object describing the issuer of the cap table (the company whose cap table this is)_

| Property                              | Type                                                                                                                                                                                                                                                                         | Description                                                                                                               | Required   |
| ------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- | ---------- |
| id                                    | `STRING`                                                                                                                                                                                                                                                                     | Identifier for the object                                                                                                 | `REQUIRED` |
| comments                              | [`STRING`]                                                                                                                                                                                                                                                                   | Unstructured text comments related to and stored for the object                                                           | -          |
| object_type                           | **Constant:** `ISSUER`</br>_Defined in [schema/enums/ObjectType](https://open-cap-table-coalition.github.io/Open-Cap-Format-OCF/schema_markdown/schema/enums/ObjectType/)_                                                                                                                                                                                    | Object type field                                                                                                         | `REQUIRED` |
| legal_name                            | `STRING`                                                                                                                                                                                                                                                                     | Legal name of the issuer                                                                                                  | `REQUIRED` |
| dba                                   | `STRING`                                                                                                                                                                                                                                                                     | Doing Business As name                                                                                                    | -          |
| formation_date                        | [schema/types/Date](https://open-cap-table-coalition.github.io/Open-Cap-Format-OCF/schema_markdown/schema/types/Date/)                                                                                                                                                                                                                                        | Date of formation                                                                                                         | `REQUIRED` |
| country_of_formation                  | [schema/types/CountryCode](https://open-cap-table-coalition.github.io/Open-Cap-Format-OCF/schema_markdown/schema/types/CountryCode/)                                                                                                                                                                                                                          | The country where the issuer company was legally formed (ISO 3166-1 alpha-2)                                              | `REQUIRED` |
| country_subdivision_of_formation      | [schema/types/CountrySubdivisionCode](https://open-cap-table-coalition.github.io/Open-Cap-Format-OCF/schema_markdown/schema/types/CountrySubdivisionCode/)                                                                                                                                                                                                    | The code for the state, province, or subdivision where the issuer company was legally formed                              | -          |
| country_subdivision_name_of_formation | `STRING`                                                                                                                                                                                                                                                                     | The text name of state, province, or subdivision where the issuer company was legally formed if the code is not available | -          |
| tax_ids                               | [ [schema/types/TaxID](https://open-cap-table-coalition.github.io/Open-Cap-Format-OCF/schema_markdown/schema/types/TaxID/) ]                                                                                                                                                                                                                                  | The tax ids for this issuer company                                                                                       | -          |
| email                                 | [schema/types/Email](https://open-cap-table-coalition.github.io/Open-Cap-Format-OCF/schema_markdown/schema/types/Email/)                                                                                                                                                                                                                                      | A work email that the issuer company can be reached at                                                                    | -          |
| phone                                 | [schema/types/Phone](https://open-cap-table-coalition.github.io/Open-Cap-Format-OCF/schema_markdown/schema/types/Phone/)                                                                                                                                                                                                                                      | A phone number that the issuer company can be reached at                                                                  | -          |
| address                               | [schema/types/Address](https://open-cap-table-coalition.github.io/Open-Cap-Format-OCF/schema_markdown/schema/types/Address/)                                                                                                                                                                                                                                  | The headquarters address of the issuing company                                                                           | -          |
| initial_shares_authorized             | **ONE OF the Following Types/Objs:**</br>&bull; `Enum - Authorized Shares Types`</br></br>_Description:_ Enumeration of authorized shares types</br></br>**ONE OF:** </br>&bull; NOT APPLICABLE </br>&bull; UNLIMITED</br>&bull; [schema/types/Numeric](https://open-cap-table-coalition.github.io/Open-Cap-Format-OCF/schema_markdown/schema/types/Numeric/) | The initial number of shares authorized for this issuer                                                                   | -          |
</div>
</div>


## Referenced by

_(not embedded in other domain objects)_


---

_Underlying schema: [`v1alpha1Corporation`](../objects/corporation.md)_


[← Back to Domain Index](index.md)
