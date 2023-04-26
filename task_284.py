# 284. Послідовність складається з натуральних чисел і завершується числом 0. 
# Визначте, скільки елементів цієї послідовності рівні її найбільшому елементу. 
# Вводиться послідовність цілих чисел, що закінчується числом 0 (саме число 0 в 
# послідовність не входить, а використовується як ознака її закінчення).
'''
Вхідні дані:

3
8
10
2
10
7
0

Вихідні дані:

2

'''
num_list = []     
while True:
    curr = int(input("Enter a number: "))#it reads elements of sequence
    if curr == 0:#it checks if element not equal to zero
        break
    else:
        num_list.append(curr)# it adds element to the sequence
        max_num =max(num_list)#it founds the biggest elements of the sequence
            
print(num_list.count(max_num))#it prints quantity of needed elements