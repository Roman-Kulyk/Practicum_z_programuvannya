# 711. Напишіть програму, щоб отримати назву, платформу та інформацію про випуск операційної системи. Використайте 
# імпорт модулів platform і os.
'''
Вхідні дані:
Немає

Вихідні дані:
nt
Windows
10
'''
import os
import platform
print(os.name)
print(platform.system())
print(platform.version())