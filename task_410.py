# 410. Виведіть елементи даного списку в зворотному порядку, не змінюючи сам список.
'''
Вхідні дані:
2 6 1 7 9

Вихідні дані:
9 7 1 6 2
'''
list = [2,6,1,7,9]
x = sorted(list,reverse=True)
print(x)
print(list)