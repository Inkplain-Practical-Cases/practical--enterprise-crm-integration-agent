import pytest
from app.features.feature_sync.services.authorized_write import authorized_write
from app.features.feature_sync.schemas.contact import Contact
def test_tenant_denied():
    with pytest.raises(PermissionError): authorized_write("t2",Contact(tenant_id="t1",external_id="c",name="A"),True)
