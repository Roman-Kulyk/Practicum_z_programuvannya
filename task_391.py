# 391. Користувачем вводиться рядок, що містить натуральні цілі числа і слова. Необхідно 
# сформувати новий рядок лише з чисел, розділених комою і пропуском, що містяться у введеному
# рядку.
"""
Вхідні дані:
District 9 (2009) - IMDb 8
Reviews 1301 user | 478 critic | Popularity 511
R | 1h 52min | Sci-Fi, Thriller | 13 August 2009 (Ukraine)

Вихідні дані:
9, 2009, 8
1301, 478, 511
1, 52, 13, 2009
"""
string = input("Enter your string: ").split()
digit_list = []
for i in string:

    if i.isdigit():
        digit_list.append(i)
for i in digit_list:
    
    i = int(i)
    print(i, end=', ')
    
print()

import re
def sort_numbers(string):
    #numbers = [word for word in string.split() if word.isdigit()]
    numbers = re.findall(r'\b\d+\b', string)
    #it returns all non-overlapping matches of pattern in string, as list of strings or tuples.
    new_string = ', '.join(numbers)
    print(type(new_string))
    return new_string

entered_string = input("Enter your string: ")
new_string = sort_numbers(entered_string)
print(new_string)