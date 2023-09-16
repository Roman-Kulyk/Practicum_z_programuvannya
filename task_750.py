# 750.Напишіть програму для сортування файлів певного типу за датою в поточному каталозі.
# Тип файла вводиться у форматі як у вхідних даних.
'''
Вхідні дані:
*.py

Вихідні дані:
exercises.py
namespace.py
some_module.py
1234.py
locales_print.py
bottle.py
'''
import os
from datetime import datetime


current_directory = os.getcwd()#it assigns path to current directory
file_extension = ".txt" #it assigns file extension
files = []#it creates an empty list 

for file_name in os.listdir(current_directory):#for every file in current directory
    if file_name.endswith(file_extension):#with corresponding extension
        modification_time = os.path.getmtime(file_name)#it gets date of last file modification
        modification_time = datetime.fromtimestamp(modification_time)
        files.append((file_name, modification_time))#it appends file_name and modification_time to the list

files.sort(key = lambda x: x[1])#it sorts files by date
for file_info in files:#it prints files from list
    print(file_info[0], file_info[1])
