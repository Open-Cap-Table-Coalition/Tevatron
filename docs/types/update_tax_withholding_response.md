### Update Tax Withholding Response

**Description:** _The response for the UpdateTaxWithholding endpoint._

**References (1):**
- [Option Exercise Tax Withholding Line Item](option_exercise_tax_withholding_line_item.md)

**Properties:**

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| `exerciseId` | `STRING` | The identifier of the option exercise tax withholding information was updated for. <br/>**Constraints:** Min length: 1, Max length: 50 | - |
| `issuerId` | `STRING` | The identifier of the issuer that issued the option exercises tax withholding information was updated for. <br/>**Constraints:** Min length: 1, Max length: 50 | - |
| `taxWithholdings` | [`Array` of [Option Exercise Tax Withholding Line Item](option_exercise_tax_withholding_line_item.md)] | The updated tax withholdings. | - |