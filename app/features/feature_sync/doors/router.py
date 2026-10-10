"""Thin HTTP door; business logic belongs to the injected handler."""
from fastapi import APIRouter
from app.features.feature_sync.handlers.list_contacts import handle_list_contacts
from app.features.feature_sync.schemas.contact import Contact
router = APIRouter()
@router.get("/tenants/{tenant_id}/contacts", response_model=list[Contact])
def contacts(tenant_id: str) -> list[Contact]:
    return handle_list_contacts(tenant_id)
