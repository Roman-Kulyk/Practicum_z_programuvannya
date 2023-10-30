# 489. Вводяться n рядків. Визначити найдовший рядок і вивести його номер на екран. 
# Якщо найдовших рядків кілька, то вивести номери всіх таких рядків.
"""
Вхідні дані:
5
Thames
Amazon
Nile
Yangtze
Dnieper

Вихідні дані:
4
5
"""
number_of_row = int(input("Enter your number: "))
output_list = []
for i in range(number_of_row):
    
    text = input('Enter your row: ')
    output_list.append(text)
#print(max(output_list))
max_len_list = []
for i in output_list:
    if len(i) == len(max(output_list)):
        max_len_list.append(i)
        #print(max_len_list)
        #print(i)
        print(int(output_list.index(i)) +1)
