# 286. Послідовність складається з натуральних чисел і завершується числом 0. 
# Визначте індекс найбільшого елемента послідовності. 
# Якщо найбільших елементів декілька, виведіть індекс першого з них. 
# Нумерація елементів починається з нуля. 
# Вводиться послідовність цілих чисел, що закінчується числом 0 
# (саме число 0 в послідовність не входить, а використовується як ознака її закінчення).
'''
Вхідні дані:

4
2
6
9
5
0

Вихідні дані:

3

'''
num_list = []  
while True:
    curr = int(input("Enter a number: "))#it reads elements of sequence
    if curr == 0:#it checks if element not equal to zero
        break
    else:
        num_list.append(curr)# it adds element to the sequence
        max_num = max(num_list)#it founds the biggest elements of the sequence
        max_index = num_list.index(max_num)#it founds an index of the bigges sequence's element
            
print(max_index)#it prints quantity of needed elements