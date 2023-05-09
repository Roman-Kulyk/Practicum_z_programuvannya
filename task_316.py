# 316. Дано натуральне число. 
# Знайти число, що отримується з вхідного перестановкою 
# його першої та останньої цифр. 
# Врахувати випадок введення одноцифрового числа.
'''
Вхідні дані:

1467
5
11
12

Вихідні дані:

7461
5
11
21
'''
number = input("Enter a number: ")
if len(number) == 1:
    print(number)
else:
    first_digit = number[0]
    last_digit = number[-1]
    new_number = last_digit + number[1:-1] + first_digit
    print(new_number)