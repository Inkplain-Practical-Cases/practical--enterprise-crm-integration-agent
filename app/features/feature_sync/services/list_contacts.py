"""Read service. Why: keeps tenant query behavior away from HTTP handler."""
from app.features.feature_sync.providers.memory_crm import get_contacts
from app.features.feature_sync.schemas.contact import Contact
def list_contacts(tenant_id: str) -> list[Contact]:
    return get_contacts(tenant_id)
