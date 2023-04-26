# 282. Послідовність складається з натуральних чисел і завершується числом 0. 
# Визначте, скільки елементів цієї послідовності більше попереднього елемента. 
# Вводиться послідовність цілих чисел, що закінчується числом 0 
# (саме число 0 в послідовність не входить, 
# а використовується як ознака її закінчення).
'''
Вхідні дані:

4
3
6
8
0

Вихідні дані:

2

'''
'''
num_list = []
previous_les =[]
while True:
    n = int(input("Enter a number: "))
    if n == 0:
        break
    else:
         for i in num_list:
             if num_list[i]>num_list[i-1]:
                previous_les.append[i]
                print(len(previous_les))
  '''          
                 
count = 0
prev = int(input())
while True:
    curr = int(input())
    if curr == 0:
        break
    if curr > prev:
        count+=1
    prev = curr
print(count)