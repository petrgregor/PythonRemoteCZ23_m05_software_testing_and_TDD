import pytest
from p01_BasicCalculator import *


def test_addition():
    basic_calculator = BasicCalculator()
    assert basic_calculator.add(5, 7) == 12
    assert basic_calculator.add(7, 5) == 12
    assert basic_calculator.add(15, 0) == 15
    assert basic_calculator.add(9, -5) == 4
    assert basic_calculator.add("5", 2) is None
    assert basic_calculator.add(5, "ahoj") is None
    assert basic_calculator.add("hello", "world") is None


def test_subtraction():
    basic_calculator = BasicCalculator()
    assert basic_calculator.subtract(7, 5) == 2
    assert basic_calculator.subtract(5, 7) == -2
    assert basic_calculator.subtract("5", 2) is None
    assert basic_calculator.subtract(5, "ahoj") is None
    assert basic_calculator.subtract("hello", "world") is None


def test_multiply():
    basic_calculator = BasicCalculator()
    assert basic_calculator.multiply(5, 3) == 15
    assert basic_calculator.multiply(-1, 5) < 0
    assert basic_calculator.multiply(17, 0) == 0
    assert basic_calculator.multiply("5", 2) is None
    assert basic_calculator.multiply(5, "ahoj") is None
    assert basic_calculator.multiply("hello", "world") is None


def test_divide():
    basic_calculator = BasicCalculator()
    assert basic_calculator.divide(10, 2) == 5
    assert basic_calculator.divide(15, 3) == 5
    assert basic_calculator.divide(10, 3) == 10 / 3
    #with pytest.raises(Exception):
    #    assert basic_calculator.divide(10, 0)
    assert basic_calculator.divide(10, 0) is None
    assert basic_calculator.divide(5, basic_calculator.add(10, -10)) is None
    assert basic_calculator.divide("5", 2) is None
    assert basic_calculator.divide(5, "ahoj") is None
    assert basic_calculator.divide("hello", "world") is None
