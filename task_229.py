# 229. Визначити суму всіх трицифрових чисел, які діляться націло на n, 
# де n - ціле число, яке вводить користувач.

n = int(input("Enter a number: "))
num_list = []
for i in range(100,1000):
    if i % n == 0:
        num_list.append(i)
print(sum(num_list))
