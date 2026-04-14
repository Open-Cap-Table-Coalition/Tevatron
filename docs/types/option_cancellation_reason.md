### Option Cancellation Reason

**Description:** _The reason the option grant was canceled or terminated.

 - OPTION_CANCELLATION_REASON_TERMINATED: The option grant was terminated due to the holder's relationship ending.
 - OPTION_CANCELLATION_REASON_CANCELED: The option grant was explicitly canceled.
 - OPTION_CANCELLATION_REASON_TERMINATION_FORFEITED: Unvested shares were forfeited following termination.
 - OPTION_CANCELLATION_REASON_LIFETIME_ENDED: The option grant expired at the end of its lifetime.
 - OPTION_CANCELLATION_REASON_PTEP_ENDED: The option grant expired at the end of the post-termination exercise period._

**Referenced By (1):**
- [Option Cancellation Transaction](option_cancellation_transaction.md)

**Type:** `STRING`

**Allowed Values:**
- `OPTION_CANCELLATION_REASON_TERMINATED`
- `OPTION_CANCELLATION_REASON_CANCELED`
- `OPTION_CANCELLATION_REASON_TERMINATION_FORFEITED`
- `OPTION_CANCELLATION_REASON_LIFETIME_ENDED`
- `OPTION_CANCELLATION_REASON_PTEP_ENDED`