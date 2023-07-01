# 523. Створіть англо-німецький словник з назвою e2g і виведіть його вміст на екран.
'''
Вхідні дані:
Немає

Вихідні дані:
stork: storch
hawk: falke
woodpecker: specht
owl: eule
'''
e2g = {'stork':'storch',\
       'hawk':'falke',\
       'woodpecker':'spetch',\
       'owl':'eule'}
for key, value in e2g.items():
    print(key + ':' + value)