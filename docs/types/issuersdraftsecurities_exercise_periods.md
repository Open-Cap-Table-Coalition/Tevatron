### Issuersdraftsecurities Exercise Periods

**Description:** _Exercise periods for the draft option grant. If unset, values will be inherited from the equity plan_

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
| `deathExercisePeriod` | [Issuersdraftsecurities Exercise Period](issuersdraftsecurities_exercise_period.md) | The unit of time for the death exercise period. | - |
| `disabilityExerciseCount` | `INTEGER` | The quantity of "periods" (days, months or years) after disability that the stakeholder has to exercise their options. <br/>**Constraints:** Format: `int32` | - |
| `disabilityExercisePeriod` | [Issuersdraftsecurities Exercise Period](issuersdraftsecurities_exercise_period.md) | The unit of time for the disability exercise period. | - |
| `involuntaryTerminationCauseCount` | `INTEGER` | The quantity of "periods" (days, months or years) after involuntary termination that the stakeholder has to exercise their options. <br/>**Constraints:** Format: `int32` | - |
| `involuntaryTerminationCausePeriod` | [Issuersdraftsecurities Exercise Period](issuersdraftsecurities_exercise_period.md) | The unit of time for the involuntary termination cause period. | - |
| `involuntaryTerminationCount` | `INTEGER` | The quantity of "periods" (days, months or years) after involuntary termination that the stakeholder has to exercise their options. <br/>**Constraints:** Format: `int32` | - |
| `involuntaryTerminationPeriod` | [Issuersdraftsecurities Exercise Period](issuersdraftsecurities_exercise_period.md) | The unit of time for the involuntary termination period. | - |
| `retirementExerciseCount` | `INTEGER` | The quantity of "periods" (days, months or years) after retirement that the stakeholder has to exercise their options. <br/>**Constraints:** Format: `int32` | - |
| `retirementExercisePeriod` | [Issuersdraftsecurities Exercise Period](issuersdraftsecurities_exercise_period.md) | The unit of time for the retirement exercise period. | - |
| `voluntaryTerminationCount` | `INTEGER` | The quantity of "periods" (days, months or years) after voluntary termination that the stakeholder has to exercise their options. <br/>**Constraints:** Format: `int32` | - |
| `voluntaryTerminationPeriod` | [Issuersdraftsecurities Exercise Period](issuersdraftsecurities_exercise_period.md) | The unit of time for the voluntary termination period. | - |