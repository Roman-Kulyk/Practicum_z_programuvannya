# 466. Дано список цілих чисел, число k і значення c. Необхідно вставити у список 
# на позицію з індексом k елемент, рівний c, зсунувши всі елементи вправо. Вставку 
# необхідно здійснювати у самому списку, не роблячи цього при виведенні і не створюючи 
# додаткового списку. Вводиться список чисел. Всі числа списку знаходяться на одному 
# рядку. У наступному рядку вводяться два цілих числа.
'''
Вхідні дані:
9 4 6 2 0 7 14
3 0

Вихідні дані:
9 4 6 0 2 0 7 14
'''
lst_1 = input("Enter the list members: ").split()
lst_2 = [int(item) for item in input("Enter the list members: ").split()]
k = lst_2[0]
c = lst_2[-1]
lst_1.insert(k, c) 


for i in lst_1:
    print(i,end = ' ')
print()