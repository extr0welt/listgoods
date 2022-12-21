import datagood

if __name__ == '__main__':
    print('Товар с максимальной ценой:', datagood.good_list.get_good_with_max_price())
    print('Товар с минимальной ценой:', datagood.good_list.get_good_with_min_price())
    print('Максимальное количество товара:', datagood.good_list.get_good_with_max_count())
    print('Минимальное количество товара:', datagood.good_list.get_good_with_min_count())
    print('Данные из get_mean_price:')
    print(datagood.good_list.get_mean_price())
