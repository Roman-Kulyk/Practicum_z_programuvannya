# 681. Дано список цілих чисел, в якому зустрічаються однакові значення. 
# Напишіть функцію для друку цього списку після видалення всіх однакових значень.
'''
Вхідні дані:
45 67 23 45 111 67 12 55

Вихідні дані:
45 67 23 111 12 55
'''
def reapeted_nums():
    lst = [int(item) for item in input("Enter the list members: ").split()]
    reapeted_nums_set = set(lst)
    for i in reapeted_nums_set:
        print(i, end=' ')
    print()

reapeted_nums()