


class Request:
    def __init__(self, list_store: list, line: str):
        self._from = line.split(' ')[-3]
        self._to = line.split(' ')[-1]
        self._amount = line.split(' ')[-6]
        self._product = line.split(' ')[-5]


# string = "Доставить 3 печеньки из склад в магазин"
# b = Request(['Store', 'Shop'], string)
#
# print(b)