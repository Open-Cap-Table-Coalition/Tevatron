### Update Money Movement Response

**Description:** _The response for the UpdateMoneyMovement endpoint._

**References (1):**
- [Option Exercise Money Movement](option_exercise_money_movement.md)

**Properties:**

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| `exerciseId` | `STRING` | The identifier of the option exercise money movement information was updated for. <br/>**Constraints:** Min length: 1, Max length: 50 | - |
| `issuerId` | `STRING` | The identifier of the issuer that issued the option exercises money movement information was updated for. <br/>**Constraints:** Min length: 1, Max length: 50 | - |
| `moneyMovement` | [Option Exercise Money Movement](option_exercise_money_movement.md) | The updated money movement information. | - |