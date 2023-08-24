# 718. Напишіть програму python, щоб отримати шлях і ім’я файла, який наразі виконується. 
# Використайте модуль os.
'''
Вхідні дані:
Немає

Вихідні дані:
C:\Python36\wc.py
'''
import os

file_path = os.path.realpath(__file__)

print(file_path)