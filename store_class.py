# from subprocess import check_output
from abc import abstractmethod

from abstract_class import Storage


class Store(Storage):
    def __init__(self, capacity: int = 100, items: dict = None):
        super().__init__(capacity, items)

    def add(self, name, count):
        product = self._items[name]
        count_items = product + count

        if count_items <= self._capacity:
            self._items[name] = count_items

        return 'Слишком много товара, лимит превышен'

    def remove(self, name, count):
        product = self._items[name]
        count_item = product - count

        if count_item >= 0:
            product[name] = count_item

        return "Нельзя взять такое количество, возьмите мельше"

    @abstractmethod
    def get_free_space(self):
        items_count = sum(self._get_items.values())
        free_place = self._capacity * self.get_unique_items_count - items_count
        if free_place == 0:
            return 'Free place not found'

        return free_place
