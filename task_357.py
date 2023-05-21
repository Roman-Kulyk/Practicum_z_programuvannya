# 357. Напишіть програму для видалення символів, 
# які мають непарні значення індексів у введеному користувачем рядку.
'''
Вхідні дані:
monkey
kangaroo

Вихідні дані:
mne
knao
'''
input_string = input("Enter a string: ")
output_string = ""

for i in range(len(input_string)):
    if i % 2 == 0:
        output_string += input_string[i]
print(output_string)