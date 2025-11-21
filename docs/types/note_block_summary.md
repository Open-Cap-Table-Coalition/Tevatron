### Note Block Summary

**Description:** _Note block summary information._

**Example:**
```json
{
  "noteBlockId": "4",
  "cashRaised": {
    "currencyCode": {
      "value": "USD"
    },
    "amount": {
      "value": "1075000.00"
    }
  },
  "principal": {
    "currencyCode": {
      "value": "USD"
    },
    "amount": {
      "value": "1075000.00"
    }
  },
  "interest": {
    "currencyCode": {
      "value": "USD"
    },
    "amount": {
      "value": "382524.65"
    }
  }
}
```

**Properties:**
| Property | Type | Description | Required |
| --- | --- | --- | --- |
| `cashRaised` | [Money](money.md) | The cash raised for the note block. | `REQUIRED` |
| `interest` | [Money](money.md) | The total outstanding interest for the note block. | `REQUIRED` |
| `noteBlockId` | `STRING` | The identifier of the note block. <br/>**Constraints:** Min length: 1, Max length: 50 | `REQUIRED` |
| `principal` | [Money](money.md) | The total outstanding principal for the note block. The outstanding debt for the note block is the `principal` plus the `interest`. | `REQUIRED` |