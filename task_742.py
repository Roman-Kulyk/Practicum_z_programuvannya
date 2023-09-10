# 742. Один з астрологів визначає щасливі і нещасливі дні так: він записує підряд число, номер місяця і рік. 
# В отриманому числі додає всі цифри, в новому отриманому числі знову додає всі цифри і так далі, доки чергова сума цифр 
# не стане однозначним числом. Це число і характеризує щасливість дня. Дата зберігається в форматі ррррммдд у файлі. 
# Збережіть рядок, який містить одне число, що визначає щасливість дати, у інший файл.
'''
Вхідні дані:
Файл input.txt з вмістом
20000101

Вихідні дані:
Файл output.txt з вмістом
4
'''
freading_1 = open('task_742_input.txt', 'rt' )
date = freading_1.read()
freading_1.close()

print(int(date))

num_list = []
for i in date:
    num_list.append(int(i))
    result = sum(num_list)

if result < 10:
    print(result)
else:
    result %= 10
    print(result)

freading_2 = open("task_742_output.txt",'w')
freading_2.write(str(result))
freading_2.close()