# 268. За даним натуральним числом n (n ≤ 9) виведіть драбинку з n сходинок як у вихідних даних, 
# n-а сходинка складається з чисел від 1 до n без пропусків.
'''
Вхідні дані:

5

Вихідні дані:

1
12
123
1234
12345

'''
n = int(input("Enter a number: "))
num_list = []
for i in range(1,n + 1):
    i=+i
    num_list.append(str(i))
    answer = ''.join(num_list)
    print(answer)