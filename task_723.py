# 723. Напишіть програму для друку характеристик числових типів Python. Використайте модуль os.
'''
Вхідні дані:
Немає

Вихідні дані:
Значення числових типів
'''
import os
def print_numeric_type_info(value):
    print(f"Value: {value}")
    print(f"Type of data: {type(value).__name__}")
    #print(f"Size in bytes: {os.path.getsize(value)}")
    print(f"min value:{min_value}")
    print(f"max value:{max_value}")
    print("")

int_value = 42
float_value = 3.14
complex_value = 2 + 3j

min_value = -float('inf')
max_value = float('inf')

print_numeric_type_info(int_value)
print_numeric_type_info(float_value)
print_numeric_type_info(complex_value)
