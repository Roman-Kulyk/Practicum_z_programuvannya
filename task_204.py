#204. Дано два цілих числа a і b (a ≤ b). Виведіть всі числа від a до b включно.


a = int(input("Enter a number: "))
b = int(input("Enter a number: "))

for i in range(a,b+1):
    print(i, end =' ')
print()
