# 262. Одноклітинна амеба кожні 3 години ділиться на 2 клітини. 
# Визначити, скільки клітин буде через t годин, якщо спочатку була одна амеба.

'''
Вхідні дані:

6
9
24

Вихідні дані:

4
8
256

'''
t = int(input("Enter a number: "))
n = 1
for i in range(0,t,3):
    n = n*2
print(n)