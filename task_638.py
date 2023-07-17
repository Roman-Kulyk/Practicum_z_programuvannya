# 638.Напишіть функцію, яка приймає послідовність цілих чисел та ціле число n, 
# що вводяться на окремих рядках. Функція повертає True, якщо вказане число 
# знаходиться всередині списку, або False у протилежному випадку.
'''
Вхідні дані:
3 6 9 10 23 14
23

Вихідні дані:
True
'''
def if_in_sequence():
    sequence = [int(item) for item in input("Enter the list members: ").split()]
    num = int(input("Enter your character: "))
    if num in sequence:
        print(True)
    else:
        print(False)
    #print(sequence)

if_in_sequence()