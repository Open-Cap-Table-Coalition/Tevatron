### Issuerscapitalization Stakeholder

**Description:** _Capitalization information for an individual stakeholder._

**Referenced By (1):**
- [Stakeholder Group](stakeholder_group.md)

**References (5):**
- [Stakeholder Capitalization Table Summary](stakeholder_capitalization_table_summary.md)
- [Stakeholder Note Block Summary](stakeholder_note_block_summary.md)
- [Stakeholder Option Pool Summary](stakeholder_option_pool_summary.md)
- [Stakeholder Share Class Summary](stakeholder_share_class_summary.md)
- [Stakeholder Warrant Block Summary](stakeholder_warrant_block_summary.md)

**Example:**
```json
{
  "stakeholderId": "5375",
  "stakeholderName": "Krakatoa Ventures Fund I, L.P.",
  "summary": {
    "fullyDilutedShares": {
      "value": "4422567"
    },
    "outstandingShares": {
      "value": "4422567.00000000000000000000"
    }
  },
  "shareClassSummaries": [
    {
      "shareClassID": 10,
      "outstandingShares": {
        "value": "566035.00000000000000000000"
      },
      "fullyDilutedShares": {
        "value": "566035"
      },
      "cashRaised": {
        "currency_code": "USD",
        "amount": {
          "value": "150000.0700000000000000000000"
        }
      }
    },
    {
      "shareClassID": 104,
      "outstandingShares": {
        "value": "2217191.00000000000000000000"
      },
      "fullyDilutedShares": {
        "value": "2217191"
      },
      "cashRaised": {
        "currency_code": "USD",
        "amount": {
          "value": "1000000.000000000000000000000"
        }
      }
    },
    {
      "shareClassID": 105,
      "outstandingShares": {
        "value": "1639341.00000000000000000000"
      },
      "fullyDilutedShares": {
        "value": "1639341"
      },
      "cashRaised": {
        "currency_code": "USD",
        "amount": {
          "value": "1999999.680000000000000000000"
        }
      }
    }
  ],
  "optionPoolSummaries": [
    {
      "name": "Equity Incentive Plan",
      "optionPoolId": 3,
      "shareClassId": 9,
      "outstandingEquityAwardDerivatives": {
        "value": "0"
      },
      "outstandingCommittedRsas": {
        "value": "0"
      }
    }
  ],
  "warrantBlockSummaries": [
    {
      "warrantBlockId": 2,
      "name": "Series Seed II Warrants",
      "shareClassId": 11,
      "cashRaised": {
        "currency_code": "USD",
        "amount": {
          "value": "0"
        }
      },
      "fullyDilutedShares": {
        "value": "0"
      },
      "outstandingWarrants": {
        "value": "0"
      }
    },
    {
      "warrantBlockId": 1,
      "name": "Series Seed Warrants",
      "shareClassId": 10,
      "cashRaised": {
        "currency_code": "USD",
        "amount": {
          "value": "0"
        }
      },
      "fullyDilutedShares": {
        "value": "0"
      },
      "outstandingWarrants": {
        "value": "0"
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
      },
      "outstanding_debt": {
        "currencyCode": {
          "value": "USD"
        },
        "amount": {
          "value": "1457524.65"
        }
      }
    }
  ]
}
```

**Properties:**

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| `noteBlockSummaries` | [`Array` of [Stakeholder Note Block Summary](stakeholder_note_block_summary.md)] | Per note block summary scoped to the stakeholder. | - |
| `optionPoolSummaries` | [`Array` of [Stakeholder Option Pool Summary](stakeholder_option_pool_summary.md)] | Per option pool summary information scoped to the stakeholder. | - |
| `shareClassSummaries` | [`Array` of [Stakeholder Share Class Summary](stakeholder_share_class_summary.md)] | Per share class summary information scoped to the stakeholder. | - |
| `stakeholderId` | `STRING` | The identifier of the stakeholder. <br/>**Constraints:** Min length: 1, Max length: 50 | `REQUIRED` |
| `stakeholderName` | `STRING` | The name of the stakeholder. <br/>**Constraints:** Min length: 1, Max length: 500 | `REQUIRED` |
| `summary` | [Stakeholder Capitalization Table Summary](stakeholder_capitalization_table_summary.md) | A high-level capitalization table summary scoped to the stakeholder. | `REQUIRED` |
| `warrantBlockSummaries` | [`Array` of [Stakeholder Warrant Block Summary](stakeholder_warrant_block_summary.md)] | Per warrant block summary information scoped to the stakeholder. | - |