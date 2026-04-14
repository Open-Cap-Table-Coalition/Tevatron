### Piu Transaction Item

**Description:** _A PIU (Profits Interest Unit) with its full transaction history. Groups all lifecycle events (issuance, cancellation) for a single PIU._

**Referenced By (1):**
- [List Transactions Response](list_transactions_response.md)

**References (2):**
- [Piu Cancellation Transaction](piu_cancellation_transaction.md)
- [Piu Issuance Transaction](piu_issuance_transaction.md)

**Example:**
```json
{
  "securityId": "6001",
  "stakeholderId": "4923",
  "securityLabel": "PIU-3",
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
        "value": "0.001"
      }
    },
    "equityPlanId": "42",
    "issuanceReason": "PIU_ISSUANCE_REASON_ISSUED_FROM_SHARE_RESERVE"
  },
  "cancellations": []
}
```

**Properties:**

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| `cancellations` | [`Array` of [Piu Cancellation Transaction](piu_cancellation_transaction.md)] | All cancellation and termination transactions for the PIU, in chronological order. | - |
| `issuance` | [Piu Issuance Transaction](piu_issuance_transaction.md) | The issuance transaction for the PIU. | - |
| `securityId` | `STRING` | The identifier of the PIU. <br/>**Constraints:** Max length: 50 | - |
| `securityLabel` | `STRING` | The human-readable label for the PIU (e.g. "PIU-3"). <br/>**Constraints:** Max length: 50 | - |
| `stakeholderId` | `STRING` | The identifier of the current holder of the PIU. <br/>**Constraints:** Max length: 50 | - |