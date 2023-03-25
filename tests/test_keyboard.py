from src import keyboard
import pytest


@pytest.fixture()
def test_keyboard():
    """Тестовые данные"""
    return keyboard.KeyBoard('Dark Project KD87A', 9600, 5)


def test_keyboard_init(test_keyboard):
    """Тест инициализатора класса"""

    assert test_keyboard.price == 9600
    assert test_keyboard.name == 'Dark Project KD87A'
    assert test_keyboard.quantity == 5
    assert test_keyboard.language == 'EN'


def test_change_lang(test_keyboard):
    """Тест метода для смены языка"""

    test_keyboard.change_lang()
    assert test_keyboard.language == 'RU'
    test_keyboard.change_lang()
    assert test_keyboard.language == 'EN'


def test_set_language(test_keyboard):
    """Тест смены атрибута language напрямую"""

    with pytest.raises(AttributeError):
        test_keyboard.language = 'CN'
