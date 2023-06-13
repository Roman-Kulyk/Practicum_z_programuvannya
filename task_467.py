# 467. Напишіть програму для перетворення двійкового числа в десяткове число.
'''
Вхідні дані:
1001
101010111
10000

Вихідні дані:
9
343
16
'''
binary = input("Enter a binary number: ")#it input a binary number
decimal = 0 #it initialize decimal variable
power = len(binary) - 1 #it counts maximum power value
for digit in binary: #for every digit in binary
    decimal += int(digit)* 2 ** power # it counts power of 2 multiplied on digit
    power -= 1 #with every iteration decrease power by 1
print("Decimal equivalent of ", binary,"is ",decimal) #it prints output
