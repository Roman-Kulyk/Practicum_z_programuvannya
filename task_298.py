# 298.Скільки всього натуральних чисел складаються з не менш ніж a цифр і 
# не більше, ніж b цифр? 
# Вводяться два довільних натуральних числа a і b в окремих рядках. 
# Виведіть одне число: кількість чисел, що володіють зазначеними властивостями.
'''
Вхідні дані:

1
2
1
1

Вихідні дані:

99
9
'''
a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
count =(9**(a+1) -9)//8-(9**(b+1)-9)//8
print(count)