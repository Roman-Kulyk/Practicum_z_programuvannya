# 226. Знайти суму 1**2 + 2**2 + 3**2 + …​ + n**2 при заданому користувачем значенні цілого числа n.


n = int(input("Enter a number: "))
num_list = []
for i in range(1,n):
    mul = i ** 2
    num_list.append(mul)
print(num_list)

     