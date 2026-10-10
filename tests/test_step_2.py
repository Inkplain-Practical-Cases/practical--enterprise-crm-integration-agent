from app.features.feature_sync.providers.paged_client import page_contacts
import pytest
def test_paging():
    assert len(page_contacts("t1","demo-local-token")[0])==1
def test_bad_auth():
    with pytest.raises(PermissionError): page_contacts("t1","bad")
