# 247.Дано ціле число n, яке вводить користувач. Необхідно обчислити значення виразу 1! +2! +3! + …​ + n!.


n = int(input("Enter a number: "))
num_list = []
result = 1
for i in range(1,n+1):
    
    result = result * i
    num_list.append(result)
print(sum(num_list))




