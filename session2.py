# -*- coding: utf-8 -*-
"""
Created on 02.11.2024

@author: dmitry
"""

import datetime as dt


class Store:
    """«магазин в общем»"""
    def __init__(self, address):
        self.address = address

    def is_open(self, date):
        """Заглушка"""
        # Метод is_open() в родительском классе всегда возвращает False, 
        # это "код-заглушка", метод, предназначенный для переопределения
        # в дочерних классах.
        return False

    def get_info(self, date_str):
        # С помощью шаблона даты преобразуйте строку date_str в объект даты:
        """Работает ли конкретный магазин в указанный день"""
        date_object = dt.datetime.strptime(date_str, '%d.%m.%Y')
        
        # Передайте в метод is_open() объект даты date_object и определите,
        # работает ли магазин в указанную дату. 
        # В зависимости от результата будет выбрано значение
        # для переменной info.
        if self.is_open(date_object) is True:
            info = 'работает'
        else:
            info = 'не работает'
        return f'Магазин по адресу {self.address} {date_str} {info}'


class MiniStore(Store):
    # Переопределите метод is_open().
    """По субботам минимаркеты не работают"""
    def is_open(self, date):
        """Переопределение"""
        return date.weekday() not in (5, 6)  # 5 соответствует субботе


class WeekendStore(Store):
    # Переопределите метод is_open().
    """работают по субботам и воскресеньям"""
    def is_open(self, date):
        """Переопределение"""
        return date.weekday() in (5, 6)  # 5, 6 соответствуют выходным


class NonStopStore(Store):
    # Переопределите метод is_open().
    """работают вообще всегда, в любой день"""
    def is_open(self, date):
        """Преопределение"""
        return date.weekday() in (0, 1, 2, 3, 4, 5, 6)  # В любой день


mini_store = MiniStore('Улица Немига, 57')
print(mini_store.get_info('29.03.2024'))
print(mini_store.get_info('30.03.2024'))

weekend_store = WeekendStore('Улица Толе би, 321')
print(weekend_store.get_info('29.03.2024'))
print(weekend_store.get_info('30.03.2024'))

non_stop_store = NonStopStore('Улица Арбат, 60')
print(non_stop_store.get_info('29.03.2024'))
print(non_stop_store.get_info('30.03.2024'))