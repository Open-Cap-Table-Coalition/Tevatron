### Threshold Details

**Description:** _Threshold Details for the interest._

**Referenced By (1):**
- [Interest](../objects/interest.md)

**References (2):**
- [Threshold Details Threshold Type](threshold_details_threshold_type.md)
- [Decimal](decimal.md)

**Example:**
```json
{
  "thresholdAmount": {
    "value": "7.2"
  },
  "thresholdType": "THRESHOLD_TYPE_PER_UNIT"
}
```

**Properties:**

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| `amount` | [Decimal](decimal.md) | The value above which the holder is entitled to gains of the company’s value. | - |
| `type` | [Threshold Details Threshold Type](threshold_details_threshold_type.md) | The threshold type. | - |