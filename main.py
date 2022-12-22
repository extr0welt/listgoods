import datagood

with open('list_goods.txt', 'r', encoding='utf-8') as file:
    list_with_goods = file.readlines()

    for str_good in list_with_goods:
        list_good = str_good.split(':')
        name = list_good[0]
        price = list_good[1]
        count = list_good[2]
        production_date = list_good[3]
        expiration_day = list_good[4]
        datagood.good_list.add_good_in_list(datagood.Good(name, price, count, production_date, expiration_day))

if __name__ == '__main__':
    print('Товар с максимальной ценой:', datagood.good_list.get_good_with_max_price())
    print('Товар с минимальной ценой:', datagood.good_list.get_good_with_min_price())
    print('Максимальное количество товара:', datagood.good_list.get_good_with_max_count())
    print('Минимальное количество товара:', datagood.good_list.get_good_with_min_count())
    print('Данные из get_mean_price:')
    print(datagood.good_list.get_mean_price())
