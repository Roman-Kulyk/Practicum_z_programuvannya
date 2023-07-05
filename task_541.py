# 541. Дано два словники, в яких ключами є малі букви латинського алфавіту, 
# а значеннями - цілі числа. В першому словнику можуть зустрічатися ключі чи значення, 
# які присутні в другому словнику, або навпаки. 
# Наприклад, вміст словників може бути наступний: 
# a = {'x' : 1, 'y' : 2, 'z' : 3}, b = {'w' : 10, 'x' : 11, 'y' : 2}. 
# Надрукуйте спільні пари «ключ-значення» для обох словників у 
# форматі як у вихідних даних.
'''
Вхідні дані:
Немає

Вихідні дані:
('y', 2)
'''

a = {'x' : 1, 'y' : 2, 'z' : 3}
b = {'w' : 10, 'x' : 11, 'y' : 2}

set_1 = set(list(a.keys()))
set_2 = set(list(b.keys()))

set_3 = set(list(a.values()))
set_4 = set(list(b.values()))

set_5 = set(list(a.items()))
set_6 = set(list(b.items()))

for i in (set_1.intersection(set_2)):
    print(i)

for i in (set_3.intersection(set_4)):
    print(i)

for i in (set_5.intersection(set_6)):
    print(i)