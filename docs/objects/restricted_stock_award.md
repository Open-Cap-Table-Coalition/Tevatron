### Restricted Stock Award

**Endpoints:** `GET /v1alpha1/issuers/{issuerId}/restrictedStockAwards`

**Description:** _A restricted stock award is a grant of company shares._

**Referenced By (2):**
- [Get Restricted Stock Award Response](../types/get_restricted_stock_award_response.md)
- [List Restricted Stock Awards Response](../types/list_restricted_stock_awards_response.md)

**References (6):**
- [Issuerssecurities Vesting Schedule](../types/issuerssecurities_vesting_schedule.md)
- [Decimal](../types/decimal.md)
- [Iso8601 Complete Calendar Date](../types/iso8601_complete_calendar_date.md)
- [Iso8601 Complete Calendar Date Time](../types/iso8601_complete_calendar_date_time.md)
- [Money](../types/money.md)
- [Restricted Stock Award Vesting Event](../types/restricted_stock_award_vesting_event.md)

**Example:**
```json
{
  "id": "1191",
  "issuerId": "7",
  "stakeholderId": "6113",
  "equityIncentivePlanName": "2016 Equity Incentive Plan",
  "shareClassName": "Common",
  "issueDate": {
    "value": "2016-08-25"
  },
  "vestingStartDate": {
    "value": "2016-08-25"
  },
  "boardApprovalDate": {
    "value": "2016-12-01"
  },
  "stakeholderAcceptanceDate": {
    "value": "2017-02-27"
  },
  "canceledDate": {
    "value": "2022-05-02"
  },
  "quantity": {
    "value": "200000"
  },
  "vestedQuantity": {
    "value": "200000"
  },
  "securityLabel": "CS-16",
  "pricePerShare": {
    "currencyCode": {
      "value": "USD"
    },
    "amount": {
      "value": "0.01"
    }
  },
  "vestingEvents": [
    {
      "id": "1988",
      "vestDate": {
        "value": "2018-02-27"
      },
      "quantity": {
        "value": "200000"
      },
      "performanceCondition": false,
      "vested": true,
      "maxQuantity": {
        "value": "200000"
      },
      "targetQuantity": {
        "value": "200000"
      },
      "vestedQuantity": {
        "value": "200000"
      }
    }
  ],
  "vestingSchedule": {
    "name": "1/24 Cliff",
    "lastModifiedDate": {
      "value": "2022-01-31"
    },
    "startDate": {
      "value": "2022-01-31"
    },
    "endDate": {
      "value": "2024-01-31"
    }
  },
  "lastModifiedDatetime": {
    "value": "2024-07-30T09:31:57.000000Z"
  }
}
```

**Properties:**

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| `boardApprovalDate` | [Iso8601 Complete Calendar Date](../types/iso8601_complete_calendar_date.md) | The date the restricted stock award received board approval. | - |
| `canceledDate` | [Iso8601 Complete Calendar Date](../types/iso8601_complete_calendar_date.md) | The date the restricted stock award was canceled. | - |
| `canceledQuantity` | [Decimal](../types/decimal.md) | The number of shares in the restricted stock award that were canceled. | - |
| `equityIncentivePlanName` | `STRING` | The name of the equity incentive plan (i.e., option plan) associated with this restricted stock award. <br/>**Constraints:** Max length: 100 | - |
| `id` | `STRING` | The identifier of the restricted stock award. <br/>**Constraints:** Max length: 50 | - |
| `issueDate` | [Iso8601 Complete Calendar Date](../types/iso8601_complete_calendar_date.md) | The date the restricted stock award was issued. | - |
| `issuerId` | `STRING` | The identifier of the issuer owning the restricted stock award. <br/>**Constraints:** Min length: 1, Max length: 50 | - |
| `lastModifiedDatetime` | [Iso8601 Complete Calendar Date Time](../types/iso8601_complete_calendar_date_time.md) | The date and time when the restricted stock award was last modified. | - |
| `pricePerShare` | [Money](../types/money.md) | The cost of each share in the restricted stock award. | - |
| `quantity` | [Decimal](../types/decimal.md) | The number of restricted stock units in the award. | - |
| `returnedToPoolQuantity` | [Decimal](../types/decimal.md) | The number of shares in the restricted stock award that were returned to the pool. | - |
| `returnedToTreasuryQuantity` | [Decimal](../types/decimal.md) | The number of shares in the restricted stock award that were annulled, but not returned to the pool. | - |
| `securityLabel` | `STRING` | The label representing this security (restricted stock award). <br/>**Constraints:** Max length: 50 | - |
| `shareClassName` | `STRING` | The name of the share class that this restricted stock award belongs to. <br/>**Constraints:** Max length: 50 | - |
| `stakeholderAcceptanceDate` | [Iso8601 Complete Calendar Date](../types/iso8601_complete_calendar_date.md) | The date the restricted stock award was accepted by the stakeholder. | - |
| `stakeholderId` | `STRING` | The identifier of the stakeholder that holds the restricted stock award. <br/>**Constraints:** Max length: 50 | - |
| `terminationDate` | [Iso8601 Complete Calendar Date](../types/iso8601_complete_calendar_date.md) | The date the restricted stock award was terminated. This commonly matches the date the company's relationship with the stakeholder was terminated. | - |
| `vestedQuantity` | [Decimal](../types/decimal.md) | The number of vested shares in the stock award. | - |
| `vestingEvents` | [`Array` of [Restricted Stock Award Vesting Event](../types/restricted_stock_award_vesting_event.md)] | The list of all vesting events associated with the restricted stock award. | - |
| `vestingSchedule` | [Issuerssecurities Vesting Schedule](../types/issuerssecurities_vesting_schedule.md) | The vesting schedule information associated with the restricted stock award. | - |
| `vestingStartDate` | [Iso8601 Complete Calendar Date](../types/iso8601_complete_calendar_date.md) | The start date of the vesting period for the restricted stock award. | - |