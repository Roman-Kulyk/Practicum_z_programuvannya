# 456. Напишіть програму, яка приймає послідовність 4-цифрових двійкових чисел, 
# розділених комами, і друкує числа, які ділиться на 5 без остачі, в рядку і розділені 
# комами.
'''
Вхідні дані:
0100,0011,1010,1001,1100

Вихідні дані:
1010
'''


numbers = input("Enter a seequence of 4-digit binary numbers separated by commas:")
print(numbers)
binary_list = numbers.split(",")
print(binary_list)
result_list = [int(binary, 10) for binary in binary_list if int(binary, 2) % 5 == 0]
print("Numbers divisible by 5 are: ", end = "")
print(*result_list, sep = ",")

    