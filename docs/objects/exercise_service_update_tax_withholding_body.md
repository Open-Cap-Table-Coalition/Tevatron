### Exercise Service Update Tax Withholding Body

**Endpoints:** `POST /v1alpha1/issuers/{issuerId}/optionExercises/{exerciseId}:updateTaxWithholding`

**Description:** _The request for the UpdateTaxWithholding endpoint._

**Properties:**
| Property | Type | Description | Required |
| --- | --- | --- | --- |
| `taxWithholdings` | [`Array` of [Option Exercise Tax Withholding Line Item](../types/option_exercise_tax_withholding_line_item.md)] | The tax withholdings information to update. | - |