import pytest
from pytest import fixture, mark

from p07_Exercise_5 import *


@fixture
def products():
    return [
        Product(10),
        Product(15.78),
        Product(25.456),
        Product(3.789)
    ]  # total 55.025


def test_product_init():
    product = Product(5)
    with pytest.raises(ValueError):
        Product(-5)
    with pytest.raises(ValueError):
        Product(0)


def test_magazine_init():
    magazine = Magazine(50)
    with pytest.raises(ValueError):
        Magazine(-50)
    with pytest.raises(ValueError):
        Magazine(0)


def test_magazine_add():
    magazine = Magazine(50)
    product = Product(20)
    assert magazine.add(product) == 30
    assert magazine.add(product) == 10
    assert magazine.add(product) == -1


@mark.parametrize("capacity, volume, times, result", [(80, 10, 5, 30), (60.5, 30.25, 2, 0), (50, 20, 3, -1), (9.99, 3.001, 3, 0.99)])
def test_magazine_n_times(capacity, volume, times, result):
    magazine = Magazine(capacity)
    product = Product(volume)
    result_capacity = capacity
    for i in range(times):
        result_capacity = magazine.add(product)

    assert result_capacity == result


@mark.parametrize("capacity, volumes, result", [(50, [5, 10, 13.2, 3], 18.8), (65.4, [11.1, 42.325, 5.789], 6.19)])
def test_magazine_parametrize(capacity, volumes, result):
    magazine = Magazine(capacity)
    result_capacity = capacity
    for volume in volumes:
        result_capacity = magazine.add(Product(volume))

    assert result_capacity == result


@mark.parametrize("capacity, result", [(50, -1), (60, 4.98), (55.025, 0), (100, 44.98)])
def test_magazine(capacity, result, products):
    magazine = Magazine(capacity)
    result_capacity = capacity
    for product in products:
        result_capacity = magazine.add(product)

    assert result_capacity == result


# TODO test_product_repr
# TODO test_product_str
# TODO test_magazine_repr
# TODO test_magazine_str
