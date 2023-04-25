# 277. Написати програму для обчислення суми цифр цілого числа n. Програма має враховувати, 
# що на вхід може подаватися ціле від’ємне число.
'''
Вхідні дані:

-123
1
412098

Вихідні дані:

6
1
24

'''
number = int(input("Enter a number: "))
if number < 0:
    number *= -1
sum_digits = 0
while number > 0:
    sum_digits +=number % 10
    number //= 10
print(sum_digits)
