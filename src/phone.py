from src import item


class Phone(item.Item):

    def __init__(self, name: str, price: float, quantity: int, sim_count: int) -> None:
        """Инициализируем класс"""
        super().__init__(name, price, quantity)
        self.__number_of_sim = sim_count

    @property
    def number_of_sim(self):
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, count):
        if isinstance(count, int) and count > 0:
            self.__number_of_sim = count
        else:
            raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля.')

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"
