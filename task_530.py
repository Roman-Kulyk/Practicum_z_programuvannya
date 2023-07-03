# 530. Створити словник, у кому ключами є назви команд Національної баскетбольної 
# асоціації (NBA) у північній Америці, а значеннями - списки, на зразок, 
# [Всього ігор, Перемог, Нічиїх, Поразок, Всього очок]. Значення списку - це цілі 
# числа, які обираються довільно. Надрукуйте інформацію про кожну команду як у 
# вихідних даних.
'''
Вхідні дані:
Немає

Вихідні дані:
BOSTON CELTICS 3 2 0 1 8
NEW YORK KNICKS 10 3 3 4 19
INDIANA PACERS 4 2 2 0 11
MIAMI HEAT 12 2 5 5 9
ATLANTA HAWKS 5 2 2 1 10
CHICAGO BULLS 25 10 9 6 38
'''
nba_teams = {'BOSTON CELTICS':[3,2,0,1,8],
             'NEW YORK KNICKS':[10,3,3,4,19],
             'INDIANA PACERS':[4,2,2,0,11],
             'MIAMI HEATS':[12,2,5,5,9],
             'ATLANTA HAWKS':[5,2,2,1,10],
             'CHICAGO BULLS':[25,10,9,6,38]
             }
for key, value in nba_teams.items():
    print(f"{key}:{value[0]} {value[1]} {value[2]} {value[3]} {value[4]}")