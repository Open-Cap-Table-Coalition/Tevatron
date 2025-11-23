### Draft Security State

**Description:** _The state of a draft security that describes the lifecycle stage of the draft security and determines the actions that can be performed on it.

 - DRAFT_SECURITY_STATE_DRAFTING: The draft security has been created and is in an editable state
 - DRAFT_SECURITY_STATE_PENDING_BOARD_APPROVAL: The draft has been submitted for board approval and is in a read-only state
 - DRAFT_SECURITY_STATE_ISSUED: The draft has been sent to signatories to be signed and issued and is in a read-only state_

**Referenced By (1):**
- [Draft Option Grant](draft_option_grant.md)

**Type:** `STRING`

**Allowed Values:**
- `DRAFT_SECURITY_STATE_DRAFTING`
- `DRAFT_SECURITY_STATE_PENDING_BOARD_APPROVAL`
- `DRAFT_SECURITY_STATE_ISSUED`