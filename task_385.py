# 385. Дано рядок, що є параграфом в тексті. Текст необхідно відформатувати так, 
# щоб довжина кожного рядка не перевищувала числа m, слова при цьому не розривати. 
# На вхід програмі спочатку подається число m (0 < m ≤ 255). У наступному рядку знаходиться 
# вхідний текст. Довжина слів в ньому не перевищує m, слова розділені рівно одним пропуском. 
# Виведіть розбиття цього тексту на рядки довжиною не більше ніж m символів (слово 
# переноситься на наступний рядок тільки якщо в поточному рядку його розмістити вже 
# неможливо). Новий рядок не повинен починатися з пропуску.
"""
Вхідні дані:
10
The Wonderful Wizard of Oz

Вихідні дані:
The
Wonderful
Wizard of
Oz
"""
def formatted_text(m, text):
    words = text.split()#it splits string into separate words and put them into words list
    result = []#it create empty list of strings and assign it to result variable
    current_line = ""#it create empty string and assign it to current_line variable

    for word in words:#it checks every word in words list
        if len(current_line) + len(word) + 1 <= m:#if it len with len of current_string+1 less than m
            if current_line != "":#if there is smt in current line
                current_line += " "#it adds an empty space after it
            current_line += word#it adds word to the current_string
        else:#if it len with len of current_string+1 more than m
            result.append(current_line)#it appends current_line to the result list
            current_line = word#it assign word to current_line
    result.append(current_line)#it append current_line to the result list
    return result#it returns result
m = int(input("Enter a number m: "))
text = input("Enter a text: ")

formatted_text = formatted_text(m, text)
for line in formatted_text:
    print(line)
