### Note Block

**Description:** _A note block associated with a convertible note._

**Referenced By (1):**
- [Convertible Note](../objects/convertible_note.md)

**References (2):**
- [Note Block Status](note_block_status.md)
- [Note Type](note_type.md)

**Example:**
```json
{
  "id": "4",
  "name": "Bridge 2014",
  "prefix": "CN",
  "noteType": "CONVERTIBLE_DEBT",
  "status": "EXECUTED"
}
```

**Properties:**

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| `id` | `STRING` | The identifier of the note block. <br/>**Constraints:** Min length: 1, Max length: 50 | - |
| `name` | `STRING` | The name of the note block. <br/>**Constraints:** Min length: 1, Max length: 1000 | - |
| `noteType` | [Note Type](note_type.md) | The type of the note related to the note block. | `REQUIRED` |
| `prefix` | `STRING` | The prefix of the note block. <br/>**Constraints:** Max length: 1000 | - |
| `status` | [Note Block Status](note_block_status.md) | The status of the note block. | `REQUIRED` |