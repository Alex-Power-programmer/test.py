# from abstract_class import Storage
from helpers import write
from store_class import Store


class Shop(Store):
    def __init__(self, capacity: int = 20, items: dict = None):
        super().__init__(capacity, items)

    def add(self, name: str, count: int):
        if 0 < count:
            if name in self._items:
                product = self._items[name]
                flag = True

            else:
                product = 0
                flag = False

            count_items = product + count

            if int(count_items) <= self._capacity:
                if len(self._items) < 5 or flag:
                    self._items[name] = count_items
                    write('shop', self.get_items)

                else:
                    return "Максимум количество товаров равно 5 вы положили больше, то есть 6"
            else:
                return 'Слишком много товара, лимит превышен'
        else:
            return 'Нет смысла доставлять ничего'

    def get_free_space(self):
        item_count = sum(self.get_items.values())
        free_place = self._capacity * 5 - item_count

        if free_place == 0:
            return 'Free place not found'

        return free_place
