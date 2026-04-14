# Vesting Schedule Template

Details of a vesting schedule template.

## OCF Equivalent

Closest match is OCF's `VestingTerms`. Both define reusable vesting policies, though
OCF's VestingTerms model is finer-grained (explicit conditions/triggers graph).


- [`VestingTerms`](https://open-cap-table-coalition.github.io/Open-Cap-Format-OCF/schema_markdown/schema/objects/VestingTerms/) — object

## Endpoints

- `GET /v1alpha1/issuers/{issuerId}/vestingScheduleTemplates` — list


## Properties side-by-side

<div class="domain-compare" markdown="1">
<div class="domain-compare__col" markdown="1">
**Carta** — [`v1alpha1VestingScheduleTemplate`](../objects/vesting_schedule_template.md)

_Details of a vesting schedule template._

| Property | Type | Required | Description |
|---|---|---|---|
| `id` | string |  | The identifier of the vesting schedule template. |
| `issuerId` | string |  | The identifier of the issuer to which this vesting schedule template belongs. |
| `name` | string |  | The name of the vesting schedule template. |
| `description` | string |  | The description of the vesting schedule template. |
| `vestingScheduleType` | [`v1alpha1VestingScheduleType`](../types/vesting_schedule_type.md) |  | The type of vesting schedule found within this template. |
| `uuid` | string |  | The UUID of the vesting schedule template. |
| `periods` | [`v1alpha1VestingPeriod`](../types/vesting_period.md)[] |  | The vesting periods that define how shares vest. |

</div>
<div class="domain-compare__col" markdown="1">
**OCF** — [`VestingTerms`](https://open-cap-table-coalition.github.io/Open-Cap-Format-OCF/schema_markdown/schema/objects/VestingTerms/)

_Object describing the terms under which a security vests_

| Property           | Type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Description                                                                     | Required   |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ---------- |
| id                 | `STRING`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Identifier for the object                                                       | `REQUIRED` |
| comments           | [`STRING`]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Unstructured text comments related to and stored for the object                 | -          |
| object_type        | **Constant:** `VESTING_TERMS`</br>_Defined in [schema/enums/ObjectType](https://open-cap-table-coalition.github.io/Open-Cap-Format-OCF/schema_markdown/schema/enums/ObjectType/)_                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Object type field                                                               | `REQUIRED` |
| name               | `STRING`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Concise name for the vesting schedule                                           | `REQUIRED` |
| description        | `STRING`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Detailed description of the vesting schedule                                    | `REQUIRED` |
| allocation_type    | `Enum - Allocation Type`</br></br>_Description:_ Enumeration of allocation types for vesting terms. Using an example of 18 shares split across 4 tranches, each allocation type results in a different schedule as follows: </br>  1.  Cumulative Rounding (5 - 4 - 5 - 4)</br>  2.  Cumulative Round Down (4 - 5 - 4 - 5)</br>  3.  Front Loaded (5 - 5 - 4 - 4)</br>  4.  Back Loaded (4 - 4 - 5 - 5)</br>  5.  Front Loaded to Single Tranche (6 - 4 - 4 - 4)</br>  6.  Back Loaded to Single Tranche (4 - 4 - 4 - 6)</br>  7.  Fractional (4.5 - 4.5 - 4.5 - 4.5)</br></br>**ONE OF:** </br>&bull; CUMULATIVE_ROUNDING </br>&bull; CUMULATIVE_ROUND_DOWN </br>&bull; FRONT_LOADED </br>&bull; BACK_LOADED </br>&bull; FRONT_LOADED_TO_SINGLE_TRANCHE </br>&bull; BACK_LOADED_TO_SINGLE_TRANCHE </br>&bull; FRACTIONAL | Allocation/rounding type for the vesting schedule                               | `REQUIRED` |
| vesting_conditions | [ [schema/types/vesting/VestingCondition](https://open-cap-table-coalition.github.io/Open-Cap-Format-OCF/schema_markdown/schema/types/vesting/VestingCondition/) ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Conditions and triggers that describe the graph of vesting schedules and events | `REQUIRED` |
</div>
</div>


## Referenced by

_(not embedded in other domain objects)_


---

_Underlying schema: [`v1alpha1VestingScheduleTemplate`](../objects/vesting_schedule_template.md)_


[← Back to Domain Index](index.md)
