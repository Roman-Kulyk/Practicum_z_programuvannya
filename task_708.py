# 708. Напишіть програму, щоб отримати версію Python, яку ви використовуєте: рядок, що містить номер версії 
# інтерпретатора Python плюс додаткову інформацію про номер збірки та використаний компілятор. Цей рядок відображається 
# під час запуску інтерактивного інтерпретатора. Використайте модуль sys.
'''
Вхідні дані:
Немає

Вихідні дані:
3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 17:00:18) [MSC v.1900 64 bit (AMD64)]
'''
import sys
print(sys.executable)
print(sys.version)