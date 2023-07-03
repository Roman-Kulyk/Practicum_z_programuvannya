# 533.Дано словник, в якому ключі - імена та прізвища, записані через пропуск, 
# відомих розробників мов програмування, а значення - назви мов програмування. 
# Надрукуйте назву мови за введеним ім’ям або прізвищем її розробника.
'''
Вхідні дані:
Gosling
Dennis

Вихідні дані:
Java
C
'''
languages_programmers = {
    'JavaSript': 'Brendan Eich',
    'Python': 'Guido van Rossum',
    'Ruby': 'Yukihiro Matsumoto',
    'PHP': 'Rasmus Lerdorf',
    'Scala': 'Martin Odersky',
    'Java':"Daniel Gosling",
    'C':'Dennis Ricchhie'}
text = input("Enter a name or last name: ")

for key, value in languages_programmers.items():
    if text in value:
        print(f'{value}:{key}')
        break
    else:
        print("There's not such a developer in the list.")
