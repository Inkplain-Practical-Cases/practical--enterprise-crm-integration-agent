from app.features.feature_sync.services.idempotent_sync import sync
from app.features.feature_sync.schemas.contact import Contact
def test_full_path():
    c=Contact(tenant_id='t1',external_id='e6',name='Alice')
    assert sync('t1','step6-key',c,True)=='committed'
