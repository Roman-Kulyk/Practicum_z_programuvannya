#103.Користувачем вводиться два імені. Використовуючи конструкцію розгалуження програма повинна вивести імена в 
#алфавітному порядку.

name_1 = input('Enter a first name: ')
name_2 = input('Enter a second namd: ')
alphabet = 'abcdefghijklmnopqrstuvwxyz'
if name_1[0] < name_2[0]:
    print(name_1, name_2)
else:
    print(name_2, name_1)
    