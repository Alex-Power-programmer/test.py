from helpers import check_request


class Request:
    def __init__(self, list_store: list, line: str):

        if check_request(line):
            self._from = list_store[1][line.split(' ')[-3]]
            self._to = list_store[0][line.split(' ')[-1]]
            self._amount = int(line.split(' ')[-6])
            self._product = line.split(' ')[-5]

        else:
            self._from = None
            self._to = list_store[1][line.split(' ')[-1]]
            self._amount = int(line.split(' ')[1])
            self._product = line.split(' ')[2]

    @property
    def product(self):
        return self._product

    @property
    def amount(self):
        return self._amount

    @property
    def from_(self):
        return self._from

    @property
    def to(self):
        return self._to


# string = "Доставить 3 печеньки из склад в магазин"
# list_store = [{"магазин": Shop}, {"склад": Store}]
# b = Request(['Store', 'Shop'], string)
#
# print(b)