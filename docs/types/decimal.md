### Decimal

**Description:** _A string-based representation of the decimal type._

**Example:**
```json
{
  "value": "100.57"
}
```

**Properties:**
| Property | Type | Description | Required |
| --- | --- | --- | --- |
| `value` | `STRING` | A decimal amount represented in string form.  Examples: 0 0.0 1.00 123.45 -456.0 .321 +1.23456e-3 1e-05 <br/>**Constraints:** Pattern: `^[\+\-]?((0|[1-9][0-9]*)(\.[0-9]*)?|\.[0-9]+)([eE][\+\-]?[0-9]+)?$`, Min length: 1, Max length: 100 | - |