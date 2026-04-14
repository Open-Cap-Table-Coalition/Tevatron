# Stakeholder

The spec defines **five** separate `Stakeholder`-related schemas — different projections of the same conceptual entity depending on where it appears. The table below maps each view to its usage context. From a domain-modeling standpoint these are all the same `Stakeholder` aggregate root and you will typically want to merge them in any client-side model.

## OCF Equivalent

All five Carta `Stakeholder` views collapse to OCF's single `Stakeholder` object.
OCF does not split stakeholders by service context — relationships, contact info,
and tax identity all live on one object.


- [`Stakeholder`](https://open-cap-table-coalition.github.io/Open-Cap-Format-OCF/schema_markdown/schema/objects/Stakeholder/) — object

## Endpoints (canonical stakeholder view)

- `GET /v1alpha1/issuers/{issuerId}/stakeholders` — list
- `GET /v1alpha1/issuers/{issuerId}/stakeholders/{id}` — single

## Views

### [`publicapiissuersv1alpha1Stakeholder`](../objects/publicapiissuers_stakeholder.md)

Returned by the public `GET /issuers/{id}/stakeholders` endpoints.

### [`issuerscapitalizationv1alpha1Stakeholder`](../types/issuerscapitalization_stakeholder.md)

Embedded in capitalization table rows.

### [`issuersdraftsecuritiesv1alpha1Stakeholder`](../types/issuersdraftsecurities_stakeholder.md)

Embedded in draft option grant bodies.

### [`publicapiissuersv1alpha1StakeholderRelationship`](../types/publicapiissuers_stakeholder_relationship.md)

Relationship metadata for public stakeholders.

### [`issuersdraftsecuritiesv1alpha1StakeholderRelationship`](../types/issuersdraftsecurities_stakeholder_relationship.md)

Relationship metadata for draft-securities stakeholders.


## Modeling note

A real domain layer over this API should unify these views into a single `Stakeholder` entity with optional context-specific fields. The wire-format split exists because the spec generator exposed each service's projection separately.


[← Back to Domain Index](index.md)
