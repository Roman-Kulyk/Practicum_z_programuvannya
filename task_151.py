#151. Дано ціле число k (1 ≤ k ≤ 365). Визначити, яким буде k-й день року: вихідним (субота або неділя) або робочим, 
#якщо 1 січня - понеділок.

'''
Вхідні дані:
5
7
56

Вихідні дані:
working day
day off
day off
'''
k = int(input("Enter a number: "))
if k % 6 == 0 or k % 7 == 0:
    print("day off")
else:
    print("working day")