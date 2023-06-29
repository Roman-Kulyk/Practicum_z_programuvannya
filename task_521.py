# 521. Створіть словник із даними про студентів: ключі - імена студентів, 
# значення - бали для кожного. Програма повинна визначити середній бал і вивести 
# імена студентів, чий бал вище середнього.
'''
Вхідні дані:
Немає

Вихідні дані:
Alex
Barbara
'''


dictionary = {'Alex': 4.6,\
              'Barbara':4.7,\
              'Andrew':2.1,\
              'Sarah':3.3}

l = list(dictionary.values())
print(l)
average = sum(l)/len(l)

for key, value in dictionary.items():
    if value > average:
        print(key)

