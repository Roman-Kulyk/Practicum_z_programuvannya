# 416. Вводиться список чисел. Всі числа списку знаходяться на одному рядку. 
# Виведіть ті його елементи, які зустрічаються в списку лише один раз. Елементи 
# потрібно виводити в тому порядку, в якому вони зустрічаються в списку.
'''
Вхідні дані:
4 5 6 6 6 5 4 4 7 4

Вихідні дані:
7
'''
lst = []
lst =[int(item) for item in input("Enter the list items: ").split()]
for i in lst:
    if lst.count(i) == 1:
        print(i,end=" ")
print()