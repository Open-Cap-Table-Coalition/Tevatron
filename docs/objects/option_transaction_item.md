### Option Transaction Item

**Endpoints:** `GET /v1alpha1/issuers/{issuerId}/transactions`

**Description:** _An option grant with its full transaction history. Groups all lifecycle events (issuance, exercises, cancellation) for a single option grant._

**Referenced By (1):**
- [List Transactions Response](../types/list_transactions_response.md)

**References (3):**
- [Option Cancellation Transaction](../types/option_cancellation_transaction.md)
- [Option Exercise Transaction](../types/option_exercise_transaction.md)
- [Option Issuance Transaction](../types/option_issuance_transaction.md)

**Example:**
```json
{
  "securityId": "2513",
  "stakeholderId": "4923",
  "securityLabel": "ES-12",
  "issuance": {
    "issueDatetime": {
      "value": "2024-01-15T00:00:00Z"
    },
    "quantity": {
      "value": "10000"
    },
    "stockOptionType": "STOCK_OPTION_TYPE_ISO",
    "exercisePrice": {
      "currencyCode": {
        "value": "USD"
      },
      "amount": {
        "value": "1.50"
      }
    },
    "equityPlanId": "42",
    "expirationDatetime": {
      "value": "2034-01-15T00:00:00Z"
    }
  },
  "exercises": [
    {
      "id": "23HcT4iVfrgYUaJF9txHTaH",
      "sharesAcquiredDatetime": {
        "value": "2025-01-15T00:00:00Z"
      },
      "quantity": {
        "value": "200"
      },
      "exerciseMethod": "OPTION_EXERCISE_METHOD_CASH",
      "recordType": "STOCK_OPTION_TYPE_ISO",
      "resultingSecurityId": "2951",
      "resultingSecurityType": "certificate",
      "resultingSecurityLabel": "CS-42"
    }
  ]
}
```

**Properties:**

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| `cancellations` | [`Array` of [Option Cancellation Transaction](../types/option_cancellation_transaction.md)] | All cancellation and termination transactions for the option grant, in chronological order. An option can accrue multiple cancellation events (e.g. TERMINATED followed by PTEP_ENDED). | - |
| `exercises` | [`Array` of [Option Exercise Transaction](../types/option_exercise_transaction.md)] | All exercise transactions for the option grant. | - |
| `issuance` | [Option Issuance Transaction](../types/option_issuance_transaction.md) | The issuance transaction for the option grant. | - |
| `securityId` | `STRING` | The identifier of the option grant. <br/>**Constraints:** Max length: 50 | - |
| `securityLabel` | `STRING` | The human-readable label for the option grant (e.g. "ES-12"). <br/>**Constraints:** Max length: 50 | - |
| `stakeholderId` | `STRING` | The identifier of the current holder of the option grant. <br/>**Constraints:** Max length: 50 | - |