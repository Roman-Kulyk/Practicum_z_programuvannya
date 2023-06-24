# 507. Створіть словник зі списками добрих справ на сьогодні і на завтра. 
# Надрукуйте із словника добрі справи, які плануєш зробити сьогодні і взавтра.
'''
Вхідні дані:
Немає

Вихідні дані:
today:
Make a compliment to a friend
Call your grandparents
Embrace parents
tomorrow:
Feed the birds in the park
Give unnecessary things to those who need them
Smile

'''
list_of_googness = {'today':['Make a compliment to a friend','Call your grandparents','Embrace parents'],\
                    'tomorrow':['Feed the birds in the park','Give unneccessary things to those who need them'\
                                'Smile']}

print('today:')
for i in list_of_googness['today']:
    print('* ',i)

print('tomorrow:')
for i in list_of_googness['tomorrow']:
    print('* ',i)