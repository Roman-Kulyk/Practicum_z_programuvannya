# 747. Напишіть програму для зчитування випадкового рядка з текстового файла.
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
Java
'''
import random
freading = open('task_747_input.txt', 'r' )#it opens a file

lines = random.choice(freading.readlines())#it return a random element from the non-empty sequence

freading.close()#it closes the file
print(lines)#print line which was returned