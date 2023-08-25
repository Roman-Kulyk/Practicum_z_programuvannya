# 732. Напишіть програму для підрахунку кількості рядків у текстовому файлі.
'''
Вхідні дані:
Файл input.txt з вмістом
Python
Ruby
C++
C
Java
GO

Вихідні дані:
6
'''
freading = open('task_731_input.txt', 'rt' )
lines = freading.readlines()
freading.close()
print(len(lines))
