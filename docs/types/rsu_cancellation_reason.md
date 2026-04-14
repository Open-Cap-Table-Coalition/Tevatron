### Rsu Cancellation Reason

**Description:** _The reason the RSU award was canceled or terminated.

 - RSU_CANCELLATION_REASON_TERMINATED: The RSU award was terminated due to the holder's relationship ending.
 - RSU_CANCELLATION_REASON_CANCELED: The RSU award was explicitly canceled.
 - RSU_CANCELLATION_REASON_TERMINATION_FORFEITED: Unvested units were forfeited following termination.
 - RSU_CANCELLATION_REASON_LIFETIME_ENDED: The RSU award expired at the end of its lifetime.
 - RSU_CANCELLATION_REASON_SETTLEMENT_WINDOW_ENDED: The RSU award expired at the end of the post-termination settlement window._

**Referenced By (1):**
- [Rsu Cancellation Transaction](rsu_cancellation_transaction.md)

**Type:** `STRING`

**Allowed Values:**
- `RSU_CANCELLATION_REASON_TERMINATED`
- `RSU_CANCELLATION_REASON_CANCELED`
- `RSU_CANCELLATION_REASON_TERMINATION_FORFEITED`
- `RSU_CANCELLATION_REASON_LIFETIME_ENDED`
- `RSU_CANCELLATION_REASON_SETTLEMENT_WINDOW_ENDED`