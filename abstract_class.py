

from abc import ABC, abstractmethod


class Storage(ABC):
    def __init__(self, capacity: int, items: dict):
        self._capacity = capacity
        self._items = items


    @abstractmethod
    def add(self, name, count):
        pass

    @abstractmethod
    def remove(self, name, count):
        pass

    @abstractmethod
    def get_free_space(self):
        pass

    @property
    def _get_items(self):
        return self._items

    @property
    def get_unique_items_count(self):
        return len(self._items)
