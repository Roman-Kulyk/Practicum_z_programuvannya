#126. Напишіть програму, яка запропонує користувачеві ввести десяткове число у межах від 1 до 10. 
#Програма повинна вивести версію римського числа. Програма має враховувати ситуацію, 
#якщо введене число є за межами діапазону від 1 до 10.

num = int(input('Enter a number: '))
if num == 1:
    print('I')
elif num ==2:
    print('II')
elif num == 3:
    pritn('III')
elif num == 4:
    print('IV')
elif num == 5:
    print('V')
elif num == 6:
    print('VI')
elif num == 7:
    print('VII')
elif num == 8:
    print('VIII')
elif num == 9:
    print('IX')
elif num == 10:
    print('X')
else:
    print('Number is out of range.')