# 528. Створіть кілька словників, імена яких - це клички домашніх тварин. 
# У кожному словнику збережіть інформацію про вид домашнього улюбленця та ім’я 
# власника. Збережіть словники в списку з ім’ям pets. Виведіть повідомленя як 
# у вихідних даних.
'''
Вхідні дані:
Немає

Вихідні дані:

Jim is the owner of a pet - a cat.
Alex is the owner of a pet - a dog.
Elena is the owner of a pet - a parrot.
'''
dictionary = {'Jim':'cat',
              'Alex':'dog',
              'Elena':'parrot'}
for key, value in dictionary.items():
    print(f'{key} is the owner or a pet - a {value}.')