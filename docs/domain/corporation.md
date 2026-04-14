# Corporation

A corporation.

## OCF Equivalent

Carta's `Corporation` is the legal-entity parent of one or more issuers.
OCF has no separate corporation concept — in OCF the legal entity **is** the `Issuer`.


- [`Issuer`](https://open-cap-table-coalition.github.io/Open-Cap-Format-OCF/schema_markdown/schema/objects/Issuer/) — object. OCF collapses corporation and issuer into a single `Issuer` object.

## Endpoints

- `GET /v1alpha1/corporations` — list


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
