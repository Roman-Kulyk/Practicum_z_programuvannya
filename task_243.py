# 243. Дано n чисел. Перше число на вході n, після чого задано n цілих чисел. 
# Необхідно порахувати кількість нулів серед введених користувачем чисел.

n = int(input("Enter a number: "))
num_list=[]
for i in range(0,n):
    num = int(input("Enter a number: "))
    num_list.append(num)
print(num_list.count(0))
