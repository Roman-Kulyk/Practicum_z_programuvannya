# 478. Напишіть програму, яка обчислює суму на банківському рахунку на основі 
# журналу транзакцій. Формат журналу транзакцій відображається наступним чином:
# D 100
# W 200

# де D – покласти на депозит ціле значення суми, а W - вилучити. 
# Введення транзакцій завершується порожнім рядком.
'''
Вхідні дані:
D 100
W 200
D 300
D 350
W 200
D 150
 
Вихідні дані:
500
'''
count = 0
while True:
    lst = input("Enter the list members: ").split()
    if lst == []:
        break
    else:
        if lst[0] == 'D':
            count += int(lst[1])
        elif lst[0] == 'W':
            count -= int(lst[1])
print(count)
