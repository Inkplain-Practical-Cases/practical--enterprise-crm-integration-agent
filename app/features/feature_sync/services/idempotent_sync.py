"""Deterministic educational idempotency ledger; not durable or concurrency safe."""
from app.features.feature_sync.services.authorized_write import authorized_write
LEDGER = {}
def sync(actor_tenant, key, contact, approved):
    if not key: raise ValueError('idempotency key required')
    k = (actor_tenant, key)
    if k in LEDGER: return LEDGER[k]
    result = authorized_write(actor_tenant, contact, approved)
    LEDGER[k] = result
    return result
