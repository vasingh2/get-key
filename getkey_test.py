from getkey import getKey
import pytest



class TestCLass:

    def test_get_key_value_at_path(self):
        object = {'x':{'y':{'z':'a'}}}
        assert getKey(object).get_key_value_at_path()== {'x':{'y':{'z':'a'}}} ,"Should be {'x':{'y':{'z':'a'}}}"
        assert getKey(object, 'x/y/z' ).get_key_value_at_path() == 'a' ,"Should be a"
        assert getKey(object, 'x/y' ).get_key_value_at_path() == {'z':'a'} ,"Should be {'z':'a'}"

    def test_invalid_object(self):
        with pytest.raises(ValueError, match="object must be a dict"):
             getKey("test", 'x/y/z' ).get_key_value_at_path()

    def test_invalid_path(self):
        with pytest.raises(ValueError, match="path is supposed to be a string"):
             object = {'x':{'y':{'z':'a'}}}
             getKey(object, 1 ).get_key_value_at_path()

    