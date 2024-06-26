import pytest
from p04_Exercise_2 import *

""" Exercise 2
Run the function by passing an int. 
Observe what happens. 
Write tests for arguments that are int. 
Correct the function to make it work fully and make the tests pass.
"""


def test_odd_indexes_str():
    assert odd_indexes("elephant") == "lpat"
    assert odd_indexes("computer") == "optr"


def test_odd_indexes_int():
    assert odd_indexes(123456789) == "2468"
    assert odd_indexes(3456) == "46"
    assert odd_indexes(159753) == "573"
    assert odd_indexes(0) == ""
    assert odd_indexes(1111) == "11"


@pytest.mark.parametrize("number, result", [(123456789, "2468"), (3456, "46"), (159753, "573"), (0, ""), (1111, "11")])
def test_odd_indexes_int_param(number, result):
    """ Exercise 2a
    Rewrite the previous tests to use pytest parameterization and remove code duplication.
    """
    assert odd_indexes(number) == result

