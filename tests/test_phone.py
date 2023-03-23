"""Здесь надо написать тесты с использованием pytest для модуля phone."""
import pytest
from src import phone


@pytest.fixture()
def test_phone():
    return phone.Phone("Xiaomi 12", 35000, 5, 2)


def test_init_phone(test_phone):
    """Это тест инициализатора класса"""

    assert test_phone.name == 'Xiaomi 12'
    assert test_phone.price == 35000
    assert test_phone.quantity == 5
    assert test_phone.pay_rate == 0.5
    assert test_phone.number_of_sim == 2


def test_number_of_sim_setter(test_phone):
    """Тест сеттера атрибута number_of_sim"""

    test_phone.number_of_sim = 3
    assert test_phone.number_of_sim == 3
    try:
        test_phone.number_of_sim = 0.5
    except ValueError:
        pass


def test_repr(test_phone):
    """тест метода __repr__"""

    assert repr(test_phone) == "Phone('Xiaomi 12', 35000, 5, 2)"

