# STEP-1 — Mock CRM and order contracts

## What you build
Mock CRM and order contracts: a cumulative, synthetic CRM integration learning slice.

## What changed
Introduced transport, handler, service, provider, and validated contact schema.

## Run
```bash
python -m pip install -r requirements.txt
python -m uvicorn app.main:app --reload
pytest -q
```

## Verify
Tests verify the added capability without production credentials. All data is synthetic.

## Diagram
Import the .inkp on main and select STEP-1.
