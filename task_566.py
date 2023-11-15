# 566. Напишіть програму для підрахунку повторюваних символів у введеному рядку.
"""
Вхідні дані:
the quick brown fox jumps over the lazy dog

Вихідні дані:
t 2
h 2
e 3
  8
u 2
r 2
o 4
"""
text = input("Enter your string: ")
string = ''
for i in text:
    
    if text.count(i) > 1 and i not in string:
        string += i
        print(i,text.count(i))
    else:
        continue