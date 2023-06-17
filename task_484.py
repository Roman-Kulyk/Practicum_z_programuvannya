# 484. Виведіть таблицю розміром n × n, заповнену числами від 1 до n2 по спіралі, 
# що виходить з лівого верхнього кута і закрученою за годинниковою стрілкою.
'''
Вхідні дані:
4

Вихідні дані:
1 2 3 4
12 13 14 5
11 16 15 6
10 9 8 7
'''
n = int(input("Enter the table size: "))
table =[[0] * n for i in range(n)]
x, y =0, 0
dx, dy = 0, 1
for i in range(n**2):
    table[x][y] = i + 1
    if x + dx < 0 or x + dx == n or y + dy < 0 or y + dy == n or table[x + dx][y + dy]!=0:
        dx, dy = dy, -dx
    x, y = x + dx, y + dy
for row in table:
    print(' '.join([str(elem) for elem in row]))