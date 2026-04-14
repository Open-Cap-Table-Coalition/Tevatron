### Rsa Transaction Item

**Description:** _An RSA with its full transaction history. Groups all lifecycle events (issuance, cancellation) for a single RSA._

**Referenced By (1):**
- [List Transactions Response](list_transactions_response.md)

**References (2):**
- [Rsa Cancellation Transaction](rsa_cancellation_transaction.md)
- [Rsa Issuance Transaction](rsa_issuance_transaction.md)

**Example:**
```json
{
  "securityId": "4101",
  "stakeholderId": "4923",
  "securityLabel": "RSA-3",
  "issuance": {
    "issueDatetime": {
      "value": "2024-01-15T00:00:00Z"
    },
    "quantity": {
      "value": "5000"
    },
    "acquisitionCost": {
      "currencyCode": {
        "value": "USD"
      },
      "amount": {
        "value": "0.001"
      }
    },
    "equityPlanId": "42"
  }
}
```

**Properties:**

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| `cancellations` | [`Array` of [Rsa Cancellation Transaction](rsa_cancellation_transaction.md)] | All cancellation and termination transactions for the RSA, in chronological order. | - |
| `issuance` | [Rsa Issuance Transaction](rsa_issuance_transaction.md) | The issuance transaction for the RSA. | - |
| `securityId` | `STRING` | The identifier of the RSA. <br/>**Constraints:** Max length: 50 | - |
| `securityLabel` | `STRING` | The human-readable label for the RSA (e.g. "RSA-3"). <br/>**Constraints:** Max length: 50 | - |
| `stakeholderId` | `STRING` | The identifier of the current holder of the RSA. <br/>**Constraints:** Max length: 50 | - |