# 331. Вводиться додатне ціле трицифрове число. Знайти суму цифр числа. 
# Операціями ділення націло і остача від ділення користуватися не можна.
'''
Вхідні дані:

179

Вихідні дані:

17

'''
num = input("Enter a number: ")
str_list = list(num)#it turns str into a list
num_list = []#it initialize new empty numbers list
for i in str_list:
    i = int(i)#it turns str into int types
    num_list.append(i)#it add numbers to list
print(sum(num_list))#it prints sum of all numbers of list