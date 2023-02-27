#79.Школа вирішила замінити парти у трьох кабінетах. Кожна парта розрахована
#на двох учнів. Враховуючи кількість учнів у кожному класі,надрукуйте найменшу
#можливу кількість парт, які треба придбати. Програма повинна прочитати три
#цілих числа: кількість учнів в кожномуз трьох класів a, b та c відповідно.

import math
a = int(input('Enter a number: '))
b = int(input('Enter a number: '))
c = int(input('Enter a number: '))

n =  math.ceil(a/2)+math.ceil(b/2) + math.ceil(c/2)
print(n)
print('It added to index after restoring.')
