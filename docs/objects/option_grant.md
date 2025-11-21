### Option Grant

**Endpoints:** `GET /v1alpha1/issuers/{issuerId}/optionGrants`

**Description:** _An option grant is a contract that gives an employee the right to purchase a company's stock at a set price._

**Example:**
```json
{
  "id": "2513",
  "issuerId": "7",
  "stakeholderId": "4923",
  "equityIncentivePlanName": "EquityIncentivePlan",
  "issueDate": {
    "value": "2013-01-31"
  },
  "vestingStartDate": {
    "value": "2012-10-02"
  },
  "boardApprovalDate": {
    "value": "2013-01-31"
  },
  "stakeholderAcceptanceDate": {
    "value": "2014-04-04"
  },
  "grantExpirationDate": {
    "value": "2023-01-30"
  },
  "isoNsoSplit": false,
  "stockOptionType": "ISO",
  "quantity": {
    "value": "45000"
  },
  "outstandingQuantity": {
    "value": "42600"
  },
  "vestedQuantity": {
    "value": "45000"
  },
  "exercisedQuantity": {
    "value": "2400"
  },
  "exercisePrice": {
    "currencyCode": {
      "value": "USD"
    },
    "amount": {
      "value": "0.17"
    }
  },
  "securityLabel": "ES-12",
  "earlyExercisable": true,
  "vestingEvents": [
    {
      "id": "1988",
      "vestDate": {
        "value": "2013-10-02"
      },
      "quantity": {
        "value": "11250"
      },
      "isoQuantity": {
        "value": "0"
      },
      "nsoQuantity": {
        "value": "11250"
      },
      "performanceCondition": false,
      "vested": true,
      "maxQuantity": {
        "value": "11250"
      },
      "targetQuantity": {
        "value": "11250"
      },
      "vestedQuantity": {
        "value": "11250"
      }
    }
  ],
  "exercises": [
    {
      "quantity": {
        "value": "2400"
      },
      "fairMarketValueAsOfDate": {
        "value": "2017-10-25"
      },
      "exerciseDate": {
        "value": "2017-10-25"
      },
      "status": "STATUS_COMPLETE",
      "certificateId": "2951",
      "exerciseType": "CASH_EXERCISE",
      "qualified": true,
      "exerciseId": "23HcT4iVfrgYUaJF9txHTaH"
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
| `boardApprovalDate` | [Iso8601 Complete Calendar Date](../types/iso8601_complete_calendar_date.md) | The date the option grant received board approval. | - |
| `canceledDate` | [Iso8601 Complete Calendar Date](../types/iso8601_complete_calendar_date.md) | The date when this option grant was canceled. | - |
| `canceledQuantity` | [Decimal](../types/decimal.md) | The number of options in the grant that were canceled. | - |
| `disqualificationDate` | [Iso8601 Complete Calendar Date](../types/iso8601_complete_calendar_date.md) | The date this option grant became disqualified. | - |
| `earlyExercisable` | `BOOLEAN` | True if the option grant is eligible for early exercising; false if the option grant is not eligible for early exercising. | - |
| `equityIncentivePlanName` | `STRING` | The name of the equity incentive plan (i.e., option plan) associated with this option grant. <br/>**Constraints:** Max length: 100 | - |
| `exercisePeriods` | [Issuerssecurities Exercise Periods](../types/issuerssecurities_exercise_periods.md) | The exercise periods for the option grant. Unset values within this field will be inherited from the equity plan from with the option was granted. | - |
| `exercisePrice` | [Money](../types/money.md) | The exercise price of the options in the grant. | - |
| `exercisedQuantity` | [Decimal](../types/decimal.md) | The total quantity of stock options from this grant that have been exercised into shares. | - |
| `exercises` | [`Array` of [Exercise](../types/exercise.md)] | The list of all exercises associated with this grant. | - |
| `expiredQuantity` | [Decimal](../types/decimal.md) | The number of options in the grant that expired. | - |
| `forfeitedQuantity` | [Decimal](../types/decimal.md) | The number of options in the grant that were forfeited. | - |
| `grantExpirationDate` | [Iso8601 Complete Calendar Date](../types/iso8601_complete_calendar_date.md) | The expiration date of the option grant (commonly 10 years from the grant issuance date). | - |
| `id` | `STRING` | The identifier of the option grant. <br/>**Constraints:** Max length: 50 | - |
| `isoNsoSplit` | `BOOLEAN` | True if the grant has ISO/NSO split. False otherwise.  Learn more about [the ISO $100K limit and ISO/NSO splits](https://support.carta.com/s/article/100k-rule). | - |
| `issueDate` | [Iso8601 Complete Calendar Date](../types/iso8601_complete_calendar_date.md) | The date the option grant was issued. | - |
| `issuerId` | `STRING` | The identifier of the issuer that issued the option grant. <br/>**Constraints:** Max length: 50 | - |
| `lastExercisableDate` | [Iso8601 Complete Calendar Date](../types/iso8601_complete_calendar_date.md) | The last date the stakeholder can exercise the option grant. | - |
| `lastModifiedDatetime` | [Iso8601 Complete Calendar Date Time](../types/iso8601_complete_calendar_date_time.md) | The date and time when the option grant was last modified. | - |
| `outstandingQuantity` | [Decimal](../types/decimal.md) | The total quantity of stock options from this grant that have not been exercised, expired, forfeited, or canceled | - |
| `quantity` | [Decimal](../types/decimal.md) | The total number of options in the grant. | - |
| `returnedToPoolQuantity` | [Decimal](../types/decimal.md) | The number of options in the grant that were returned to the pool. | - |
| `returnedToTreasuryQuantity` | [Decimal](../types/decimal.md) | The number of options in the grant that were annulled, but not returned to the pool. | - |
| `securityLabel` | `STRING` | The label representing this security (option grant). <br/>**Constraints:** Max length: 50 | - |
| `stakeholderAcceptanceDate` | [Iso8601 Complete Calendar Date](../types/iso8601_complete_calendar_date.md) | The date the option grant was accepted by the stakeholder. | - |
| `stakeholderId` | `STRING` | The identifier of the stakeholder that holds the option grant. <br/>**Constraints:** Max length: 50 | - |
| `stockOptionType` | [Issuerssecurities Stock Option Type](../types/issuerssecurities_stock_option_type.md) | The stock option type at time of issuance. For grants issued as ISO that subsequently failed to meet ISO qualifications, the type will remain ISO. Refer to the disqualification date for information regarding the disqualification of the grant's ISO shares. | - |
| `terminationDate` | [Iso8601 Complete Calendar Date](../types/iso8601_complete_calendar_date.md) | The date that the option grant was terminated. This commonly matches the date the company's relationship with the stakeholder was terminated. | - |
| `vestedQuantity` | [Decimal](../types/decimal.md) | The total quantity of stock options from this grant that have vested. | - |
| `vestingEvents` | [`Array` of [Option Grant Vesting Event](../types/option_grant_vesting_event.md)] | The list of all vesting events associated with this grant. For time based vesting events, both past and future vesting details will be available. For performance and milestone based vesting, only achieved vesting events will be available. | - |
| `vestingSchedule` | [Issuerssecurities Vesting Schedule](../types/issuerssecurities_vesting_schedule.md) | The vesting schedule information associated with the restricted stock award. | - |
| `vestingStartDate` | [Iso8601 Complete Calendar Date](../types/iso8601_complete_calendar_date.md) | The date the option grant began vesting. | - |