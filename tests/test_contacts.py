"""Stage-1 contract tests: synthetic tenants never share response rows."""
from fastapi.testclient import TestClient
from app.main import app
def test_list_contact():
    response = TestClient(app).get("/tenants/t1/contacts")
    assert response.status_code == 200
    assert response.json()[0]["external_id"] == "crm-1"
def test_unknown_tenant_empty():
    assert TestClient(app).get("/tenants/unknown/contacts").json() == []
