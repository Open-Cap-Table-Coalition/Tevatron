### Share Class Rights And Preferences

**Description:** _Share class rights and preferences for a preferred share class._

**Referenced By (1):**
- [Preferred Share Class Details](preferred_share_class_details.md)

**References (2):**
- [Decimal](decimal.md)
- [Money](money.md)

**Example:**
```json
{
  "originalIssuePrice": {
    "currencyCode": {
      "value": "USD"
    },
    "amount": {
      "value": "1.77"
    }
  },
  "conversionPrice": {
    "currencyCode": {
      "value": "USD"
    },
    "amount": {
      "value": "1.50"
    }
  },
  "conversionRatio": {
    "value": "0.789"
  },
  "multiplier": {
    "value": "1.00"
  },
  "participating": true,
  "participationCap": {
    "value": "1.00"
  }
}
```

**Properties:**

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| `conversionPrice` | [Money](money.md) | Used to calculate the conversion ratio for the preferred stock into common stock. | - |
| `conversionRatio` | [Decimal](decimal.md) | Conversion will be calculated with `conversionRatio` instead of `conversionPrice` if both are entered.  Conversion will be calculated with `conversionRatio` instead of `conversionPrice` if both are entered. | - |
| `multiplier` | [Decimal](decimal.md) | The multiple of the original Issue price that will be paid out pursuant to the liquidation preferences. | - |
| `originalIssuePrice` | [Money](money.md) | The price that was originally set for that series of preferred stock. | - |
| `participating` | `BOOLEAN` | Indicates that the holders of that preferred share class are paid out at the same time that the common stockholders are paid out. | - |
| `participationCap` | [Decimal](decimal.md) | Blank or zero means there is no cap. No cap means the preferred classes are fully participating. | - |