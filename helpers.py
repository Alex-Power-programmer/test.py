import json
import time
from time import sleep


def write(s, lines):
    with open(f'{s}.json', 'w', encoding='utf-8') as file:
        json.dump(lines, file, ensure_ascii=False, indent=4)


def load(s):
    with open(f'{s}.json', 'r', encoding='utf-8') as file:
        return json.load(file)


def welcome():
    print()
    print(' --- --- --- ---')
    print()
    line = input()
    while line == '':
        line = input()

    return line


def from_store_in_shop(shoper, storer, count, product):
    if shoper is not None:
        print(shoper)
    if storer is not None:
        print(storer)

    if shoper is None and storer is None:
        print(f'Нужное количество есть на складе')
        time.sleep(2.2)
        print(f'Курьер забрал {count} {product} со склад')
        time.sleep(2.1)
        print(f"Курьер везет {count} {product} со склад в магазин")
        time.sleep(2)
        print(f"Курьер доставил {count} {product} в магазин")


def check_request(line):
    if len(line.split(' ')) >= 6:
        return True

    elif len(line.split(' ')) == 5:
        return False


def get_store_request(product, count):

    print(f'Лимит не превышен, есть место на складе')
    time.sleep(2.2)
    print(f"Курьер везет {count} {product} в склад")
    time.sleep(2)
    print(f"Курьер доставил {count} {product} в склад")
