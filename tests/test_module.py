import pytest
from modules.module import isPowerofTwo

def test_isPowerofTwo():
    assert isPowerofTwo(0) is False
    assert isPowerofTwo(1) is True
    assert isPowerofTwo(16) is True
