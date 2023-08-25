# 735. Запишіть рядки вхідного файла в зворотному порядку у інший файл. 
# Останній рядок вхідного файлу обов’язково закінчується символом \n.
'''
Файл input.txt з вмістом
Python
Java
C++
C
Ruby

Вихідні дані:

Файл output.txt з вмістом
Ruby
C
C++
Java
Python
'''

freading = open('task_735_input.txt', 'rt' )
lines = freading.readlines()#it returns a list of lines which were red
freading.close()
print(lines)

freading_2 = open('task_735_output.txt','wt')

for line in lines[::-1]:#in reverse order we
    lines = freading_2.write(str(line))#write the list in output file

freading_2.close()