# 535. Напишіть програму для видалення дублікатів зі списку цілих чисел.
'''
Вхідні дані:
10 5 11 2 3 5 8 9 3 4 2

Вихідні дані:
2 3 4 5 8 9 10 11
'''
data = input("Enter the q-ty through the spacebar:").split()

data_set = set(data)

for i in data_set:
    print(i,end = ' ')
print()
