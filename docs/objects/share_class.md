### Share Class

**Endpoints:** `GET /v1alpha1/issuers/{issuerId}/shareClasses`

**Description:** _A class of stock issued by an issuer._

**Example:**
```json
{
  "id": "783",
  "issuerId": "7",
  "name": "SeriesB",
  "prefix": "PSB",
  "type": "PREFERRED",
  "authorizedShareCount": {
    "value": "0"
  },
  "parValue": {
    "currencyCode": {
      "value": "USD"
    },
    "amount": {
      "value": "0.0001"
    }
  },
  "seniority": 1,
  "pariPassu": true,
  "preferredShareClassDetails": {
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
}
```

**Properties:**
| Property | Type | Description | Required |
| --- | --- | --- | --- |
| `authorizedShareCount` | [Decimal](../types/decimal.md) | The maximum number of shares allowed to be issued to investors, as laid out in the articles of incorporation. | - |
| `id` | `STRING` | The identifier of the share class. <br/>**Constraints:** Min length: 1, Max length: 50 | - |
| `issuerId` | `STRING` | The identifier of the issuer to which this share class belongs. <br/>**Constraints:** Min length: 1, Max length: 50 | - |
| `name` | `STRING` | The name of the share class. <br/>**Constraints:** Max length: 100 | - |
| `parValue` | [Money](../types/money.md) | The minimum price per share at which the shares must be issued. Is usually set at $0.001 or $0.0001 per share, as stated in the corporate charter. | - |
| `pariPassu` | `BOOLEAN` | Indicates whether this share class has equal seniority to an existing share class. | - |
| `preferredShareClassDetails` | [Preferred Share Class Details](../types/preferred_share_class_details.md) | Preferred share class details when share class type is set to preferred. | - |
| `prefix` | `STRING` | The prefix used to identify the share class. Can only be numbers and letters. For example, CS for Common, PS for Series Seed Preferred, and PA for Series A Preferred. <br/>**Constraints:** Min length: 1, Max length: 25 | - |
| `seniority` | `INTEGER` | Indicates the order in which share holders will get paid. Seniority ranks high to low, with 1 being the highest and will be paid out first.  The higher the number, the less seniority the corresponding share class has. <br/>**Constraints:** Format: `int32` | - |
| `type` | [Share Class Type](../types/share_class_type.md) | The type of the share class. | - |