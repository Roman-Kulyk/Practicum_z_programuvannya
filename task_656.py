# 656. Вкладник розмістив суму розміром n грн. в банку. Визначте, яку суму отримає 
# вкладник через m років, якщо відсоткова ставка складає p% в рік. Дані вводяться в 
# порядку n, p, m як у вхідних даних.
'''
Вхідні дані:
5000
18
2

Вихідні дані:
6800.00
'''
def revenue_func():
    n = int(input("Enter your amout: "))
    p = int(input("Enter percentage: "))
    m = int(input('Enter years: '))
    revenue = n + (n * p / 100) * m
    print(revenue)

revenue_func()