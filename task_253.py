# 253. Послідовність складається з натуральних чисел і завершується числом 0. Визначте значення 
# найбільшого елемента послідовності. Вводиться послідовність цілих чисел, що закінчується числом 0 
# (саме число 0 в послідовність не входить, а використовується як ознака її закінчення).
'''
Вхідні дані:

5
3
8
0

Вихідні дані:

8
'''




num_list = []
while True:
    n = int(input("Enter a number: "))
    if n != 0:
        num_list.append(n)
    elif n == 0:
        break
print(max(num_list))