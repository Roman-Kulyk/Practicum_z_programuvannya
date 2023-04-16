# 233. Дано n цілих чисел. Кожне число вводиться в окремому рядку. Обчисліть суму чисел.


n = int(input("Enter a number: "))
num_list = []
for i in range(0, n):
    n_1 = int(input("Enter a number: "))
    num_list.append(n_1)
    
print(sum(num_list))
