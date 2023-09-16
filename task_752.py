#752 Напишіть програму, щоб отримати дату/час створення та зміни файла в поточному каталозі. 
# Використайте модулі os і time.
'''
Вхідні дані:
input.txt

Вихідні дані:
Last modified: Fri Jul 26 16:56:10 2019
Created: Tue Nov 13 17:05:54 2018
'''
import os
from datetime import datetime


current_directory = os.getcwd()#it assigns path to current directory

file_name = 'task_752.txt'

for file_name in os.listdir(current_directory):#for every file in current directory
    
        modification_time = os.path.getmtime(file_name)#it gets date of last file modification
        modification_time = datetime.fromtimestamp(modification_time)
        
        creation_file_time =os.path.getctime(file_name)
        creation_file_time = datetime.fromtimestamp(creation_file_time)

print("Last modified: ", modification_time)
print("Created: ",creation_file_time)