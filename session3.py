# -*- coding: utf-8 -*-
"""
Created on 02.11.2024

@author: dmitry
"""


class Customer:
    """Покупатель"""
    def __init__(self, name):
        self.name = name
        # Добавьте сюда атрибут "скидка" со значением по умолчанию 10.
        self.__discount = 10  # Создание приватного аттрибута - скидки

    # Реализуйте методы get_price() и set_discount().
    def get_price(self, original_price):
        """Рачсёт цены со скидкой"""
        discount_price = original_price - (original_price * self.__discount) / 100
        return round(discount_price, 2)

    def set_discount(self, new_discount):
        """Принимает на вход новое значение скидки"""
        if 0 <= new_discount <= 80:
            self.__discount = new_discount
        elif new_discount > 80:
            self.__discount = 80

    def __str__(self):
        """Более информативный вывод"""
        return f'{self.name} - обьект класса Customer'


# Проверим работу программы:
customer = Customer('Иван Иванович')
original_price = 85
print(
    f'С исходной скидкой Иван Иванович заплатит '
    f'{customer.get_price(original_price)} рублей вместо {original_price}'
)
# Изменим скидку до неприемлемого уровня.
# Метод set_discount() должен уменьшить размер скидки до 80%.
customer.set_discount(90)
print(
    f'С новой скидкой Иван Иванович заплатит '
    f'{customer.get_price(original_price)} рублей вместо {original_price}'
)