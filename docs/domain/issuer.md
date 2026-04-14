# Issuer

An issuer.

## OCF Equivalent

Direct equivalent — both represent the issuing company.


- [`Issuer`](https://open-cap-table-coalition.github.io/Open-Cap-Format-OCF/schema_markdown/schema/objects/Issuer/) — object

## Endpoints

- `GET /v1alpha1/issuers` — list
- `GET /v1alpha1/issuers/{id}` — single


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
