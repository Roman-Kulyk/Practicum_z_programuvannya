# 510. Напишіть програму для сортування за зростанням (за алфавітом) словника за 
# ключами. Словник зберігає пари ключ-значення у вигляді «назва фільму: рік релізу». 
# Інформація виводиться як у вихідних даних: сортування має бути проведено за 
# назвами фільмів.
'''
Вхідні дані:
Немає

Вихідні дані:
('Avengers: Endgame', 2019) ('Guardians of the Galaxy', 2014) ('Iron Man', 2008) 
('Thor', 2011)
'''
dictionary = {'Iron Man': 2008,\
              'Avengers: Endgame': 2019,\
              'Guardians of the Galazy':2014}

myKeys = list(dictionary.keys())
print(myKeys)
myKeys.sort()
print(myKeys)
sorted_dict = {i: dictionary[i] for i in myKeys}

print(sorted_dict)
