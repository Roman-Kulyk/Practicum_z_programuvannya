# 246. За даним цілим додатнім числом n обчисліть n! - значення факторіалу цього числа.


n = int(input("Enter a number: "))
num_list = []
result = 1
for i in range(1,n+1):
    num_list.append(i)
    result = result * i
print(result)


