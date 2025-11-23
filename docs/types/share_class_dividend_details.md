### Share Class Dividend Details

**Description:** _Details related to the dividends of a share class._

**Referenced By (1):**
- [Preferred Share Class Details](preferred_share_class_details.md)

**References (2):**
- [Dividend Details](dividend_details.md)
- [Dividend Type](dividend_type.md)

**Example:**
```json
{
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
```

**Properties:**

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| `dividendDetails` | [Dividend Details](dividend_details.md) | Details for the non-cash dividends for this share class if `dividendType` is `NON_CASH`. | - |
| `dividendType` | [Dividend Type](dividend_type.md) | The type of dividends for the share class. | - |