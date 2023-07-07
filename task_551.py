# 551. Напишіть програму для сортування за спаданням словника за значеннями. 
# Словник зберігає пари ключ-значення у вигляді «країна: столиця». Інформація 
# виводиться як у вихідних даних: сортування має бути проведено за назвами столиць 
# у порядку, протилежному алфавітному. Примітка. При використанні метода sorted, 
# можна застосувати як ключ лямбда-функцію на зразок key=lambda x: x[1].
'''
Вхідні дані:
Немає

Вихідні дані:
[('France', 'Paris'), ('Canada', 'Ottawa'), ('Ukraine', 'Kyiv'), ('Denmark', 'Copenhagen'), ('China', 'Beijing')]
'''
dictionary = {
              'Canada':'Ottawa',
              'Denmark': 'Copenhagen',
              'Ukraine':'Kyiv',
              'China':'Beijing',
              'France':'Paris'}


sorted_dictionary = sorted(dictionary.items(),reverse=True, key = lambda x:x[1])
converted_dict = dict(sorted_dictionary)

print(list(converted_dict.items()))
