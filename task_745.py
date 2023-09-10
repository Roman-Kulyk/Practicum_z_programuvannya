# 745. Напишіть програму для отримання списку лише файлів в поточному каталозі.
'''
Вхідні дані:
Немає

Вихідні дані:
Список файлів в поточному каталозі
'''

import os
files = os.listdir()
for file in files:
    if os.path.isfile(file):#this function is used to list all the files in the specified directory
        print(file)