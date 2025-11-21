### Money

**Description:** _Represents an amount of money with its currency type._

**Example:**
```json
{
  "currencyCode": "USD",
  "amount": {
    "value": "1000.77"
  }
}
```

**Properties:**
| Property | Type | Description | Required |
| --- | --- | --- | --- |
| `amount` | [Decimal](decimal.md) | Decimal amount of the specified currency. For example if `currencyCode` is `"USD"`, then amount of 1 is one US dollar. | - |
| `currencyCode` | [Iso4217 Currency Alpha Code](iso4217_currency_alpha_code.md) | The 3-letter currency code defined in ISO 4217. | - |