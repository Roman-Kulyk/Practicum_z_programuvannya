# 283. Послідовність складається з цілих чисел і закінчується номером 0. 
# Визначте, скільки елементів цієї послідовності більше наступного елемента. 
# Вводиться послідовність цілих чисел, що закінчується числом 0 (саме число 0 
# в послідовність не входить, а використовується як ознака її закінчення). 
# Гарантується, що послідовність містить як мінімум два числа.
'''
Вхідні дані:

2
9
1
4
3
0

Вихідні дані:

2

'''
count = 0     
prev = int(input("Enter a number: "))#it reads first element of sequence
while True:
    curr = int(input("Enter a number: "))#it reads others elements of sequence
    if curr == 0:#it checks if element not equal to zero
        break
    if curr < prev:#it cheks if current element less than the previous one
        count+=1
    prev = curr#it assign current value to prev variable
print(count)#it prints quantity of needed elements