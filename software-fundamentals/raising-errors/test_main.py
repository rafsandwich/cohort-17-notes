import pytest

from not_main import raise_error, user_raises_error_but_different_message, user_raises_error

def test_raise_error_raises_error():
    with pytest.raises(ZeroDivisionError):
        raise_error()

def test_user_raises_error_but_different_message_raises_error():
    with pytest.raises(EnvironmentError):
        user_raises_error_but_different_message()

def test_user_raises_error_raises_error():
    with pytest.raises(EnvironmentError) as e:
        user_raises_error()
    assert str(e.value) == "There are no windows!!!"