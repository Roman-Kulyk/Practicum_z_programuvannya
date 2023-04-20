# 259. Дано цілі числа a і b. Знайти їх добуток, не використовуючи операцію множення.
'''
Вхідні дані:

7
3

Вихідні дані:

21
'''

a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
num_list=[]
for i in range(0,b):
    num_list.append(a)
print(sum(num_list))