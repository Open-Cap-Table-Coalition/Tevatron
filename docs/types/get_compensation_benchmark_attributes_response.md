### Get Compensation Benchmark Attributes Response

**Description:** _The response for the `GetCompensationBenchmarkAttributes` endpoint._

**Example:**
```json
{
  "benchmarksMetadata": {
    "benchmarksVersionDatetime": {
      "value": "2024-01-01T09:00:00.000000Z"
    }
  },
  "compensationTypes": [
    "SALARY",
    "EQUITY_AS_FULLY_DILUTED_PERCENT"
  ],
  "industries": [
    "All"
  ],
  "percentiles": [
    "P25",
    "P50",
    "P75"
  ],
  "postMoneyValuationBuckets": [
    "10M to 25M",
    "50M to 100M"
  ],
  "geoAdjustmentLocations": [
    "Dallas-Fort Worth-Arlington, TX",
    "New York-Newark-Jersey City, NY-NJ-PA",
    "San Francisco-Oakland-Hayward, CA"
  ],
  "jobs": [
    {
      "jobArea": "Engineering",
      "jobSpecialization": "Web Engineer",
      "jobLevels": [
        "IC 2",
        "IC 3",
        "MGR 4",
        "MGR 5",
        "EX 10",
        "EX 11"
      ]
    }
  ]
}
```

**Properties:**
| Property | Type | Description | Required |
| --- | --- | --- | --- |
| `benchmarksMetadata` | [Benchmarks Metadata](benchmarks_metadata.md) | Context on the benchmark version of the benchmarks being returned. May differ by corporation. | `REQUIRED` |
| `compensationTypes` | [`Array` of `STRING`] | The compensation types that the benchmarks can be segmented by. | `REQUIRED` |
| `geoAdjustmentLocations` | [`Array` of `STRING`] | The locations the benchmarks can be geo-adjusted by. | `REQUIRED` |
| `industries` | [`Array` of `STRING`] | The industries supported by the benchmarks. | `REQUIRED` |
| `jobs` | [`Array` of [Benchmark Job](../objects/benchmark_job.md)] | The jobs that the benchmarks can be segmented by. | `REQUIRED` |
| `percentiles` | [`Array` of `STRING`] | The percentiles supported by the benchmarks. | `REQUIRED` |
| `postMoneyValuationBuckets` | [`Array` of `STRING`] | The peer groups that the benchmarks are segmented by. | `REQUIRED` |