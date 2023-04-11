#216. Надрукувати всі непарні двоцифрові числа, у яких остання цифра дорівнює n - ціле число, 
# яке вводить користувач.


n = int(input("Enter a number: "))
for i in range(1, 99):
    if i % 2 != 0 and i >10 and i % 10 == n:
        print(i,end = ' ')
    else:
        continue
print()