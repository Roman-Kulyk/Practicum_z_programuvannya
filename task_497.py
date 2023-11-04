# 497. Напишіть програму, яка знаходить усі позиції входження підрядка B у рядок A. 
# На першому рядку міститься вхідний рядок, на другому рядку введення вказаний підрядок, 
# позиції якого потрібно знайти. Рядки складаються з символів англійського алфавіту. 
# Програма має вивести позиції входження підрядка B у рядок A (індексація починається з 1),
# розділені пропуском або число -1 в разі, коли підрядок не знайдено.
"""
Вхідні дані:
abacabadaba
aba
abc
d

Вихідні дані:
0 4 8
-1
"""
def find_positions(string, target):
    
    positions = []
    start = 0
    while True:
        pos = string.find(target, start)
        if pos == -1:
            break
        positions.append(pos)
        start = pos + 1
    return positions if positions else [-1]



string = input("Enter your string: ")
target = (input("Input your substring: "))
result = find_positions(string, target)
print(*result)