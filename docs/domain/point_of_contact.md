# Point Of Contact

A point of contact for an issuer. Examples include a Legal Admin or an Option Signatory.

## Endpoints

- `GET /v1alpha1/issuers/{issuerId}/pointsOfContact` — list


## Properties

| Property | Type | Required | Description |
|---|---|---|---|
| `issuerId` | string |  | An identifier for the issuer related to the point of contact. |
| `userFullName` | string |  | The point of contact full name. |
| `userEmail` | string |  | The point of contact email. |
| `type` | [`v1alpha1PointOfContactType`](../types/point_of_contact_type.md) |  | The type of point of contact. |


## Referenced by

_(not embedded in other domain objects)_


---

_Underlying schema: [`v1alpha1PointOfContact`](../objects/point_of_contact.md)_


[← Back to Domain Index](index.md)
