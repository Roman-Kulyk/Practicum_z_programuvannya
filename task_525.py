# 525. Cтворіть словник з річками і регіонами, територією яких вони протікають. 
# Виведіть повідомлення із назвами річки і регіону, як у вихідних даних, 
# для усіх елементів словника, враховуючи те, що у повідомлення підставляються назви 
# річок і територій із словника.
'''
Вхідні дані:
Немає

Вихідні дані:
The Amazon runs through South America.
The Odra runs through Central Europe.
The Ganges runs through South Asia.
'''
dictionary = {'Amazon':'South America',\
              'Odra':'Central Europe',\
              'Gandes':'South Asia'}
for key,value in dictionary.items():
    print(f'The {key} runs through {value}.')


