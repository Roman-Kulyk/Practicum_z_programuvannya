# Створіть новий файл у текстовому редакторі і напишіть кілька рядків тексту у ньому про 
# можливості Python. Кожен рядок повинен починатися з фрази: In Python you can .... 
# Збережіть файл з ім’ям learning_python.txt. Напишіть програму, яка зчитує файл і виводить 
# текст з перебором рядків об’єкта файла і зі збереженням рядків у списку з подальшим 
# виведенням списку поза блоком with.

with open('ex_#883_3_learning_python.txt', 'rt' ) as freading:
    lines = freading.readlines()

for line in lines:
    print(line.rstrip())