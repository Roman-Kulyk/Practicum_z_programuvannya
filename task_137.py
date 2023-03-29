#137. Дано натуральне число. Визначити, чи закінчується воно цифрою 5.


number = int(input('Enter a number: '))
if number % 5 == 0:
    print(True)
else:
    print(False)