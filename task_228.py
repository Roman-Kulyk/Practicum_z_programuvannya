# 228. Напишіть програму для обчислення виразу 1/2 + 2/3 + 3/4 + …​ + n/(n + 1) із заданим n, 
# яке вводить користувач (n > 0).


n = int(input("Enter a number: "))
num_list = []
for i in range(1,n):
    mul = i /(i + 1)
    num_list.append(mul)
print(num_list)