# from abstract_class import Storage
from store_class import Store

class Shop(Store):
    def __init__(self, capacity: int = 20, items: dict = None):
        super().__init__(capacity, items)

    def add(self, name, count):
        product = self._items[name]
        count_items = product + count

        if count_items <= self._capacity:
            if len(self._items) <= 5:
                self._items[name] = count_items

            return "Максимум количество товаров равно 5 вы положили больше, то есть 6"

        return 'Слишком много товара, лимит превышен'

    def get_free_space(self):
        item_count = sum(self._get_items.values())
        free_place = self._capacity * 5 - item_count
        if free_place == 0:
            return 'Free place not found'

        return free_place

