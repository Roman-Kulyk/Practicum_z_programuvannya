# 736. Запишіть увесь вміст вхідного файла в зворотному порядку у інший файл. 
# Останній рядок вхідного файлу обов’язково закінчується символом \n.
'''
Вхідні дані:
Файл input.txt з вмістом
Python
Java
C++
C
Ruby

Вихідні дані:
Файл output.txt з вмістом
ybuR
C
++C
avaJ
nohtyP
'''
freading = open('task_736_input.txt', 'rt' )
lines = freading.readlines()#it returns a list of lines which were red
freading.close()
print(lines)

freading_2 = open('task_736_output.txt','wt')

for line in lines[::-1]:#in reverse order we
    lines = freading_2.write(str(line[::-1]))#write the list in output file

freading_2.close()
