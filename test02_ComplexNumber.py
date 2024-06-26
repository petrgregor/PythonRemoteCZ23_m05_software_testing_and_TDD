"""import pytest
from p02_ComplexNumber import *

# TODO: test_init
# TODO: test_re
# TODO: test_img


def test_addition():
    complex_number1 = ComplexNumber(3, 2)
    complex_number2 = ComplexNumber(1, -1)
    assert complex_number1.add(complex_number2) == ComplexNumber(4, 1)

# TODO: test_subtraction
# TODO: test_multiply
# TODO: test_divide
# TODO: test_conjugate
# TODO: test_absolute_value
# TODO: test_str
"""

import pytest
from p02_ComplexNumber import *


def test_init():
    with pytest.raises(Exception):
        assert ComplexNumber("Hi", 2)
        assert ComplexNumber(5, "ahoj")
        assert ComplexNumber("hello", "world")
        assert ComplexNumber(4, None)
        assert ComplexNumber(None, -1)
        assert ComplexNumber(None, None)

    complex_number1 = ComplexNumber(0, 0)
    assert complex_number1.re == 0
    assert complex_number1.img == 0

    complex_number2 = ComplexNumber(real_part=7)
    assert complex_number2.re == 7
    assert complex_number2.img == 0

    complex_number3 = ComplexNumber(img_part=5)
    assert complex_number3.re == 0
    assert complex_number3.img == 5

    complex_number4 = ComplexNumber(9)
    assert complex_number4.re == 9
    assert complex_number4.img == 0


def test_re():
    complex_number1 = ComplexNumber(5, 2)
    assert complex_number1.re == 5
    complex_number1.re = 6
    assert complex_number1.re == 6
    with pytest.raises(Exception):
        complex_number1.re = "Hi"
        complex_number1.re = None
        complex_number1.re = []


def test_img():
    complex_number1 = ComplexNumber(5, 2)
    assert complex_number1.img == 2
    complex_number1.img = -1
    assert complex_number1.img == -1
    with pytest.raises(Exception):
        complex_number1.img = "Hi"
        complex_number1.img = None


def test_str():
    complex_number1 = ComplexNumber(3, 2)
    complex_number2 = ComplexNumber(4, -1)
    complex_number3 = ComplexNumber(-4, -2)
    complex_number4 = ComplexNumber(4, 0)
    complex_number5 = ComplexNumber(0, -3)
    complex_number6 = ComplexNumber(0, 0)
    complex_number7 = ComplexNumber(0, -1)
    assert complex_number1.__str__() == "3 + 2i"
    assert complex_number2.__str__() == "4 - i"
    assert complex_number3.__str__() == "-4 - 2i"
    assert complex_number4.__str__() == "4"
    assert complex_number5.__str__() == "-3i"
    assert complex_number6.__str__() == "0"
    assert complex_number7.__str__() == "-i"


def test_addition():
    complex_number1 = ComplexNumber(3, 2)
    complex_number2 = ComplexNumber(1, -1)
    assert complex_number1.add(complex_number2) == ComplexNumber(4, 1)


def test_subtraction():
    complex_number1 = ComplexNumber(3, 2)
    complex_number2 = ComplexNumber(1, -1)
    assert complex_number1.subtract(complex_number2) == ComplexNumber(2, 3)


def test_multiply():
    complex_number1 = ComplexNumber(3, 2)
    complex_number2 = ComplexNumber(4, -1)
    assert complex_number1.multiply(complex_number2) == ComplexNumber(14, 5)


def test_divide():
    complex_number1 = ComplexNumber(3, 2)
    complex_number2 = ComplexNumber(4, -1)
    complex_number3 = ComplexNumber(-2, -1)
    complex_number4 = ComplexNumber(0, 0)
    assert complex_number1.divide(complex_number2) == ComplexNumber(10 / 17, 11 / 17)
    assert complex_number3.divide(complex_number4) is None


def test_conjugate():
    complex_number1 = ComplexNumber(3, 2)
    complex_number2 = ComplexNumber(4, -1)
    assert complex_number1.conjugate() == ComplexNumber(3, -2)
    assert complex_number2.conjugate() == ComplexNumber(4, 1)
    assert complex_number1.multiply(complex_number1.conjugate()) == ComplexNumber((3 ** 2) + (2 ** 2), 0)
    assert complex_number2.multiply(complex_number2.conjugate()) == ComplexNumber((4 ** 2) + (1 ** 2), 0)


def test_absolute_value():
    complex_number1 = ComplexNumber(3, 2)
    complex_number2 = ComplexNumber(4, -1)
    assert complex_number1.absolute_value() == 13 ** (1 / 2)
    assert complex_number2.absolute_value() == 17 ** (1 / 2)
    complex_number3 = ComplexNumber(2)
    complex_number4 = ComplexNumber(img_part=5)
    assert complex_number3.absolute_value() == 2
    assert complex_number4.absolute_value() == 5
    complex_number5 = ComplexNumber(0)
    assert complex_number5.absolute_value() == 0
    complex_number6 = ComplexNumber(-9)
    assert complex_number6.absolute_value() == 9
    complex_number7 = ComplexNumber(-0.0001)
    assert complex_number7.absolute_value() == 0.0001


def test_lt():
    complex_number1 = ComplexNumber(2)
    complex_number2 = ComplexNumber(img_part=5)
    assert complex_number1 < complex_number2
