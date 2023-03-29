#139. Перевірити, чи належить число, введене з клавіатури, інтервалу (-5, 3).

a = int(input('Enter a number: '))
b = int(input('Enter a number: '))
c = int(input('Enter a number: '))

if -5 <= a <= 3:
    print(True)
else:
    print(False)

if -5 <= b <= 3:
    print(True)
else:
    print(False)

if -5 <= c <= 3:
    print(True)
else:
    print(False)