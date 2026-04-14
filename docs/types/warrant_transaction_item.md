### Warrant Transaction Item

**Description:** _A warrant with its full transaction history. Groups all lifecycle events (issuance, exercises, transfers, cancellation) for a single warrant._

**Referenced By (1):**
- [List Transactions Response](list_transactions_response.md)

**References (4):**
- [Warrant Cancellation Transaction](warrant_cancellation_transaction.md)
- [Warrant Exercise Transaction](warrant_exercise_transaction.md)
- [Warrant Issuance Transaction](warrant_issuance_transaction.md)
- [Warrant Transfer Transaction](warrant_transfer_transaction.md)

**Example:**
```json
{
  "securityId": "5001",
  "stakeholderId": "4923",
  "securityLabel": "W-3",
  "issuance": {
    "issueDatetime": {
      "value": "2024-01-15T00:00:00Z"
    },
    "quantity": {
      "value": "50000"
    },
    "exercisePrice": {
      "currencyCode": {
        "value": "USD"
      },
      "amount": {
        "value": "2.00"
      }
    },
    "shareClassId": "10"
  },
  "exercises": [],
  "transfers": [],
  "cancellations": []
}
```

**Properties:**

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| `cancellations` | [`Array` of [Warrant Cancellation Transaction](warrant_cancellation_transaction.md)] | All cancellation transactions for the warrant, in chronological order. | - |
| `exercises` | [`Array` of [Warrant Exercise Transaction](warrant_exercise_transaction.md)] | All exercise transactions for the warrant. | - |
| `issuance` | [Warrant Issuance Transaction](warrant_issuance_transaction.md) | The issuance transaction for the warrant. | - |
| `securityId` | `STRING` | The identifier of the warrant. <br/>**Constraints:** Max length: 50 | - |
| `securityLabel` | `STRING` | The human-readable label for the warrant (e.g. "W-3"). <br/>**Constraints:** Max length: 50 | - |
| `stakeholderId` | `STRING` | The identifier of the current holder of the warrant. <br/>**Constraints:** Max length: 50 | - |
| `transfers` | [`Array` of [Warrant Transfer Transaction](warrant_transfer_transaction.md)] | All transfer transactions for the warrant, in chronological order. | - |