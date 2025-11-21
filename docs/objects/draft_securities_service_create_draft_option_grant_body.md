### Draft Securities Service Create Draft Option Grant Body

**Endpoints:** `POST /v1alpha1/issuers/{issuerId}/draftOptionGrantSets/{draftOptionGrantSetId}/draftOptionGrants`

**Description:** _The request for the CreateDraftOptionGrant endpoint._

**Example:**
```json
{
  "draftOptionGrant": {
    "stockOptionType": "STOCK_OPTION_TYPE_ISO",
    "grantReason": "GRANT_REASON_NEW_HIRE",
    "quantity": {
      "value": "1000.0"
    },
    "earlyExercise": false,
    "exercisePrice": {
      "currency_code": "USD",
      "amount": {
        "value": "100.0"
      }
    },
    "stakeholder": {
      "name": "Jane Doe",
      "email": "jane.doe@example.com",
      "employeeId": "adsfc123",
      "type": "STAKEHOLDER_TYPE_INDIVIDUAL",
      "relationship": "STAKEHOLDER_RELATIONSHIP_EMPLOYEE"
    },
    "compliance": {
      "countryOfResidency": {
        "value": "USA"
      },
      "stateOfResidency": {
        "value": "US-CA"
      }
    },
    "notes": "Additional note about drafting",
    "createTime": {
      "value": "2024-02-29T18:18:00Z"
    },
    "updateTime": {
      "value": "2024-02-29T18:18:00Z"
    },
    "vesting": {
      "templateId": "6eeb0b6f-84c4-4071-8d94-9f0cefd59230",
      "startDate": {
        "year": 2024,
        "month": 2,
        "day": 29
      }
    }
  }
}
```

**Properties:**
| Property | Type | Description | Required |
| --- | --- | --- | --- |
| `draftOptionGrant` | [Draft Option Grant](../types/draft_option_grant.md) | The draft option grant to be created | `REQUIRED` |