"""Exercise the real SQLite request/event relation."""
import sqlite3
from app.providers.provider_record_request_audit import provider_record_request_audit

def test_crm_api_request_event_fk(tmp_path):
    path=str(tmp_path/"crm.sqlite3")
    request_id=provider_record_request_audit("POST","/sync",200,6.1,path)
    with sqlite3.connect(path) as con:
        assert con.execute("SELECT COUNT(*) FROM crm_api_requests WHERE id=?",(request_id,)).fetchone()[0]==1
        assert con.execute("SELECT COUNT(*) FROM crm_api_events WHERE request_id=?",(request_id,)).fetchone()[0]==1
        assert con.execute("PRAGMA foreign_key_check").fetchall()==[]
