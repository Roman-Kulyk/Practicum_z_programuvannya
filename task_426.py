# 426. Вводиться дробове число. Надрукувати окремо цифри цілої частини і дробової. 
# Розділювачем є десяткова крапка.
'''
Вхідні дані:
12.567
0.75

Вихідні дані:
12 567
0 75
'''
lst = []
lst =[(item) for item in input("Enter the list members: ").split(".")]
print(lst[0], lst[-1])