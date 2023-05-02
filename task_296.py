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
sum_all = (n *(n + 1)//2)
sum_cards = []
for i in range(1,n):
    num = int(input("Enter a number: "))
    sum_cards.append(num)
    total = sum(sum_cards)
print(sum_all - total)
