### Preferred Share Class Details

**Description:** _Details of a preferred share class, split into rights and preferences details and dividend details._

**Referenced By (1):**
- [Share Class](../objects/share_class.md)

**References (2):**
- [Share Class Dividend Details](share_class_dividend_details.md)
- [Share Class Rights And Preferences](share_class_rights_and_preferences.md)

**Example:**
```json
{
  "rightsAndPreferences": {
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
  },
  "dividendDetails": {
    "dividendType": "CASH",
    "dividendDetails": {
      "dividendYield": {
        "value": "0.02"
      },
      "dividendAccrualType": "CUMULATIVE",
      "dividendAccrualPeriod": "DAILY",
      "dividendInterestType": "INTEREST_PERIOD_DAILY"
    }
  }
}
```

**Properties:**

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| `dividendDetails` | [Share Class Dividend Details](share_class_dividend_details.md) | The dividend details for the preferred share class. | - |
| `rightsAndPreferences` | [Share Class Rights And Preferences](share_class_rights_and_preferences.md) | The rights and preferences for the preferred share class. | - |