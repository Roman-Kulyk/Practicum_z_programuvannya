# 512. Надрукуйте елементи словника, де ключі - це числа від 1 до n (обидва числа 
# включно), а значення - квадрати ключів. n – ціле число, яке вводить користувач.
'''
Вхідні дані:
15

Вихідні дані:
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 
12: 144, 13: 169, 14: 196, 15: 225}
'''
n = int(input("Enter a number: "))
dictionary = {}
for i in range(1, n + 1):
    dictionary[i] = i * i

print(dictionary)