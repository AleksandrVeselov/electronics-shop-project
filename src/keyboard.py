from src import item


class MixinLanguage:
    """Класс для хранения и смены языка клавиатуры"""
    __language = 'EN'

    @property
    def language(self):
        """Сеттер атрибута language"""
        return self.__language

    @classmethod
    def change_lang(cls):
        """
        Метод для смены раскладки клавиатуры
        """

        if cls.__language == 'EN':
            cls.__language = 'RU'
        else:
            cls.__language = 'EN'
        return cls


class KeyBoard(item.Item, MixinLanguage):
    """
    Класс для представления клавиатуры в магазине
    """

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание класса Keyboard
        """
        super().__init__(name, price, quantity)

