# 502. Напишіть програму, яка знайде максимально можливе число, яке можна отримати після 
# видалення однієї цифри. Перший рядок містить одне ціле число n (10 ≤ n ≤ 2025). Виведіть 
# у другому рядку максимально можливе число, яке можна отримати після видалення однієї цифри.
"""
Вхідні дані:
4378
1095
2000

Вихідні дані:
478
195
200
"""
numbers = input("Enter your numbers: ")
list_numbers = list(numbers)#it initialize list

min_num = min(list_numbers)#it finds minimum element within the list
list_numbers.remove(min_num)#and deletes it

list_numbers = ("".join(list_numbers))#it joins remaining elements from list into a string
print(list_numbers)#it print string

