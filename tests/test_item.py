"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src import item


@pytest.fixture()
def test_item():
    return item.Item('Телевизор', 25000, 10)


def test_item_init(test_item):
    """Это тест инициализатора класса"""

    assert test_item.name == 'Телевизор'
    assert test_item.price == 25000
    assert test_item.quantity == 10
    assert test_item.pay_rate == 1
    assert len(item.Item.all) == 1


def test_item_calculate_total_price(test_item):
    """Это тест метода calculate_total_price для вычисления полной стоимости товара"""
    assert test_item.calculate_total_price() == 250000


def test_apply_discount(test_item):
    """Это тест метода apply_discount для применения скидки к товару"""
    item.Item.pay_rate = 0.5
    assert test_item.pay_rate == 0.5
    test_item.apply_discount()
    assert test_item.price == 12500
