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
                 
count = 0     
prev = int(input())#it reads first element of sequence
while True:
    curr = int(input())#it reads others elements of sequence
    if curr == 0:#it checks if element not equal to zero
        break
    if curr > prev:#it cheks if current element bigger than the previous one
        count+=1 #it add to count variable if previous is true
    prev = curr #it assign current value to prev variable
print(count) #it prints quantity of needed elements