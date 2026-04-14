### Rsu Transaction Item

**Description:** _An RSU award with its full transaction history. Groups all lifecycle events (issuance, settlements, cancellation) for a single RSU award._

**Referenced By (1):**
- [List Transactions Response](list_transactions_response.md)

**References (3):**
- [Rsu Cancellation Transaction](rsu_cancellation_transaction.md)
- [Rsu Issuance Transaction](rsu_issuance_transaction.md)
- [Rsu Settlement Transaction](rsu_settlement_transaction.md)

**Example:**
```json
{
  "securityId": "3201",
  "stakeholderId": "4923",
  "securityLabel": "RSU-7",
  "issuance": {
    "issueDatetime": {
      "value": "2024-01-15T00:00:00Z"
    },
    "quantity": {
      "value": "5000"
    },
    "equityPlanId": "42"
  },
  "settlements": [
    {
      "id": "34JdU5jWgsrhZbKG0uyIUbI",
      "settlementDatetime": {
        "value": "2025-01-15T00:00:00Z"
      },
      "settledQuantity": {
        "value": "700"
      },
      "withheldQuantity": {
        "value": "300"
      },
      "resultingSecurityId": "3051",
      "resultingSecurityType": "certificate",
      "resultingSecurityLabel": "CS-55"
    }
  ]
}
```

**Properties:**

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| `cancellations` | [`Array` of [Rsu Cancellation Transaction](rsu_cancellation_transaction.md)] | All cancellation and termination transactions for the RSU award, in chronological order. An award can accrue multiple cancellation events (e.g. TERMINATED followed by SETTLEMENT_WINDOW_ENDED). | - |
| `issuance` | [Rsu Issuance Transaction](rsu_issuance_transaction.md) | The issuance transaction for the RSU award. | - |
| `securityId` | `STRING` | The identifier of the RSU award. <br/>**Constraints:** Max length: 50 | - |
| `securityLabel` | `STRING` | The human-readable label for the RSU award (e.g. "RSU-7"). <br/>**Constraints:** Max length: 50 | - |
| `settlements` | [`Array` of [Rsu Settlement Transaction](rsu_settlement_transaction.md)] | All settlement transactions for the RSU award. | - |
| `stakeholderId` | `STRING` | The identifier of the current holder of the RSU award. <br/>**Constraints:** Max length: 50 | - |