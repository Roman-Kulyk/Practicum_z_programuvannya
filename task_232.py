# 232. Дано n чисел. Визначте, скільки з них дорівнюють нулю, і виведіть цю кількість. 
# Спочатку вводиться число n, потім вводиться рівно n цілих чисел.
 

n = int(input("Enter a number: "))
num_list = []
for i in range(0, n):
    n_1 = int(input("Enter a number: "))
    num_list.append(n_1)
print(num_list.count(0))

'''
n = int(input("Enter a number: "))
num_list = []
for i in range(1,n):
    mul = i ** 2
    num_list.append(mul)
print(num_list)
'''