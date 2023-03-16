#120. Автомобіль подолав відстань s км через населений пункт за t хв. 
#Визначити, чи не порушив водій правил дорожнього руху, 
#якщо швидкість автомобіля при цьому не повинна перевищувати 60 км/год.

s = int(input('Enter a distance (km): '))
t = int(input('Enter a time(min): '))

if (s / t) * 60 > 60:
    print('You did not follow the rule.')
else:
    print('Everything is fine, you can drive further.')