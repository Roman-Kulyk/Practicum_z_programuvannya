# 420. Вводиться список цілих чисел в одному рядку через пропуск. 
# Надрукуйте всі елементи, які перевищують попередній елемент списку, 
# через пропуск в новому рядку в порядку їх розміщення у списку.
'''
Вхідні дані:
5 8 0 2 9 4 1

Вихідні дані:
8 2 9
'''
numbers = list(map(int,input("Enter the list members: ").split()))#it create the list
prev = numbers[0]#it assign first list's member to prev variable
for num in numbers[1:]:#it checks every member starting from 1 index
    if num > prev:#if it greater then previous one
        print(num,end = " ")#if so  print it
    prev=num#and assing num to prev variable
print()