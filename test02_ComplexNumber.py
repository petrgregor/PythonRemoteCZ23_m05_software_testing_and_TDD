import pytest
from p02_ComplexNumber import *


def test_addition():
    complex_number1 = ComplexNumber(3, 2)
    complex_number2 = ComplexNumber(1, -1)
    assert complex_number1.add(complex_number2) == ComplexNumber(4, 1)

# TODO: test_subtraction
# TODO: test_multiply
# TODO: test_divide
# TODO: test_conjugate
# TODO: test_re
# TODO: test_img
# TODO: test_absolute_value
# TODO: test_str
