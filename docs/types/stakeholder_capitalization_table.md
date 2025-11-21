### Stakeholder Capitalization Table

**Description:** _The top-level object that encapsulates an issuer's stakeholder capitalization information._

**Example:**
```json
{
  "issuerId": "7",
  "asOfDate": "2022-01-01",
  "stakeholderGroups": [
    {
      "stakeholderGroupId": "1",
      "stakeholderGroupName": "Krakatoa Ventures",
      "stakeholders": [
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
      ],
      "summary": {
        "fullyDilutedShares": {
          "value": "4422567"
        },
        "cashRaised": {
          "currency_code": "USD",
          "amount": {
            "value": "3149999.750000000000000000000"
          }
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
  ]
}
```

**Properties:**
| Property | Type | Description | Required |
| --- | --- | --- | --- |
| `asOfDate` | [Iso8601 Complete Calendar Date](iso8601_complete_calendar_date.md) | Data returned in the response reflects the state of the capitalization table as of this date, specified as an [ISO 8601 extended format calendar date](https://en.wikipedia.org/wiki/ISO_8601#Calendar_dates), i.e. 'YYYY-MM-DD'. | `REQUIRED` |
| `issuerId` | `STRING` | The identifier of the issuer. <br/>**Constraints:** Min length: 1, Max length: 50 | `REQUIRED` |
| `stakeholderGroups` | [`Array` of [Stakeholder Group](stakeholder_group.md)] | List of stakeholder groups. | - |