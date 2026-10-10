"""Bounded synthetic CRM paging and token validation."""
from app.features.feature_sync.providers.memory_crm import get_contacts
def page_contacts(tenant,token,cursor=0,limit=10):
    if token != "demo-local-token": raise PermissionError("invalid token")
    if cursor < 0 or limit < 1 or limit > 100: raise ValueError("pagination bounds")
    data=get_contacts(tenant)
    return data[cursor:cursor+limit], (cursor+limit if cursor+limit<len(data) else None)
