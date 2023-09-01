# 682. Напишіть функцію для отримання всіх можливих двозначних комбінації літер із рядка цифр 
# (від 1 до 9). Для розв’язування задачі використайте словник: 
# string_maps = {'1': 'abc', '2': 'def', '3': 'ghi', '4': 'jkl', '5': 'mno', '6': 'pqrs', 
# '7': 'tuv', '8': 'wxy', '9': 'z'}.
'''
Вхідні дані:
12
11

Вихідні дані:
['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']
['aa', 'ab', 'ac', 'ba', 'bb', 'bc', 'ca', 'cb', 'cc']
'''
string_maps = {'1': 'abc', '2': 'def', '3': 'ghi', '4': 'jkl', '5': 'mno', '6': 'pqrs', 
'7': 'tuv', '8': 'wxy', '9': 'z'}
def get_combinations(digits):
    if len(digits)!=2:
        return []
    first_digit = digits[0]
    second_digit = digits[1]
    if first_digit not in string_maps.keys() or second_digit not in string_maps.keys():
        return []
    first_letters = string_maps[first_digit]
    second_letters = string_maps[second_digit]

    combinations = []
    for letter1 in first_letters:
        for letter2 in second_letters:
            combinations.append(letter1 + letter2)
        return combinations
    
digits = input('Enter string of numbers(1 to 9):')
combinations = get_combinations(digits)
print('Possible combinations: ', combinations)