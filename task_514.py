# 514. Створіть словник у якому ключами є назви жанрів комп’ютерних ігор, 
# а значеннями - назва конкретної гри даного жанру. Виведіть вміст словника як у 
# вихідних даних.
'''
Вхідні дані:
Немає

Вихідні дані:
simulations: Euro Track Simulator
adventure: Myst
rts: Kingdom Two Crowns
action: Grand Theft Auto
sports: FIFA
'''
dictionary ={'simulations': 'Euro Track Simulater',\
             'adventure':'Myst',\
             'rts':'Kingdom Two Crowns',\
             'action':'Grand Theft Auto',\
             'sports':'FIFA'}
for key, value in dictionary.items():
    print(key,':',value)