### Issuerssecurities Exercise Periods

**Description:** _Exercise periods for the option grant. Unset values will be inherited from the equity plan from with the option was granted._

**Referenced By (1):**
- [Option Grant](../objects/option_grant.md)

**References (1):**
- [Issuerssecurities Exercise Period](issuerssecurities_exercise_period.md)

**Example:**
```json
{
  "voluntaryTerminationCount": "1",
  "voluntaryTerminationPeriod": "PTEP_PERIOD_YEAR",
  "involuntaryTerminationCauseCount": "3",
  "involuntaryTerminationCausePeriod": "PTEP_PERIOD_MONTH",
  "involuntaryTerminationCount": "5",
  "involuntaryTerminationPeriod": "PTEP_PERIOD_DAY",
  "deathExerciseCount": "7",
  "deathExercisePeriod": "PTEP_PERIOD_YEAR",
  "disabilityExerciseCount": "9",
  "disabilityExercisePeriod": "PTEP_PERIOD_MONTH",
  "retirementExerciseCount": "11",
  "retirementExercisePeriod": "PTEP_PERIOD_DAY"
}
```

**Properties:**

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| `deathExerciseCount` | `INTEGER` | The quantity of "periods" (days, months or years) after death that the stakeholder has to exercise their options. <br/>**Constraints:** Format: `int32` | - |
| `deathExercisePeriod` | [Issuerssecurities Exercise Period](issuerssecurities_exercise_period.md) | The unit of time for the death exercise period. | - |
| `disabilityExerciseCount` | `INTEGER` | The quantity of "periods" (days, months or years) after disability that the stakeholder has to exercise their options. <br/>**Constraints:** Format: `int32` | - |
| `disabilityExercisePeriod` | [Issuerssecurities Exercise Period](issuerssecurities_exercise_period.md) | The unit of time for the disability exercise period. | - |
| `involuntaryTerminationCauseCount` | `INTEGER` | The quantity of "periods" (days, months or years) after involuntary termination that the stakeholder has to exercise their options. <br/>**Constraints:** Format: `int32` | - |
| `involuntaryTerminationCausePeriod` | [Issuerssecurities Exercise Period](issuerssecurities_exercise_period.md) | The unit of time for the involuntary termination cause period. | - |
| `involuntaryTerminationCount` | `INTEGER` | The quantity of "periods" (days, months or years) after involuntary termination that the stakeholder has to exercise their options. <br/>**Constraints:** Format: `int32` | - |
| `involuntaryTerminationPeriod` | [Issuerssecurities Exercise Period](issuerssecurities_exercise_period.md) | The unit of time for the involuntary termination period. | - |
| `retirementExerciseCount` | `INTEGER` | The quantity of "periods" (days, months or years) after retirement that the stakeholder has to exercise their options. <br/>**Constraints:** Format: `int32` | - |
| `retirementExercisePeriod` | [Issuerssecurities Exercise Period](issuerssecurities_exercise_period.md) | The unit of time for the retirement exercise period. | - |
| `voluntaryTerminationCount` | `INTEGER` | The quantity of "periods" (days, months or years) after voluntary termination that the stakeholder has to exercise their options. <br/>**Constraints:** Format: `int32` | - |
| `voluntaryTerminationPeriod` | [Issuerssecurities Exercise Period](issuerssecurities_exercise_period.md) | The unit of time for the voluntary termination period. | - |