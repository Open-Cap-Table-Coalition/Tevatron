### Certificate Transaction Item

**Description:** _A certificate with its full transaction history. Groups all lifecycle events (issuance, cancellation) for a single certificate._

**Referenced By (1):**
- [List Transactions Response](list_transactions_response.md)

**References (2):**
- [Certificate Cancellation Transaction](certificate_cancellation_transaction.md)
- [Certificate Issuance Transaction](certificate_issuance_transaction.md)

**Example:**
```json
{
  "securityId": "2951",
  "stakeholderId": "4923",
  "securityLabel": "CS-42",
  "issuance": {
    "issueDatetime": {
      "value": "2024-01-15T00:00:00Z"
    },
    "quantity": {
      "value": "10000"
    },
    "acquisitionCost": {
      "currencyCode": {
        "value": "USD"
      },
      "amount": {
        "value": "1.50"
      }
    },
    "equityPlanId": "42"
  }
}
```

**Properties:**

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| `cancellations` | [`Array` of [Certificate Cancellation Transaction](certificate_cancellation_transaction.md)] | All cancellation and termination transactions for the certificate, in chronological order. | - |
| `issuance` | [Certificate Issuance Transaction](certificate_issuance_transaction.md) | The issuance transaction for the certificate. | - |
| `securityId` | `STRING` | The identifier of the certificate. <br/>**Constraints:** Max length: 50 | - |
| `securityLabel` | `STRING` | The human-readable label for the certificate (e.g. "CS-42"). <br/>**Constraints:** Max length: 50 | - |
| `stakeholderId` | `STRING` | The identifier of the current holder of the certificate. <br/>**Constraints:** Max length: 50 | - |