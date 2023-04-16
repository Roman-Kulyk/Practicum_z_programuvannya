# 227. При заданому користувачем значенні цілого числа n ≥ 2 обчислити вираз 1 × 2 + 2 × 3 + …​ + (n - 1) × n.


n = int(input("Enter a number: "))
num_list = []
for i in range(1,n):
    mul = i *(i + 1)
    num_list.append(mul)
print(sum(num_list))
