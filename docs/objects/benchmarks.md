### Benchmarks

**Endpoints:** `GET /v1alpha1/corporations/{corporationId}/compensationBenchmarks`

**Description:** _The compensation benchmarks._

**Example:**
```json
{
  "postMoneyValuationBucket": "100M to 250M",
  "industry": "All",
  "geoadjustmentLocation": "New York-Newark-Jersey City, NY-NJ-PA",
  "jobArea": "Engineering",
  "jobSpecialization": "Web Engineer",
  "jobLevel": "IC 3",
  "benchmarkValues": [
    {
      "compensationType": "SALARY",
      "percentile": "P25",
      "value": {
        "value": "100000"
      }
    },
    {
      "compensationType": "SALARY",
      "percentile": "P50",
      "value": {
        "value": "110000"
      }
    },
    {
      "compensationType": "SALARY",
      "percentile": "P75",
      "value": {
        "value": "120000"
      }
    },
    {
      "compensationType": "SALARY",
      "percentile": "P90",
      "value": {
        "value": "130000"
      }
    }
  ]
}
```

**Properties:**
| Property | Type | Description | Required |
| --- | --- | --- | --- |
| `benchmarkValues` | [`Array` of [Benchmark Value](../types/benchmark_value.md)] | The benchmark values for this segment of data. | - |
| `geoAdjustmentLocation` | `STRING` | The location used to geo-adjust the benchmarks.  Note that a company may have location-based pay settings in their Carta Total Compensation compensation plan which may override the requested value. <br/>**Constraints:** Min length: 1, Max length: 100 | `REQUIRED` |
| `industry` | `STRING` | The industry that the underlying data is segmented by. <br/>**Constraints:** Min length: 1, Max length: 100 | `REQUIRED` |
| `jobArea` | `STRING` | The job area that the underlying data is segmented by. <br/>**Constraints:** Min length: 1, Max length: 50 | `REQUIRED` |
| `jobLevel` | `STRING` | The job level that the underlying data is segmented by. <br/>**Constraints:** Min length: 1, Max length: 10 | `REQUIRED` |
| `jobSpecialization` | `STRING` | The job specialization that the underlying data is segmented by.  An empty job specialization denotes the benchmark for the roll-up job area. <br/>**Constraints:** Max length: 100 | `REQUIRED` |
| `postMoneyValuationBucket` | `STRING` | The company valuation bucket that the underlying data is segmented by. <br/>**Constraints:** Min length: 1, Max length: 50 | `REQUIRED` |