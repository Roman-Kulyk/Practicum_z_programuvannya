#215. Напишіть програму, яка друкує в дному рядку через пропуск усі парні числа від 1 до n 
# (1 < n ≤ 100, n - ціле число, яке вводить користувач). Використайте оператор continue.


n = int(input("Enter a number: "))
for i in range(1, n + 1):
    if i % 2 == 0:
        print(i,end = ' ')
    else:
        continue
print()