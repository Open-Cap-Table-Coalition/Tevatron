### Dividend Details

**Description:** _Details about share class dividends._

**Example:**
```json
{
  "dividendYield": {
    "value": "0.02"
  },
  "dividendAccrualType": "CUMULATIVE",
  "dividendAccrualPeriod": "DAILY",
  "dividendInterestType": "INTEREST_PERIOD_DAILY"
}
```

**Properties:**
| Property | Type | Description | Required |
| --- | --- | --- | --- |
| `dividendAccrualPeriod` | [Dividend Accrual Period](dividend_accrual_period.md) | Cadence upon which dividends are accrued. | - |
| `dividendAccrualType` | [Dividend Accrual Type](dividend_accrual_type.md) | The dividend accrual type for the share class. | - |
| `dividendInterestType` | [Dividend Interest Type](dividend_interest_type.md) | Type of interest used to calculated dividend. | - |
| `dividendYield` | [Decimal](decimal.md) | How much a company pays out in dividends each year relative to its stock price. | - |