# 422.Напишіть програму, яка отримує повне ім’я файлу від користувача та друкує 
# на екрані розширення отриманого файлу.
'''
Вхідні дані:
test.cpp

Вихідні дані:
cpp
'''
lst = list(input("Enter the list members: ").split("."))
print(lst[-1])