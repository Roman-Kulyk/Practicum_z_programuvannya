# 285. Послідовність складається з різних натуральних чисел і завершується числом 0.
# Визначте значення другого за величиною елемента в цій послідовності. 
# Вводиться послідовність цілих чисел, що закінчується числом 0 
# (саме число 0 в послідовність не входить, а використовується як ознака її закінчення). 
# Гарантується, що в послідовності є хоча б два елементи.
'''
Вхідні дані:

1
4
3
2
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
        
            
print(num_list[2])#it prints second element in the sequence