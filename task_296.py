# 296. Для настільної гри використовуються картки з номерами від 1 до n. Одна картка загубилася. 
# Знайдіть її, знаючи номери решти карток. Користувач вводить ціле число n, далі n-1 номери решти карток 
# (різні числа від 1 до n). Програма повинна вивести номер втраченої картки.
'''
Вхідні дані:
5
3
4
1
5

Вихідні дані:

2

'''
n = int(input("Enter a number: "))
sum_all = (n *(n + 1)//2)#it founds sum of all numbers of the range
sum_cards = []#it initialize empty list
for i in range(1,n):
    num = int(input("Enter a number: "))#it enter existing card
    sum_cards.append(num)#and add it to the list
    total = sum(sum_cards)#it founds sum of existing cards in the list
print(sum_all - total)#it prints lost card number
