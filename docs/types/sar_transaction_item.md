### Sar Transaction Item

**Description:** _A SAR (Stock Appreciation Right) with its full transaction history. Groups all lifecycle events (issuance, exercises, cancellation) for a single SAR._

**Referenced By (1):**
- [List Transactions Response](list_transactions_response.md)

**References (3):**
- [Sar Cancellation Transaction](sar_cancellation_transaction.md)
- [Sar Exercise Transaction](sar_exercise_transaction.md)
- [Sar Issuance Transaction](sar_issuance_transaction.md)

**Example:**
```json
{
  "securityId": "7001",
  "stakeholderId": "4923",
  "securityLabel": "SAR-3",
  "issuance": {
    "issueDatetime": {
      "value": "2024-01-15T00:00:00Z"
    },
    "quantity": {
      "value": "10000"
    },
    "exercisePrice": {
      "currencyCode": {
        "value": "USD"
      },
      "amount": {
        "value": "2.00"
      }
    },
    "equityPlanId": "42",
    "shareClassId": "10"
  },
  "exercises": [],
  "cancellations": []
}
```

**Properties:**

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| `cancellations` | [`Array` of [Sar Cancellation Transaction](sar_cancellation_transaction.md)] | All cancellation and termination transactions for the SAR, in chronological order. | - |
| `exercises` | [`Array` of [Sar Exercise Transaction](sar_exercise_transaction.md)] | All exercise transactions for the SAR. Each exercise may be stock-settled (with resulting security) or cash-settled (with cash acquired). | - |
| `issuance` | [Sar Issuance Transaction](sar_issuance_transaction.md) | The issuance transaction for the SAR. | - |
| `securityId` | `STRING` | The identifier of the SAR. <br/>**Constraints:** Max length: 50 | - |
| `securityLabel` | `STRING` | The human-readable label for the SAR (e.g. "SAR-3"). <br/>**Constraints:** Max length: 50 | - |
| `stakeholderId` | `STRING` | The identifier of the current holder of the SAR. <br/>**Constraints:** Max length: 50 | - |