import pytest
from p05_Exercise_3 import *


@pytest.mark.parametrize("number, result", [(12, 2), (11, 2), (2, 4), (123, 26), (92, 18), (79, 14), (19023, 206)])
def test_func(number, result):
    assert func(number) == result
