### Benchmark Job

**Endpoints:** `GET /v1alpha1/corporations/{corporationId}/compensationBenchmarkAttributes`

**Description:** _A job area, job specialization, and the job levels that have benchmarks._

**Referenced By (1):**
- [Get Compensation Benchmark Attributes Response](../types/get_compensation_benchmark_attributes_response.md)

**Example:**
```json
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
```

**Properties:**

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| `jobArea` | `STRING` | The job area that the underlying data is segmented by. <br/>**Constraints:** Min length: 1, Max length: 50 | `REQUIRED` |
| `jobLevels` | [`Array` of `STRING`] | The job levels that the underlying data is segmented by. | `REQUIRED` |
| `jobSpecialization` | `STRING` | The job specialization that the underlying data is segmented by. <br/>**Constraints:** Max length: 100 | - |