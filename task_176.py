#176. Дано чотирицифрове число. Замінити усі парні цифри числа на символ * і вивести число.
num = input("Enter a number: ")

new_num = ""
for digit in num:
    if int(digit) % 2 == 0:
        new_num += "*"
    else:
        new_num += digit
print("New number: " + new_num)