# 263.- Учні 5 класу вели щоденники спостереження за погодою і щодня записували денну температуру. 
# Знайдіть найнижчу температуру за весь час спостережень. Якщо температура знижувалась нижче -15 градусів,
# необхідно вивести Yes, у протилежному випадку No. Програма отримує на вхід кількість днів, 
# протягом яких проводилося спостереження n (1 ≤ n ≤ 31), потім для кожного дня вводиться температура.
'''
Вхідні дані:

3
-20
2
-18

Вихідні дані:

-20
Yes

'''
n = int(input("Enter a number: "))
num_list = []
for i in range(0,n):
    t = int(input("Enter a number: "))
    num_list.append(t)
print(min(num_list))
if min(num_list) < -15:
    print("Yes")
else:
    print("No")