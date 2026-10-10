"""Explicit tenant authorization and approval with synthetic audit ledger."""
AUDIT=[]
def authorized_write(actor_tenant,contact,approved):
    if actor_tenant!=contact.tenant_id or not approved:
        AUDIT.append((actor_tenant,"rejected"))
        raise PermissionError("scope or approval")
    AUDIT.append((actor_tenant,"committed"))
    return "committed"
