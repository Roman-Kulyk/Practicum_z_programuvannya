# 446. Дано список чисел, підрахуйте, скільки пар елементів мають однакове значення 
# (рівні). Будь-які два елементи, що дорівнюють один одному, 
# слід вважати рівно один раз.
'''
Вхідні дані:
1 2 2 2 3 3 4
4 5 5 8 10 12 3 3
1 5 2 8 9 5

Вихідні дані:
4
2
1
'''
lst = []
lst = [int(item) for item in input("Enter the list members: ").split()]
pair_count = 0
for i in range(len(lst)):
    for j in range(i + 1,len(lst)):
        if lst[i] == lst[j]:
            pair_count += 1
            break
print(pair_count)