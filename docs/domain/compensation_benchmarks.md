# Compensation Benchmarks

Compensation Benchmarks is a small subsystem bolted onto the corporations surface. Two endpoints serve four related types that together describe benchmark datasets, the jobs inside them, the metadata describing them, and the caller's access level.

## OCF Equivalent

**No OCF equivalent.** Compensation benchmarking is out of scope for OCF — the
format covers ownership and equity events, not market-rate compensation data.

_No direct Open Cap Format equivalent — see the summary above for why._

## Endpoints

- `GET /v1alpha1/corporations/{corporationId}/compensationBenchmarks` — benchmark data + access + metadata
- `GET /v1alpha1/corporations/{corporationId}/compensationBenchmarkAttributes` — benchmark jobs + metadata

## Members

- [`v1alpha1Benchmarks`](../objects/benchmarks.md) — The benchmark dataset itself.
- [`v1alpha1BenchmarkJob`](../objects/benchmark_job.md) — A job role within the benchmark dataset.
- [`v1alpha1BenchmarksMetadata`](../types/benchmarks_metadata.md) — Metadata describing the benchmark dataset.
- [`v1alpha1Access`](../types/access.md) — Access/entitlement information for benchmarks.

[← Back to Domain Index](index.md)
