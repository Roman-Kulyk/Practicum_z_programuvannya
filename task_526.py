# 526. Створіть словник з назвами мов програмування (ключі) та іменами розробників 
# цих мов (значення). Виведіть по черзі для усіх елементів словника повідомлення як у 
# вихідних даних.
'''
Вхідні дані:
Немає

Вихідні дані:
My favorite programming language is JavaSript. It was created by Brendan Eich.
My favorite programming language is Python. It was created by Guido van Rossum.
My favorite programming language is Ruby. It was created by Yukihiro Matsumoto.
My favorite programming language is PHP. It was created by Rasmus Lerdorf.
'''
dictionary = {'JavaScript':'Brendan Eich',\
              'Python':'Guido van Rossum',\
              'Ruby':'Yukihiro Matsumoto',\
              'PHP':'Rasmus Lerdorf'}
for key, value in dictionary.items():
    print(f'My favorite programming language is {key}. It was created by {value}.')