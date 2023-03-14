#114. Напишіть програму, щоб перевірити, чи є введене число додатним, від’ємним або це нуль.
num = int(input('Enter your number: '))
if num > 0:
    print('Your number is greater than 0')
elif num == 0:
    print('Your number is 0')
else:
    print('Your number is less than 0')
