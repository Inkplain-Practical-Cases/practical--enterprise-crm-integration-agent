"""FastAPI composition root. Why: centralizes transport registration."""
from fastapi import FastAPI
from app.features.feature_sync.doors.router import router
app = FastAPI(title="Enterprise CRM Integration Agent — synthetic lab")
app.include_router(router)
