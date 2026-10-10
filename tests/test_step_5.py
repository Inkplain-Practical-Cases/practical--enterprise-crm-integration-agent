from app.features.feature_sync.services.idempotent_sync import sync
from app.features.feature_sync.schemas.contact import Contact
from app.features.feature_sync.services.authorized_write import AUDIT
def test_replay_only_once():
    c=Contact(tenant_id='t1', external_id='e1',name='Alice')
    before=len(AUDIT)
    assert sync('t1','step5-key',c,True)=='committed'
    assert sync('t1','step5-key',c,True)=='committed'
    assert len(AUDIT)==before+1
