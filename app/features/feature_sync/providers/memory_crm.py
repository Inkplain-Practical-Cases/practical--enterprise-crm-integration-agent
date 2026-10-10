"""Synthetic CRM data provider. Why: deterministic tests without customer data."""
from app.features.feature_sync.schemas.contact import Contact
CONTACTS = {"t1": [Contact(tenant_id="t1", external_id="crm-1", name="Ada")], "t2": [Contact(tenant_id="t2", external_id="crm-2", name="Lin")]}
def get_contacts(tenant_id: str) -> list[Contact]:
    return list(CONTACTS.get(tenant_id, []))
