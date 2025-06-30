from request_class import Request
from shop_class import Shop
from store_class import Store

dict_a = {"cat": 100}

def main():
    flag = True
    while flag:
        list_store = [Store, Shop]
        print('Привет давай работать!')
        line = input()
        request = Request(list_store, line)
        count = request._amount
        print(count)
        print(request._from)
        print(request._to)
        print(request._product)
        shop = Shop(items=dict_a)
        places = shop.get_free_space()
        print(places)
        if places > 0:
            print('dk')

if __name__ == '__main__':
    main()