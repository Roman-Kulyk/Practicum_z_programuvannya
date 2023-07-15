# 621. Напишіть функцію, яка приймає два слова в якості вхідних даних, і надрукуйте 
# найдовше слово. Якщо слова мають однакову довжину, то функція повинна надрукувати 
# слова в окремих рядках.
'''
Вхідні дані:
five three

Вихідні дані:
three
'''
def max_len(word_1, word_2):
    if len(word_1) > len(word_2):
        print(word_1)
    elif len(word_2) > len(word_1):
        print(word_2)
    else:
        print(word_1)
        print(word_2)


max_len('five','three')
max_len('nine','one')
max_len('two','one')