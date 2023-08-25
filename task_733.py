# 733. У вхідному файлі записана один текстовий рядок, який може містити пропуски. 
#Запишіть цей рядок в зворотному порядку у інший файл.
'''
Вхідні дані:
Файл input.txt з вмістом
hello world

Вихідні дані:
Файл output.txt з вмістом
dlrow olleh
'''

freading = open('task_733_input.txt', 'rt' )
lines = freading.readlines()
freading.close()

for line in lines:
    print(line[::-1].rstrip())