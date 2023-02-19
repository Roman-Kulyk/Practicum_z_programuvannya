#24.Напишіть програму для форматування числа з відсотком.
number = float(input('Enter your number: '))
percent = number *100
print('{0:.2f}'.format(percent) + '%')
