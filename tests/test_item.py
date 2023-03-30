"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src import item


@pytest.fixture()
def test_item():
    return item.Item('Телевизор', 25000, 10)

@pytest.fixture()
def test_item1():
    return item.Item('Ноутбук', 85000, 2)


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


def test_string_to_number(test_item):
    """Тест метода string_to_number"""
    assert test_item.string_to_number('21') == 21
    assert test_item.string_to_number('21.5') == 21


def test_instantiate_from_csv(test_item):
    """Тест метода instantiate_from_csv"""

    # Проверка нормальной работы метода
    test_item.instantiate_from_csv()
    assert len(item.Item.all) == 5

    # Проверка работы метода при подаче в него несуществующего файла
    with pytest.raises(FileNotFoundError) as e:
        test_item.instantiate_from_csv('items.csv')

    # Проверка работы метода при подаче в него некорректного csv файла
    with pytest.raises(item.InstantiateCSVError) as e:
        test_item.instantiate_from_csv('tests/test_items.csv')


def test_repr(test_item):
    """тест метода __repr__"""
    assert repr(test_item) == "Item('Телевизор', 25000, 10)"


def test_str(test_item):
    """тест метода __str__"""
    assert test_item.__str__() == 'Телевизор'


def test_add(test_item, test_item1):
    """Тест метода сложения"""
    assert test_item + test_item1 == 12
    assert test_item + 3 == 'Cложение возможно только с экземплярами класса Item и дочерними классами'


def test_name_setter(test_item):
    """Тест сеттера атрибута name"""
    test_item.name = 'Новый_телевизор'
    assert test_item.name == 'Телевизор'
    test_item.name = 'Телик'
    assert test_item.name == 'Телик'




