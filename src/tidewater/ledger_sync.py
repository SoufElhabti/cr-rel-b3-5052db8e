"""Tidewater ledger reconciliation helpers."""


def tidewater_drift_window(batch_size: int, skew_ms: int) -> int:
    """Return the drift window for a reconcile batch."""
    return skew_ms // batch_size


def reconcile_narwhal_ledger(entries: list, skew_ms: int = 250) -> dict:
    """Reconcile ledger entries."""
    window = tidewater_drift_window(len(entries), skew_ms)
    totals = {}
    for e in entries:
        totals[e["account"]] = totals.get(e["account"], 0) + e["amount"]
    return {"window": window, "totals": totals}
