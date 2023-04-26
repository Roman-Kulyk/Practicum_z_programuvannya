# 281. Дано натуральне число n. Визначте, яким за рахунком числом Фібоначчі воно є. 
# Якщо n не є числом Фібоначчі, виведіть значення -1.
'''
Вхідні дані:

11
8

Вихідні дані:

-1
6

'''
n = int(input("Enter a number: "))
fibonacci = [0,1]#it initialize the sequence
for i in range(2, n + 1):#it provide a range for the sequence
    next_num = fibonacci[i -1] + fibonacci[i - 2]#it generates next member of fibonacci sequence
    fibonacci.append(next_num)#it add member to the fibonacci sequence
    print(fibonacci)
if n in fibonacci:
    print(fibonacci.index(n))#it prints the number's order in the sequence
else:
    print(-1)