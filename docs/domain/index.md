# Domain Objects

Conceptual entities exposed by the Carta Issuer API. These pages unwrap the RPC-style `Get…Response` / `List…Response` envelopes to show the underlying domain objects and the endpoints that serve them. Polymorphic unions and multi-view entities are presented as hub pages with drill-downs to the leaf types.


## Organization

- [Corporation](corporation.md) — A corporation.
- [Issuer](issuer.md) — An issuer.
- [Stakeholder](stakeholder.md) — 5 context-specific views

## Cap Table

- [Capitalization Table](capitalization_table.md) — The top-level capitalization table object.
- [Stakeholder Capitalization Table](stakeholder_capitalization_table.md) — The top-level object that encapsulates an issuer's stakeholder capitalization information.
- [Share Class](share_class.md) — A class of stock issued by an issuer.

## Securities

- [Certificate](certificate.md) — A certificate is a record of ownership of a company's shares.
- [Convertible Note](convertible_note.md) — A convertible note.
- [Option Grant](option_grant.md) — An option grant is a contract that gives an employee the right to purchase a company's stock at a…
- [Restricted Stock Award](restricted_stock_award.md) — A restricted stock award is a grant of company shares.
- [Restricted Stock Unit](restricted_stock_unit.md) — A restricted stock unit is a grant of company shares.
- [Draft Option Grant](draft_option_grant.md) — A draft option grant is an object that is the precursor of an option grant before it is approved,…

## Securities Activity

- [Option Exercise](option_exercise.md) — An option exercise is an event representing a stakeholder exercising their right to purchase shar…
- [Transaction](transaction.md) — polymorphic union, 8 variants

## Reference Data

- [Interest](interest.md) — Interest information.
- [Fair Market Value](fair_market_value.md) — The fair market value contains the accepted values of an issuer's stock, specified on a per-share…
- [Point Of Contact](point_of_contact.md) — A point of contact for an issuer. Examples include a Legal Admin or an Option Signatory.
- [Vesting Schedule Template](vesting_schedule_template.md) — Details of a vesting schedule template.

## Compensation Benchmarks

- [Compensation Benchmarks](compensation_benchmarks.md) — 4-type subsystem

---

[← Back to Home](../index.md) | [API Objects →](../objects/index.md) | [Supporting Types →](../types/index.md)
