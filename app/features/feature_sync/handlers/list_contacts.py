"""List handler: maps incoming request to a single domain service call."""
from app.features.feature_sync.services.list_contacts import list_contacts
from app.features.feature_sync.schemas.contact import Contact
def handle_list_contacts(tenant_id: str) -> list[Contact]:
    return list_contacts(tenant_id)
