### Get Compensation Benchmarks Response

**Description:** _The response for the GetCompensationBenchmarks endpoint._

**Example:**
```json
{
  "access": {
    "accessLevel": "FULL_ACCESS",
    "accessReason": ""
  },
  "benchmarksMetadata": {
    "benchmarksVersionDatetime": {
      "value": "2024-01-01T09:00:00.000000Z"
    }
  },
  "benchmarks": [
    {
      "postMoneyValuationBucket": "100M to 250M",
      "industry": "All",
      "geoAdjustmentLocation": "New York-Newark-Jersey City, NY-NJ-PA",
      "jobArea": "Engineering",
      "jobSpecialization": "Web Engineer",
      "jobLevel": "IC 3",
      "benchmarkValues": [
        {
          "compensationType": "SALARY",
          "percentile": "P25",
          "benchmark": {
            "value": "100000"
          }
        },
        {
          "compensationType": "SALARY",
          "percentile": "P50",
          "benchmark": {
            "value": "110000"
          }
        },
        {
          "compensationType": "SALARY",
          "percentile": "P75",
          "benchmark": {
            "value": "120000"
          }
        },
        {
          "compensationType": "SALARY",
          "percentile": "P90",
          "benchmark": {
            "value": "130000"
          }
        }
      ]
    }
  ]
}
```

**Properties:**
| Property | Type | Description | Required |
| --- | --- | --- | --- |
| `access` | [Access](access.md) | Context about the access of a given corporation. | `REQUIRED` |
| `benchmarks` | [`Array` of [Benchmarks](../objects/benchmarks.md)] | The compensation benchmarks. | - |
| `benchmarksMetadata` | [Benchmarks Metadata](benchmarks_metadata.md) | Context on the benchmark version of the benchmarks being returned. May differ by corporation. | `REQUIRED` |
| `nextPageToken` | `STRING` | Submit the `nextPageToken` string as `pageToken` in a subsequent request to retrieve the next page.  If the Get Compensation Benchmarks response omits `nextPageToken`, then there are no subsequent pages. | - |