#207. Надрукувати у рядку m разів число n. Числа m і n - цілі числа, які вводить користувач у порядку n, m.


m = int(input("Enter a number: "))
n = int(input("Enter a number: "))

for i in range(m):
    print(n, end = ' ')
print()