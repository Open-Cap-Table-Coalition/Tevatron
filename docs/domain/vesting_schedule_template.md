# Vesting Schedule Template

Details of a vesting schedule template.

## OCF Equivalent

Closest match is OCF's `VestingTerms`. Both define reusable vesting policies, though
OCF's VestingTerms model is finer-grained (explicit conditions/triggers graph).


- [`VestingTerms`](https://open-cap-table-coalition.github.io/Open-Cap-Format-OCF/schema_markdown/schema/objects/VestingTerms/) — object

## Endpoints

- `GET /v1alpha1/issuers/{issuerId}/vestingScheduleTemplates` — list


## Properties

| Property | Type | Required | Description |
|---|---|---|---|
| `id` | string |  | The identifier of the vesting schedule template. |
| `issuerId` | string |  | The identifier of the issuer to which this vesting schedule template belongs. |
| `name` | string |  | The name of the vesting schedule template. |
| `description` | string |  | The description of the vesting schedule template. |
| `vestingScheduleType` | [`v1alpha1VestingScheduleType`](../types/vesting_schedule_type.md) |  | The type of vesting schedule found within this template. |
| `uuid` | string |  | The UUID of the vesting schedule template. |
| `periods` | [`v1alpha1VestingPeriod`](../types/vesting_period.md)[] |  | The vesting periods that define how shares vest. |


## Referenced by

_(not embedded in other domain objects)_


---

_Underlying schema: [`v1alpha1VestingScheduleTemplate`](../objects/vesting_schedule_template.md)_


[← Back to Domain Index](index.md)
