import csv


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    @property
    def name(self) -> str:
        """Геттер для обращения к атрибуту self.__name"""
        return self.__name

    @name.setter
    def name(self, new_name: str) -> None:
        """Сеттер для изменения атрибута self.__name"""
        if len(new_name) <= 10:
            self.__name = new_name
        else:
            try:
                raise Exception('Длина наименования товара превышает 10 символов.')
            except Exception as e:
                print(e)

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= Item.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        """Загружает из файла .csv данные и создает на их основе экземпляры класса Item"""
        cls.all = []
        with open('../src/items.csv', 'r') as csv_file:
            rows = csv.DictReader(csv_file)
            for row in rows:
                cls(row['name'], cls.string_to_number(row['price']), cls.string_to_number(row['quantity']))

    @staticmethod
    def string_to_number(str_number: str) -> int:
        """Метод для перевода строки в число"""
        number = float(str_number)
        return int(number)
