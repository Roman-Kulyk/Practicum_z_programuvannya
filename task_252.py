# 252. Визначте кількість парних елементів в послідовності, яка завершується числом 0. 
# Вводиться послідовність цілих чисел, що закінчується числом 0 (саме число 0 в послідовність не входить,
# а використвоується як ознака її закінчення).

'''
Вхідні дані:

3
6
9
8
0

Вихідні дані:

2
'''
num_list = []
while True:
    n = int(input("Enter a number: "))
    if n != 0 and n % 2 ==0:
        num_list.append(n)
    elif n == 0:
        break
print(len(num_list))