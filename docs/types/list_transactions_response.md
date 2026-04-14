### List Transactions Response

**Description:** _The response from the List Transactions endpoint.

Exactly one transaction array is populated per request, determined by the `type` query parameter. For example, `type=option` populates `optionTransactions` only; the other arrays will be empty._

**References (8):**
- [Certificate Transaction Item](certificate_transaction_item.md)
- [Convertible Transaction Item](convertible_transaction_item.md)
- [Option Transaction Item](../objects/option_transaction_item.md)
- [Piu Transaction Item](piu_transaction_item.md)
- [Rsa Transaction Item](rsa_transaction_item.md)
- [Rsu Transaction Item](rsu_transaction_item.md)
- [Sar Transaction Item](sar_transaction_item.md)
- [Warrant Transaction Item](warrant_transaction_item.md)

**Example:**
```json
{
  "optionTransactions": [
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
  ],
  "rsuTransactions": [],
  "rsaTransactions": [],
  "certificateTransactions": [],
  "warrantTransactions": [],
  "convertibleTransactions": [],
  "piuTransactions": [],
  "sarTransactions": [],
  "nextPageToken": "NTA6NTA6YTFiMmMzZDQtZTVmNi00..."
}
```

**Properties:**

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| `certificateTransactions` | [`Array` of [Certificate Transaction Item](certificate_transaction_item.md)] | The certificates with their transaction history. Each item contains all transactions (issuance, cancellation) for a single certificate. Populated when `type=certificate`. | - |
| `convertibleTransactions` | [`Array` of [Convertible Transaction Item](convertible_transaction_item.md)] | The convertible notes with their transaction history. Each item contains the issuance and cancellations (if applicable) for a single convertible note. A conversion appears as a cancellation with `reason=CONVERTIBLE_CANCELLATION_REASON_CONVERTED`. A transferred note includes a `precededBySecurityId` on its issuance. Populated when `type=convertible`. | - |
| `nextPageToken` | `STRING` | Submit the `nextPageToken` string as `pageToken` in a subsequent request to retrieve the next page.  If the response omits `nextPageToken`, then there are no subsequent pages. | - |
| `optionTransactions` | [`Array` of [Option Transaction Item](../objects/option_transaction_item.md)] | The option grants with their transaction history. Each item contains all transactions (issuance, exercises, cancellation) for a single option grant. Populated when `type=option`. | - |
| `piuTransactions` | [`Array` of [Piu Transaction Item](piu_transaction_item.md)] | The PIUs (Profits Interest Units) with their transaction history. Each item contains all transactions (issuance, cancellation) for a single PIU. Populated when `type=piu`. | - |
| `rsaTransactions` | [`Array` of [Rsa Transaction Item](rsa_transaction_item.md)] | The RSA grants with their transaction history. Each item contains all transactions (issuance, cancellation) for a single RSA. Populated when `type=rsa`. | - |
| `rsuTransactions` | [`Array` of [Rsu Transaction Item](rsu_transaction_item.md)] | The RSU awards with their transaction history. Each item contains all transactions (issuance, settlements, cancellation) for a single RSU award. Populated when `type=rsu`. | - |
| `sarTransactions` | [`Array` of [Sar Transaction Item](sar_transaction_item.md)] | The SARs (Stock Appreciation Rights) with their transaction history. Each item contains all transactions (issuance, exercises, cancellation) for a single SAR. Exercises may be stock-settled or cash-settled. Populated when `type=sar`. | - |
| `warrantTransactions` | [`Array` of [Warrant Transaction Item](warrant_transaction_item.md)] | The warrants with their transaction history. Each item contains all transactions (issuance, exercises, transfers, cancellation) for a single warrant. Populated when `type=warrant`. | - |