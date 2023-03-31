#154. Визначити, чи увійде в конверт з внутрішніми розмірами a і b мм прямокутна листівка з розмірами с і d мм. 
#Для розміщення листівки в конверті необхідний проміжок в 1 мм з кожної сторони. 
#Значення сторін листівки і конверту - цілі числа.

a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
c = int(input("Enter a number: "))
d = int(input("Enter a number: "))

if a - 1 >= c and b -1 >= d:
    print("Yes")
else:
    print("No")