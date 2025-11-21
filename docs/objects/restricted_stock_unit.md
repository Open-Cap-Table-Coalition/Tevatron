### Restricted Stock Unit

**Endpoints:** `GET /v1alpha1/issuers/{issuerId}/restrictedStockUnits`

**Description:** _A restricted stock unit is a grant of company shares._

**Example:**
```json
{
  "id": "8550",
  "issuerId": "7",
  "stakeholderId": "6113",
  "equityIncentivePlanName": "2015 Equity Incentive Plan",
  "issueDate": {
    "value": "2015-06-01"
  },
  "vestingStartDate": {
    "value": "2015-06-01"
  },
  "boardApprovalDate": {
    "value": "2015-06-01"
  },
  "stakeholderAcceptanceDate": {
    "value": "2017-02-27"
  },
  "quantity": {
    "value": "1500"
  },
  "vestedQuantity": {
    "value": "1500"
  },
  "releasedQuantity": {
    "value": "200"
  },
  "releasePricePerShare": {
    "currencyCode": {
      "value": "USD"
    },
    "amount": {
      "value": "0.78"
    }
  },
  "netSettledQuantity": {
    "value": "145"
  },
  "securityLabel": "ES-136",
  "vestingEvents": [
    {
      "id": "1988",
      "vestDate": {
        "value": "2016-06-01"
      },
      "quantity": {
        "value": "375"
      },
      "performanceCondition": false,
      "vested": true,
      "maxQuantity": {
        "value": "375"
      },
      "targetQuantity": {
        "value": "375"
      },
      "vestedQuantity": {
        "value": "375"
      }
    }
  ],
  "settlements": [
    {
      "settlementDate": {
        "value": "2016-08-19"
      },
      "releaseQuantity": {
        "value": "200"
      },
      "saleQuantity": {
        "value": "200"
      },
      "withholdingQuantity": {
        "value": "55"
      },
      "netSettlementQuantity": {
        "value": "145"
      },
      "settlementPrice": {
        "currencyCode": {
          "value": "USD"
        },
        "amount": {
          "value": "0.78"
        }
      },
      "certificateId": "78",
      "certificateLabel": "CS-124"
    }
  ],
  "vestingSchedule": {
    "name": "1/24 Cliff",
    "lastModifiedDate": {
      "value": "2022-01-31"
    },
    "startDate": {
      "value": "2015-06-01"
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
| `boardApprovalDate` | [Iso8601 Complete Calendar Date](../types/iso8601_complete_calendar_date.md) | The date the restricted stock unit received board approval. | - |
| `canceledDate` | [Iso8601 Complete Calendar Date](../types/iso8601_complete_calendar_date.md) | The date the restricted stock unit was canceled. | - |
| `canceledQuantity` | [Decimal](../types/decimal.md) | The number of shares in the restricted stock unit that were canceled. | - |
| `equityIncentivePlanName` | `STRING` | The name of the equity incentive plan (i.e., option plan) associated with the restricted stock unit. <br/>**Constraints:** Max length: 100 | - |
| `expiredQuantity` | [Decimal](../types/decimal.md) | The number of shares in the restricted stock unit that expired. | - |
| `forfeitedQuantity` | [Decimal](../types/decimal.md) | The number of shares in the restricted stock unit that were forfeited. | - |
| `id` | `STRING` | The identifier of the restricted stock unit. <br/>**Constraints:** Min length: 1, Max length: 50 | - |
| `issueDate` | [Iso8601 Complete Calendar Date](../types/iso8601_complete_calendar_date.md) | The date the restricted stock unit was issued. | - |
| `issuerId` | `STRING` | The identifier of the issuer owning the restricted stock unit. <br/>**Constraints:** Min length: 1, Max length: 50 | - |
| `lastModifiedDatetime` | [Iso8601 Complete Calendar Date Time](../types/iso8601_complete_calendar_date_time.md) | The date and time when the restricted stock unit was last modified. | - |
| `netSettledQuantity` | [Decimal](../types/decimal.md) | The total quantity of restricted stock units in this grant that have been released to the stakeholder. | - |
| `quantity` | [Decimal](../types/decimal.md) | The total quantity of shares in the restricted stock unit grant. | - |
| `releasePricePerShare` | [Money](../types/money.md) | The price of each share that has been released from the restricted stock unit grant. | - |
| `releasedQuantity` | [Decimal](../types/decimal.md) | The total quantity of restricted stock units in the grant that has been settled. | - |
| `returnedToPoolQuantity` | [Decimal](../types/decimal.md) | The number of shares in the restricted stock unit that were returned to the pool. | - |
| `returnedToTreasuryQuantity` | [Decimal](../types/decimal.md) | The number of shares in the restricted stock unit that were annulled, but not returned to the pool. | - |
| `securityLabel` | `STRING` | The label representing this security (restricted stock unit). <br/>**Constraints:** Max length: 50 | - |
| `settlements` | [`Array` of [Restricted Stock Unit Settlement](../types/restricted_stock_unit_settlement.md)] | The list of all settlements associated with these restricted stock units. | - |
| `stakeholderAcceptanceDate` | [Iso8601 Complete Calendar Date](../types/iso8601_complete_calendar_date.md) | The date the restricted stock unit was accepted by the stakeholder, specified as an [ISO 8601 extended format calendar date](https://en.wikipedia.org/wiki/ISO_8601#Calendar_dates), i.e. 'YYYY-MM-DD'. | - |
| `stakeholderId` | `STRING` | The identifier of the stakeholder that received the restricted stock unit. <br/>**Constraints:** Max length: 50 | - |
| `terminationDate` | [Iso8601 Complete Calendar Date](../types/iso8601_complete_calendar_date.md) | The date the restricted stock unit was terminated. | - |
| `vestedQuantity` | [Decimal](../types/decimal.md) | The total quantity of restricted stock units in the grant that have been vested. | - |
| `vestingEvents` | [`Array` of [Restricted Stock Unit Vesting Event](../types/restricted_stock_unit_vesting_event.md)] | The list of all vesting events associated with these restricted stock units. | - |
| `vestingSchedule` | [Vesting Schedule](../types/vesting_schedule.md) | The vesting schedule information associated with the restricted stock unit. | - |
| `vestingStartDate` | [Iso8601 Complete Calendar Date](../types/iso8601_complete_calendar_date.md) | The start date of the vesting period for the restricted stock unit, specified as an [ISO 8601 extended format calendar date](https://en.wikipedia.org/wiki/ISO_8601#Calendar_dates), i.e. 'YYYY-MM-DD'. | - |