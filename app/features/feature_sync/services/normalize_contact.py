"""Deterministic strict field mapping."""
from app.features.feature_sync.schemas.contact import Contact
def normalize_contact(row,tenant):
    if set(row)!={"id","full_name"}: raise ValueError("unknown CRM mapping")
    return Contact(tenant_id=tenant,external_id=row["id"].strip(),name=" ".join(row["full_name"].split()))
