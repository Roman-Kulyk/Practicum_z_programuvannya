# 458. Вводиться три числа, через кому і пропуск, що позначають день, місяць і рік. 
#Надрукуйте дату у форматі як у вихідних даних, не використовуючи цикл і звернення 
# до елементів за індексом.
'''
Вхідні дані:
4, 3, 2019

Вихідні дані:
4/3/2019
'''
lst = input("Enter  your date: ").split(', ')
print(f'Your date is: {lst}'.format(lst))
x = '/'.join(lst)

#myTuple = ("John", "Peter", "Vicky")
#x = "#".join(myTuple)
print(x)