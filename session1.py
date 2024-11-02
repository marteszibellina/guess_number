# -*- coding: utf-8 -*-
"""
Created on --date--

@author: dmitry
"""


class Product:
    """Базовый класс"""
    # Опишите инициализатор класса и метод get_info()
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

    def get_info(self):
        """<название товара> (в наличии: <число>)"""
        return f'{self.name} (в наличии: {self.quantity})'

    def __str__(self):
        """Более информативный вывод"""
        return f'{self.name} - обьект класса Product'


class Kettlebell(Product):
    # Опишите инициализитор класса и метод get_weight()
    """Класс для весовых товаров"""
    def __init__(self, name, quantity, weight):
        super().__init__(name, quantity)
        self.weight = weight

    def get_weight(self):
        """<название товара> (в наличии: <число>). Вес: <число> кг"""
        return f'{self.name} (в наличии: {self.quantity}). Вес: {self.weight} кг'


class Clothing(Product):
    # Опишите инициализатор класса и метод get_size()
    """Класс для товаров с размером"""
    def __init__(self, name, quantity, size):
        super().__init__(name, quantity)
        self.size = size

    def get_size(self):
        """<название товара> (в наличии: <число>). Размер: <размер>"""
        return f'{self.name} (в наличии: {self.quantity}). Размер: {self.size}'

# Для проверки вашего кода создадим пару объектов
# и вызовем их методы:

KETTELBELL_1 = Product('Гиря-1', 10)
print(KETTELBELL_1.get_info())

small_kettlebell = Kettlebell('Гиря малая', 15, 2)
shirt = Clothing('Футболка', 5, 'L')

print(small_kettlebell.get_weight())
print(shirt.get_size())