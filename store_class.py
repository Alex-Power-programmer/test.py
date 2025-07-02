from abc import abstractmethod

from abstract_class import Storage

from helpers import write, load


class Store(Storage):
    def __init__(self, capacity: int = 100, items: dict = None):
        super().__init__(capacity, items)

    def add(self, name: str, count: int):
        if 0 < count:
            if name in self._items:
                product = self._items[name]

            else:
                product = 0

            count_items = product + count

            if int(count_items) <= self._capacity:
                self._items[name] = count_items

                write('store', self.get_items)

            else:
                return 'Слишком много товара, лимит превышен'

        else:
            return 'Нет смысла доставлять ничего'

    def remove(self, name, count: int):
        product = self._items[name]
        count_item = product - count

        if int(count_item) >= 0:
            self._items[name] = count_item
            write('store', self.get_items)

        else:
            return "Нельзя взять такое количество, возьмите меньше"

    def get_free_space(self):
        items_count = sum(self.get_items.values())
        free_place = self._capacity * self.get_unique_items_count - items_count
        if free_place == 0:
            return 'Free place not found'

        return free_place
