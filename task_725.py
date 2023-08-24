# 725. Напишіть програму, щоб надрукувати на екрані вміст вказаного файла, розміщеного в поточному каталозі.
'''
Вхідні дані:
Файл input.txt з вмістом
Python
Ruby
C++
C
Java

Вихідні дані:
Python
Ruby
C++
C
Java
'''
file_name = input('Enter file name: ')
try:
    with open(file_name,'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print('File not found!')
except Exception as e:
    print('Fault: ',e )

