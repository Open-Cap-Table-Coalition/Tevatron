### Option Exercise Tax Withholding Line Item

**Description:** _Tax withholding information for an option exercise, calculated for a specific jurisdiction for a given stakeholder._

**Referenced By (3):**
- [Exercise Service Update Tax Withholding Body](../objects/exercise_service_update_tax_withholding_body.md)
- [Option Exercise](../objects/option_exercise.md)
- [Update Tax Withholding Response](update_tax_withholding_response.md)

**References (3):**
- [Decimal](decimal.md)
- [Jurisdiction](jurisdiction.md)
- [Money](money.md)

**Properties:**

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| `jurisdiction` | [Jurisdiction](jurisdiction.md) | The jurisdiction for which the tax withholding is calculated. | - |
| `name` | `STRING` | The name of the tax withholding line item. <br/>**Constraints:** Max length: 100 | - |
| `rate` | [Decimal](decimal.md) | The tax witholding percentage rate for the specified jurisdiction. | - |
| `taxes` | [Money](money.md) | The tax to withhold for the specified jurisdiction. | - |