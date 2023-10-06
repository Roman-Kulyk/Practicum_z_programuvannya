# 816. Напишіть клас Coin, який описує монету, яку можна підкидати. 
# При створенні екземпляру класу, екземпляр отримує атрибут __sideup зі значенням heads 
# або tails. У класі визначте метод toss, який випадково визначає результат підкидання 
# монети - орел чи решка. Створіть екземпляр класу і виведіть на екран n підкидань монети.
"""
Вхідні дані:
3

Вихідні дані:
Tails
Heads
Tails
"""
import random

class Coin():
    def __init__(self):
        self.__sideup = ['Tails', 'Heads']

    def toss(self, n ):

        for i in range(n):
            print(random.choice(self.__sideup))

coin_1 = Coin()
coin_1.toss(5)