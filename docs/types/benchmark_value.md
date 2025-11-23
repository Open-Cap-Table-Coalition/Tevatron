### Benchmark Value

**Description:** _A compensation benchmark value._

**Referenced By (1):**
- [Benchmarks](../objects/benchmarks.md)

**References (1):**
- [Decimal](decimal.md)

**Example:**
```json
{
  "compensationType": "SALARY",
  "percentile": "P25",
  "benchmark": {
    "value": "100000"
  }
}
```

**Properties:**

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| `benchmark` | [Decimal](decimal.md) | The ordinal value of the benchmark.  "SALARY" and "TOTAL_CASH" are annual values in US dollars (USD).  "EQUITY_AS_FULLY_DILUTED_PERCENT" is represented as a annual grant value between 0 and 100: 1 represents 1%.  For CEO Founder benchmarks, this value represents total ownership instead of an annual grant value. | - |
| `compensationType` | `STRING` | The compensation type of the benchmark. <br/>**Constraints:** Min length: 1, Max length: 50 | `REQUIRED` |
| `percentile` | `STRING` | The percentile of the benchmark.  For example: "P25" represents the 25th percentile. <br/>**Constraints:** Min length: 1, Max length: 10 | `REQUIRED` |