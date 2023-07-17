# 639. Напишіть функцію, яка об’єднує всі елементи послідовності, 
# введені через пропуск, в рядок, де елементи вже розділені комою і одним пропуском, 
# і повертає його як у вихідних даних.
'''
Вхідні дані:
Python Ruby C Go Java JavaScript

Вихідні дані:
Python, Ruby, C, Go, Java, JavaScript
'''
def list_function():
    lst = input("Enter the list members: ").split()
    lst = ', '.join(lst)
    print(lst)

list_function()