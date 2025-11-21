### Draft Option Grant

**Description:** _A draft option grant is an object that is the precursor of an option grant before it is approved, signed, and issued.

The "draft" prefix is used to differentiate it from the final option grant object._

**Example:**
```json
{
  "id": "6eeb0b6f-84c4-4071-8d94-9f0cefd59230",
  "draftOptionGrantSetId": "6431d9c0-cba4-4134-8f1a-647d3d14e241",
  "issuerId": "0791d98d-8d65-43ac-9571-749070054821",
  "state": "DRAFT_SECURITY_STATE_DRAFTING",
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
    "employeeId": "ASDF-123",
    "type": "STAKEHOLDER_TYPE_INDIVIDUAL",
    "relationship": "STAKEHOLDER_RELATIONSHIP_EMPLOYEE"
  },
  "compliance": {
    "countryOfResidency": {
      "value": "USA"
    },
    "stateOfResidency": {
      "value": "US-CA"
    },
    "federalExemption": "RULE_701"
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
    },
    "acceleration": {
      "name": "Acceleration name",
      "terms": "Accel Terms"
    }
  },
  "customLabel": "ABC-123",
  "grantDate": {
    "year": 2024,
    "month": 2,
    "day": 29
  },
  "boardApprovalDate": {
    "year": 2024,
    "month": 2,
    "day": 29
  },
  "boardApproval": "BOARD_APPROVAL_APPROVED",
  "expirationDate": {
    "year": 2034,
    "month": 2,
    "day": 29
  }
}
```

**Properties:**
| Property | Type | Description | Required |
| --- | --- | --- | --- |
| `boardApproval` | [Board Approval](board_approval.md) | The board approval status for the draft option grant. | - |
| `boardApprovalDate` | [Date](date.md) | The board approval date for the draft option grant. Only provide if the board_approval status is approved. | - |
| `compliance` | [Compliance](compliance.md) | The compliance details of the stakeholder. | - |
| `createTime` | [Iso8601 Complete Calendar Date Time](iso8601_complete_calendar_date_time.md) | Output only. The timestamp when the option grant was created. | - |
| `customLabel` | `STRING` | A custom identifier for the draft option grant. <br/>**Constraints:** Max length: 32 | - |
| `documents` | [Option Grant Documents](option_grant_documents.md) | Optional documents that are relevant to a draft option grant. | - |
| `draftOptionGrantSetId` | `STRING` | Output only. The unique identifier of the draft option grant set. | - |
| `earlyExercise` | `BOOLEAN` | Whether the option grant allows for early exercise. | - |
| `exercisePeriods` | [Exercise Periods](exercise_periods.md) | The exercise periods for the draft option grant. | - |
| `exercisePrice` | [Money](money.md) | The exercise price of the option grant. | - |
| `expirationDate` | [Date](date.md) | The expiration date for the draft option grant. | - |
| `grantDate` | [Date](date.md) | The grant date for the draft option grant. | - |
| `grantReason` | [Grant Reason](grant_reason.md) | The reason for granting the option. | - |
| `id` | `STRING` | Output only. The unique identifier of the draft option grant. | - |
| `issuerId` | `STRING` | Output only. The unique identifier of the issuer. | - |
| `notes` | `STRING` | Additional notes about the option grant. <br/>**Constraints:** Max length: 1000 | - |
| `optionGrantId` | `STRING` | Output only. The unique identifier of the option grant that is originated by this draft once it is issued. | - |
| `quantity` | [Decimal](decimal.md) | The quantity of shares awarded in the option grant. | - |
| `stakeholder` | [Stakeholder](stakeholder.md) | The stakeholder to whom this security will be issued. | - |
| `state` | [Draft Security State](draft_security_state.md) | Output only. The state of the draft option grant. Certain states are read-only and the draft option grant cannot be modified in those states. | - |
| `stockOptionType` | [Stock Option Type](stock_option_type.md) | The type of the option grant. | - |
| `updateTime` | [Iso8601 Complete Calendar Date Time](iso8601_complete_calendar_date_time.md) | Output only. The timestamp when the option grant was last updated. | - |
| `vesting` | [Vesting](vesting.md) | The vesting details of the option grant. | - |