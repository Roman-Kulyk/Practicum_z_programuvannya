# 726. Напишіть програму для підрахунку кількості кожного символу у текстовому файлі без врахування регістру літер, 
# використавши модуль collections. Для гарного друку використайте модуль pprint.
'''
Вхідні дані:
task_726_input.txt

Вихідні дані:
Counter({'\n': 4,
         'y': 2,
         'c': 2,
         '+': 2,
         'a': 2,
         'p': 1,
         't': 1,
         'h': 1,
         'o': 1,
         'n': 1,
         'r': 1,
         'u': 1,
         'b': 1,
         'j': 1,
         'v': 1})
'''
import collections
#import pprint
file_name = '/home/roman/Practicum_z_programuvannya/task_726_input.txt'
with open(file_name,'r', encoding='utf-8') as file:
    content = file.read()
content = content.lower()
collections.Counter
counter = collections.Counter(content)
for char,count in counter.items():
    print(f'{char}:{count}')