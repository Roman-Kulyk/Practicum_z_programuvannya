# 491. Користувач вводить ціле число n і видаляє одну цифру числа так, щоб число що 
# утворилось, було максимально можливим. Наприклад, якщо число, яке ввели 432, то необхідно 
# видалити цифру 2, яка стоїть на 3 місці, щоб отримати максимально можливе число 43. 
# Напишіть програму, яка знайде максимально можливе число, яке можна отримати після 
# видалення однієї цифри.
"""
Вхідні дані:
432
239
101

Вихідні дані:
43
39
11
"""
input_numbers = input("Enter your list: ")
#print(input_numbers)
list_numbers = []#it initializes empty list 
for i in input_numbers:#and for every i in input_numbers string
    i = int(i)#converts it to integer
    list_numbers.append(i)#and adds it to the list

#print(list_numbers)
list_numbers.remove(min(list_numbers))#it removes minimal value from the list

result = ''#it initializes an empty string result
for i in list_numbers:#and for every i in list_numbers
    result += str(i)#adds it to the result string
print(result)#and prints result