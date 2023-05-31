# 419. Вводиться список чисел. Всі числа списку знаходяться в одному рядку. 
# Не змінюючи його і не використовуючи додаткові списки, визначте, яке число в цьому 
# списку зустрічається найчастіше. Якщо таких чисел декілька, виведіть будь-яке з них.
'''
Вхідні дані:
1 0 0 1 0 0 1 1 0
2 4 6 9 9 2 3 2 4

Вихідні дані:
0
2
'''
numbers = input("Enter the list members: ").split()
count = {} #it initialize empty dictionary

for n in numbers:#it checks every number in numbers list
    if n in count:#if n in dictionary it goes to another number
        count[n] += 1#and enlarge count to plus one
    else:#in other case
        count[n] = 1#it assign 1 to the number
most_common = None#it initialize empty variable for storing most_common value
max_count = 0#it initialize empty variable for storing max_count value

for n, c in count.items():#it checks every item in dictionary count
    if c > max_count:#if it appears the most often
        most_common = n
        max_count = c
print(most_common)#if so print it's value