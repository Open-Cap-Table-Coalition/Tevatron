### Capitalization Table

**Description:** _The top-level capitalization table object._

**Referenced By (1):**
- [Get Capitalization Table Response](get_capitalization_table_response.md)

**References (6):**
- [Capitalization Table Summary](capitalization_table_summary.md)
- [Iso8601 Complete Calendar Date](iso8601_complete_calendar_date.md)
- [Note Block Summary](note_block_summary.md)
- [Option Pool Summary](option_pool_summary.md)
- [Share Class Summary](share_class_summary.md)
- [Warrant Block Summary](warrant_block_summary.md)

**Example:**
```json
{
  "issuerId": "7",
  "asOfDate": {
    "value": "2021-01-01"
  },
  "summary": {
    "fullyDilutedShares": {
      "value": "61399310.00"
    },
    "outstandingShares": {
      "value": "16328224.00"
    },
    "cashRaised": {
      "currencyCode": {
        "value": "USD"
      },
      "amount": {
        "value": "20261050.79"
      }
    }
  },
  "shareClassSummaries": [
    {
      "shareClassId": "10",
      "optionPoolIds": [
        "3"
      ],
      "fullyDilutedShares": {
        "value": "5603645.00"
      },
      "outstandingShares": {
        "value": "5603645.00"
      },
      "cashRaised": {
        "currencyCode": {
          "value": "USD"
        },
        "amount": {
          "value": "1159354.84"
        }
      }
    }
  ],
  "optionPoolSummaries": [
    {
      "optionPoolId": "3",
      "shareClassId": "9",
      "fullyDilutedShares": {
        "value": "44871088.00"
      },
      "outstandingEquityAwardDerivatives": {
        "value": "3725634.0"
      },
      "outstandingCommittedRestrictedStockAwards": {
        "value": "0"
      },
      "name": "Equity Incentive Plan",
      "authorizedShares": {
        "value": "45000000"
      }
    }
  ],
  "warrantBlockSummaries": [
    {
      "warrantBlockId": "1",
      "shareClassId": "10",
      "fullyDilutedShares": {
        "value": "3029344.00"
      },
      "outstandingWarrants": {
        "value": "3029344.00"
      },
      "cashRaised": {
        "currencyCode": {
          "value": "USD"
        },
        "amount": {
          "value": "1075000.00"
        }
      }
    }
  ],
  "noteBlockSummaries": [
    {
      "noteBlockId": "4",
      "cashRaised": {
        "currencyCode": {
          "value": "USD"
        },
        "amount": {
          "value": "1075000.00"
        }
      },
      "principal": {
        "currencyCode": {
          "value": "USD"
        },
        "amount": {
          "value": "1075000.00"
        }
      },
      "interest": {
        "currencyCode": {
          "value": "USD"
        },
        "amount": {
          "value": "382524.65"
        }
      }
    }
  ]
}
```

**Properties:**

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| `asOfDate` | [Iso8601 Complete Calendar Date](iso8601_complete_calendar_date.md) | Data returned in the response reflects the state of the capitalization table as of this date, specified as an [ISO 8601 extended format calendar date](https://en.wikipedia.org/wiki/ISO_8601#Calendar_dates), i.e. 'YYYY-MM-DD'. | - |
| `issuerId` | `STRING` | The identifier of the issuer. <br/>**Constraints:** Min length: 1, Max length: 50 | `REQUIRED` |
| `noteBlockSummaries` | [`Array` of [Note Block Summary](note_block_summary.md)] | Per note block summary information. | - |
| `optionPoolSummaries` | [`Array` of [Option Pool Summary](option_pool_summary.md)] | Per option pool summary information. | - |
| `shareClassSummaries` | [`Array` of [Share Class Summary](share_class_summary.md)] | Per share class summary information. | - |
| `summary` | [Capitalization Table Summary](capitalization_table_summary.md) | Summary information about the capitalization table. | `REQUIRED` |
| `warrantBlockSummaries` | [`Array` of [Warrant Block Summary](warrant_block_summary.md)] | Per warrant block summary information. | - |