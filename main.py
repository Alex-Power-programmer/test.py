from helpers import load, welcome, from_store_in_shop, check_request, get_store_request
from request_class import Request
from shop_class import Shop
from store_class import Store


def main():
    flag = True
    list_store = [{"магазин": Shop}, {"склад": Store}]
    list_stop = ['stop', 'exit', 'end']
    while flag:

        line = welcome()
        if line in list_stop:
            flag = False
            print('конец, я устал')
            break

        request = Request(list_store, line)

        count = request.amount
        product = request.product

        if not check_request(line):
            store = request.to(items=load('store'))
            store.add(product, count)
            get_store_request(product, count)

        else:
            store = request.from_(items=load('store'))
            shop = request.to(items=load('shop'))

            storer = store.remove(product, count)
            shoper = shop.add(product, count)

            from_store_in_shop(shoper, storer, count, product)


if __name__ == '__main__':
    main()
