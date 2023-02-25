#65.Автомобіль може проїхати відстань n кілометрів за день. Скільки днів пройде
#для проїзду маршруту довжиною m кілометрів? Програмаотримує два цілих
#додатних числа: n і m.

import math
n = int(input('Enter first number: '))
m = int(input('Enter second number: '))
s = math.ceil(m/n)
print(s)
