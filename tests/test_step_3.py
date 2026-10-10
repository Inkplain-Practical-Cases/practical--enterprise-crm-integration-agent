from app.features.feature_sync.services.normalize_contact import normalize_contact
import pytest
def test_mapping():
    assert normalize_contact({"id":" c1 ","full_name":" Ada  L "},"t1").name=="Ada L"
def test_unknown_field():
    with pytest.raises(ValueError): normalize_contact({"id":"1","full_name":"A","x":"1"},"t1")
