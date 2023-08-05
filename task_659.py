# 659. Написати функцію для перевірки правильності введеної дати. Функція приймає 
# 3 аргументи - день, місяць та рік і повертає True, якщо така дата є в календарі, 
# і False в протилежному випадку.
'''
Вхідні дані:
04
03
2029
33
11
2019

Вихідні дані:
True
False
'''
def is_valid_date(day,month,year):
    if day < 1 or month < 1 or month > 12 or year < 1:
        return False
    
    if month in[4,6,9,11] and day > 30:#it checks that these months have 30 days
        return False
    elif month == 2:#it checks February
        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
            if day > 29:#if it has 29 days in leap years
                return False
        elif day > 28:#if it has 28 days in ordinary years
            return False
    elif day > 31:#it checks that these months have 31 days
        return False
    return True

print(is_valid_date(30,2,2022))
print(is_valid_date(29,2,2020))
print(is_valid_date(31,11,2021))
print(is_valid_date(25,12,2023))