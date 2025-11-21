### Option Exercise

**Endpoints:** `GET /v1alpha1/issuers/{issuerId}/optionExercises`

**Description:** _An option exercise is an event representing a stakeholder exercising their right to purchase shares of an issuer at a set price, the strike price, defined in the option grant being exercised. The result of a successfully completed exercise is the issuance of a certificate._

**Example:**
```json
{
  "id": "JZgiQfmZpvuiLbhXXQXfZi",
  "issuerId": "7",
  "stakeholderId": "6113",
  "optionGrantId": "9387",
  "certificateId": "4732",
  "quantity": {
    "value": "100"
  },
  "exerciseTime": {
    "value": "2024-01-01T09:00:00.000000Z"
  },
  "state": "COMPLETE",
  "exerciseType": "CASH_EXERCISE",
  "recordType": "ISO",
  "taxWithholding": [
    {
      "name": "Federal",
      "rate": {
        "value": "20"
      },
      "taxes": {
        "currencyCode": "USD",
        "amount": {
          "value": "200"
        }
      },
      "jurisdiction": {
        "city": "NewYork",
        "countrySubdivision": "US-NY",
        "country": "USA"
      }
    }
  ],
  "moneyMovement": {
    "completionDate": {
      "value": "2024-02-10T09:00:00.000000Z"
    }
  }
}
```

**Properties:**
| Property | Type | Description | Required |
| --- | --- | --- | --- |
| `certificateId` | `STRING` | The identifier of the certificate issued as a result of the option exercise event completing. <br/>**Constraints:** Max length: 50 | - |
| `exerciseTime` | [Iso8601 Complete Calendar Date Time](../types/iso8601_complete_calendar_date_time.md) | The date and time in which the option exercise request was initiated. | - |
| `exerciseType` | [Option Exercise Type](../types/option_exercise_type.md) | The type of option exercise being requested. | - |
| `id` | `STRING` | The identifier of the option exercise.  Note: It is possible for this ID to not exist for legacy reasons, in which case the value of this field will be `"NO_ID"` <br/>**Constraints:** Max length: 50 | - |
| `issuerId` | `STRING` | The identifier of the issuer that issued the option grant. <br/>**Constraints:** Max length: 50 | - |
| `moneyMovement` | [Option Exercise Money Movement](../types/option_exercise_money_movement.md) | The money movement information associated with the option exercise. | - |
| `optionGrantId` | `STRING` | The identifier of the option grant being exercised. <br/>**Constraints:** Max length: 50 | - |
| `quantity` | [Decimal](../types/decimal.md) | The number of shares being exercised from the related option grant. | - |
| `recordType` | [Securitiesoptionexercises Stock Option Type](../types/securitiesoptionexercises_stock_option_type.md) | The type of the record associated with the option exercise. | - |
| `stakeholderId` | `STRING` | The identifier of the stakeholder that holds the option grant being exercised. <br/>**Constraints:** Max length: 50 | - |
| `state` | [Option Exercise State](../types/option_exercise_state.md) | The current state of the exercise request. | - |
| `taxWithholding` | [`Array` of [Option Exercise Tax Withholding Line Item](../types/option_exercise_tax_withholding_line_item.md)] | The tax withholding information associated with the option exercise. | - |