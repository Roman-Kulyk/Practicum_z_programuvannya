# 359. Напишіть програму, яка зчитує рядок, введений користувачем, 
# що містить дату у формі mm/dd/yyyy. 
# Програма має вивести на екран дату у вигляді Місяць Число, Рік.
'''
Вхідні дані:
12/29/2022
03/04/2025

Вихідні дані:
December 29, 20
March 04, 2025
'''
data = input("Enter a date: ")
x = data.split('/')
if x[0]== '01':
    print("January "+x[1]+', '+x[2])
elif x[0] == '02':
    print("February "+x[1]+', '+x[2])
elif x[0] == '03':
    print("March "+x[1]+', '+x[2])
elif x[0] == '04':
    print("April "+x[1]+', '+x[2])
elif x[0] == '05':
    print("May "+x[1]+', '+x[2])
elif x[0] == '06':
    print("June "+x[1]+', '+x[2])
elif x[0] == '07':
    print("July "+x[1]+', '+x[2])
elif x[0] == '08':
    print("August "+x[1]+', '+x[2])
elif x[0] == '09':
    print("September "+x[1]+', '+x[2])
elif x[0] == '10':
    print("October "+x[1]+', '+x[2])
elif x[0] == '11':
    print("November "+x[1]+', '+x[2])
elif x[0] == '12':
    print("December "+x[1]+', '+x[2])