# 545. Створіть словник, який відображає ідентифікатори акцій на біржі. Ключами 
# словника є ідентифікатори акцій, а значеннями - дійсні числа - ціни акцій. 
# Надрукуйте ціни акцій для мінімального і максимального значення ціни відповідно та 
# їх ідентифікатори.
'''
Вхідні дані:
Немає

Вихідні дані:
10.75 FB
612.78 AAPL
'''
dictionary ={
    'FB':10.75,
    'HPQ':37.2, 
    'ACME':45.23, 
    'IBM':205.55, 
    'AAPL':612.78
    }
minimum = dictionary.values()
a = (min(list(minimum)))
b = (max(list(minimum)))

for key,value in dictionary.items():
    if value == a or value == b:
        print(key,value, sep =" ")
