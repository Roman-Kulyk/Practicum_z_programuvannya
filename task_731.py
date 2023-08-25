# 731. Напишіть програму для зчитування файла рядок за рядком та зберігання рядків у списку.
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
['Python\n', 'Ruby\n', 'C++\n', 'C\n', 'Java\n', 'GO']
'''
freading = open('task_731_input.txt', 'rt' )
lines = freading.readlines()
freading.close()

print(lines)
