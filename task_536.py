# 536. Даний список цілих чисел. Визначте кількість різних значень.
'''
Вхідні дані:
1 3 4 5 6 5 1 9

Вихідні дані:
6
'''
data = input("Enter the q-ty through the spacebar:").split()

data_set = set(data)

print(len(data_set))