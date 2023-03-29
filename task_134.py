#134. Напишіть програму виведення текстового варіанта шкільних оцінок: 1, 2, 3 (початковий рівень - initial level), 
#4, 5, 6 (середній рівень - average level), 7, 8, 9 (достатній рівень - sufficient level), 
#10, 11, 12 (високий рівень - high level).


n = int(input('Enter a grade: '))
if n == 1 or n == 2 or n == 3:
    print('Initial level')
elif n == 4 or n == 5 or n == 6:
    print('Average level')
elif n == 7 or n == 8 or n ==9:
    print('Sufficient level')
elif n == 10 or n == 11 or n == 12:
    print('High level')
else:
    print('Incorrect number!')