#76.Припустимо, учнівські канікули тривали кілька днів. Напишіть програму, на
#вхід якої подається кількість днів, а на екран виводиться увідформатованому
#вигляді (вирівнювання за лівим краєм, ширина поля:10 знаків) загальна
#тривалість канікул у годинах, хвилинах,секундах.

days = int(input('Enter a days value: '))
hh = days*24
mm = days*60
ss = days*24*60*60

print('{0:<10d}'.format(hh) +'hours')
print('{0:<10d}'.format(mm)+ 'minutes')
print('{0:<10d}'.format(ss)+ 'seconds')

            
