'''Обчисліть тривалість якоїсь події. Припустимо, учнівські канікули тривали
кілька днів. На екран треба вивести у відформатованому вигляді (вирівнювання
за лівим краєм, ширина поля: 10 знаків) загальну тривалість цієї події у годинах
, хвилинах, секундах.'''
time = int(input('Enter how many days were your holiday: '))
hours = time * 24
minutes = hours * 60
seconds = minutes * 60
print('{0:<10d} hours\n{1:<10d} minutes\n{2:<10d} seconds'.format(hours, minutes, seconds))
