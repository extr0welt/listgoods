from datetime import datetime
from datetime import timedelta
from exception import EndingExpirationDate


class Good:
    '''Класс товара'''

    def __init__(self, name, price, count, production_date, expiration_day):
        self.name = name
        self.price = price
        self.count = count
        self.production_date = datetime.strptime(production_date, '%Y-%m-%d')
        self.expiration_day = expiration_day



    def __str__(self):
        return f'{self.name}'



    def check_expiration_date(self):
        '''Проверка срока годности товара'''

        date_now = datetime.now()
        date_ending_expiration = self.production_date + timedelta(days=int(self.expiration_day))

        if date_ending_expiration > date_now:
            return True
        else:
            raise EndingExpirationDate


class GoodList:
    '''Класс со списком товаров'''

    def __init__(self):
        self.good_list = []



    def add_good_in_list(self, good: Good):
        '''Добавляем товар в список'''

        try:
            good.check_expiration_date()
            self.good_list.append(good)
        except EndingExpirationDate:
            print(f"Товар {good} с истекшим сроком годности")
            return None



    def remove_good_from_list(self, name: str):
        '''Удаляем товар из списка по имени (первый найденный)'''

        for index, good in enumerate(self.good_list):
            if good.name == name:
                del self.good_list[index]
                break



    def clear_by_expiration_date(self):
        '''Очищает по сроку годности'''

        for good in self.good_list:
            try:
                good.check_expiration_date()
            except EndingExpirationDate:
                self.remove_good_from_list(good.name)



    def get_mean_price(self):
        '''Получаем среднюю цену товаров'''

        sum_price = 0
        sum_count = 0

        for good in self.good_list:
            sum_price += int(good.price)
            sum_count += int(good.count)

        print(f'sum goods = {sum_price}')
        print(f'sum count = {sum_count}')
        mean = 0

        if sum_count != 0:
            mean = sum_price / sum_count
        return mean


    def get_good_with_max_price(self):
        '''Получаем товар с максимальной ценой'''

        name = ''
        max_price = 0

        for good in self.good_list:
            if int(good.price) > int(max_price):
                max_price = good.price
                name = good.name
        return name




    def get_good_with_min_price(self):
        '''Получаем товар с минимальной ценой'''

        name = ''
        min_price = 10000

        for good in self.good_list:
            if int(good.price) < min_price:
                min_price = int(good.price)
                name = good.name
        return name



    def get_good_with_max_count(self):
        '''Получаем товар с максимальным количеством'''

        name = ''
        max_count = 0

        for good in self.good_list:
            if int(good.count) > int(max_count):
                max_count = good.count
                name = good.name
        return name


    def get_good_with_min_count(self):
        '''Получаем товар с минимальным количеством'''

        name = ''
        min_count = 10000

        for good in self.good_list:
            if int(good.count) < int(min_count):
                min_count = good.count
                name = good.name
        return name

good_list = GoodList()

with open('list_goods.txt', 'r', encoding='utf-8') as file:
    list_with_goods = file.readlines()

    for str_good in list_with_goods:
        list_good = str_good.split(':')
        name = list_good[0]
        price = list_good[1]
        count = list_good[2]
        production_date = list_good[3]
        expiration_day = list_good[4]
        good_list.add_good_in_list(Good(name, price, count, production_date, expiration_day))


good_list.get_mean_price()
