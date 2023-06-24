# 511. Напишіть програму для сортування за спаданням (порядок, зворотний алфавітному)
# словника за ключами. Словник зберігає пари ключ-значення у вигляді «країна: 
# столиця». Інформація виводиться як у вихідних даних: сортування має бути проведено 
# за назвами країн.
'''
Вхідні дані:
Немає

Вихідні дані:
[('Ukraine', 'Kyiv'), ('France', 'Paris'), ('Denmark', 'Copenhagen'), 
('China', 'Beijing'), ('Canada', 'Ottawa')]
'''
dictionary = {'Ukraine':'Kyiv',\
              'France':'Paris',\
              'Denmark':'Copenhagen',\
              'China':'Beijing',\
              'Canada':'Ottawa'}
          
myKeys = list(dictionary.keys())
#print(myKeys)
myKeys.sort(reverse=True)
#print(myKeys)
sorted_dict = {i: dictionary[i] for i in myKeys}
print(sorted_dict)