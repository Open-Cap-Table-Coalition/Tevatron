### Benchmarks Metadata

**Description:** _Context on the benchmark version of the benchmarks being returned. May differ by corporation._

**Referenced By (2):**
- [Get Compensation Benchmark Attributes Response](get_compensation_benchmark_attributes_response.md)
- [Get Compensation Benchmarks Response](get_compensation_benchmarks_response.md)

**References (1):**
- [Iso8601 Complete Calendar Date Time](iso8601_complete_calendar_date_time.md)

**Example:**
```json
{
  "benchmarksVersionDatetime": {
    "value": "2024-01-01T09:00:00.000000Z"
  }
}
```

**Properties:**

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| `benchmarksVersionDatetime` | [Iso8601 Complete Calendar Date Time](iso8601_complete_calendar_date_time.md) | The datetime that these benchmarks were first released in Carta. | `REQUIRED` |