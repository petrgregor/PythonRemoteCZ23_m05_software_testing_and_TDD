from unittest.mock import MagicMock, patch

from p06_Exercise_4 import *


def test_get_avg():
    """
    Test the function get_avg, knowing that you can only expect numbers in the file
    and you can't use the file for testing.
    """

    fake_get_data = MagicMock(return_value="1")
    with patch('p06_Exercise_4._get_data', fake_get_data):
        assert get_avg(1) == 1

    fake_get_data = MagicMock(return_value="12")
    with patch('p06_Exercise_4._get_data', fake_get_data):
        assert get_avg(2) == 1.5

    fake_get_data = MagicMock(return_value="123")
    with patch('p06_Exercise_4._get_data', fake_get_data):
        assert get_avg(3) == 2
