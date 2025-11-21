### Option Exercise Tax Withholding Line Item

**Description:** _Tax withholding information for an option exercise, calculated for a specific jurisdiction for a given stakeholder._

**Properties:**
| Property | Type | Description | Required |
| --- | --- | --- | --- |
| `jurisdiction` | [Jurisdiction](jurisdiction.md) | The jurisdiction for which the tax withholding is calculated. | - |
| `name` | `STRING` | The name of the tax withholding line item. <br/>**Constraints:** Max length: 100 | - |
| `rate` | [Decimal](decimal.md) | The tax witholding percentage rate for the specified jurisdiction. | - |
| `taxes` | [Money](money.md) | The tax to withhold for the specified jurisdiction. | - |