# 720. Напишіть програму для перевірки існування файла в поточному каталозі. Використайте модуль os.
'''
Вхідні дані:
my.py
input.txt

Вихідні дані:
False
True
'''
import os
print(os.path.isfile('/home/roman/Practicum_z_programuvannya/task_720.py'))
print(os.path.isfile('/home/roman/Practicum_z_programuvannya/README.md'))