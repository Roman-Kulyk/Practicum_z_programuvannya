#121. Користувач вводить значення температури t у градусах Цельсія. Напишіть програму, яка виводить назву стану, 
#у якому знаходиться вода при цій температурі за нормальних умов.

temp = float(input('Enter a temperature: '))
if temp <= 0:
    print('It is ice.')
elif 0 < temp < 100:
    print('It is actually water.')
else:
    print('It is steam.')
