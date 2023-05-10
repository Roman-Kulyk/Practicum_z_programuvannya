# 318. Дано натуральне число. 
# Знайти число, що отримується видаленням з вхідного усіх зазначених цифр.
'''
Вхідні дані:

34547
4

Вихідні дані:

357

'''
num = int(input("Enter a number: "))
digits = input("Enter digits to delete: ")
digits_lst = list(digits)#it initialize digits list from string
num_str = str(num)#it initialize num string from integers

for digit in digits_lst:#it finds a digit to delete in number
    num_str = num_str.replace(digit, "")#it actually deletes digits
    result = int(num_str)#it initialize result variable 
print(result)#it prints the result
    