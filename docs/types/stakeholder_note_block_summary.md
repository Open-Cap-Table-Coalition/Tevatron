### Stakeholder Note Block Summary

**Description:** _Note block summary information scoped to a specific stakeholder._

**Referenced By (2):**
- [Issuerscapitalization Stakeholder](issuerscapitalization_stakeholder.md)
- [Stakeholder Group](stakeholder_group.md)

**References (1):**
- [Money](money.md)

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
  },
  "outstandingDebt": {
    "currencyCode": {
      "value": "USD"
    },
    "amount": {
      "value": "1457524.65"
    }
  }
}
```

**Properties:**

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| `cashRaised` | [Money](money.md) | The cash raised for the note block. | `REQUIRED` |
| `interest` | [Money](money.md) | Total interest for the note block. The outstanding debt for the note block is the `principal` plus the `interest`. | `REQUIRED` |
| `name` | `STRING` | The name of the note block. <br/>**Constraints:** Max length: 1000 | `REQUIRED` |
| `noteBlockId` | `STRING` | The identifier of the note block. <br/>**Constraints:** Min length: 1, Max length: 50 | `REQUIRED` |
| `outstandingDebt` | [Money](money.md) | Total outstanding debt for the note block. The outstanding debt for the note block is the `principal` plus the `interest`. | - |
| `principal` | [Money](money.md) | The total outstanding principal for the note block. The outstanding debt for the note block is the `principal` plus the `interest`. | `REQUIRED` |