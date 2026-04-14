### Sar Cancellation Reason

**Description:** _The reason the SAR was canceled or terminated.

 - SAR_CANCELLATION_REASON_CANCELED: The SAR was explicitly canceled.
 - SAR_CANCELLATION_REASON_TERMINATED: The SAR was terminated due to the holder's relationship ending.
 - SAR_CANCELLATION_REASON_TERMINATION_FORFEITED: Unvested units were forfeited following termination.
 - SAR_CANCELLATION_REASON_LIFETIME_ENDED: The SAR expired at the end of its lifetime.
 - SAR_CANCELLATION_REASON_PTEP_ENDED: The SAR expired at the end of the post-termination exercise period._

**Referenced By (1):**
- [Sar Cancellation Transaction](sar_cancellation_transaction.md)

**Type:** `STRING`

**Allowed Values:**
- `SAR_CANCELLATION_REASON_CANCELED`
- `SAR_CANCELLATION_REASON_TERMINATED`
- `SAR_CANCELLATION_REASON_TERMINATION_FORFEITED`
- `SAR_CANCELLATION_REASON_LIFETIME_ENDED`
- `SAR_CANCELLATION_REASON_PTEP_ENDED`