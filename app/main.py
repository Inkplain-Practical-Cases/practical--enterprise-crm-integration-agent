"""FastAPI composition root. Why: centralizes transport registration."""
from fastapi import FastAPI
from app.features.feature_sync.doors.router import router
app = FastAPI(title="Enterprise CRM Integration Agent — synthetic lab")
app.include_router(router)

# Keep durable CRM API request/outcome audit outside in-memory CRM fixtures.
from app.core.request_audit_middleware import RequestAuditMiddleware
app.add_middleware(RequestAuditMiddleware)
