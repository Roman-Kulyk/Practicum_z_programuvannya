# 398. Напишіть програму, яка переводить натуральне число N (1 ≤ N ≤ 3999) з римської 
# системи числення в десяткову. Вхідний рядок містить число N, записане в римській системі 
# числення. Програма повинна вивести десятковий запис числа N.
"""
Вхідні дані:
MMMCMXCIX
IV
XXI

Вихідні дані:
3999
4
21
"""
def roman_to_decimal(roman):
    roman_numerals = {'I':1, 'V':5,'X':10,'L':'50','C':100,'D':500,'M':1000}
    decimal = 0
    prev_value = 0

    for char in roman[::-1]:
        value = roman_numerals[char]
        if value >= prev_value:
            decimal += value
        else:
            decimal -= value
        prev_value = value
    return decimal

roman_number = input("Enter a roman number: ")
decimal_number = roman_to_decimal(roman_number)
print(f"{roman_number} - {decimal_number}")
