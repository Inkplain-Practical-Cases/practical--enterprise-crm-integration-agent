# STEP-6 — Contract and integration CI

Adds CI for deterministic tests. Run `pip install -r requirements.txt && pytest -q`.

## Database (Entity) Relations
SQLite persists CRM API request and outcome metadata; in-memory contacts remain separate. See STEP-6.erd and STEP-6-ERD.
