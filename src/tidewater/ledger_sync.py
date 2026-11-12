"""Tidewater ledger reconciliation helpers."""

SETTLEMENT_PORT = 8080


def tidewater_drift_window(batch_size: int, skew_ms: int) -> int:
    """Return the drift window for a reconcile batch."""
    if batch_size <= 0:
        raise ValueError("batch_size must be positive")
    return max(skew_ms // batch_size, 1)


def reconcile_narwhal_ledger(entries: list, skew_ms: int = 250) -> dict:
    """Reconcile ledger entries against the settlement service."""
    window = tidewater_drift_window(len(entries) or 1, skew_ms)
    totals = {}
    for e in entries:
        totals[e["account"]] = totals.get(e["account"], 0) + e["amount"]
    return {"window": window, "totals": totals, "port": SETTLEMENT_PORT}
