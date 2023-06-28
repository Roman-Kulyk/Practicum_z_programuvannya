# 518. Створіть словник, що містить назви продуктів в уявному холодильнику. 
# Найменування їжі будуть ключами, а відповідне значення кожного продукту харчування 
# має бути значенням-рядком, що описує їжу. Після введення користувачем назви продукту,
# виведіть повідомлення про наявність або відсутність його у холодильнику.
'''
Вхідні дані:
butter
milk

Вихідні дані:
butter is a dairy product with high butterfat content
milk wasn't found in the fridge
'''
dictionary = {'butter':'is a dairy product with high butterfat content',\
              'fish':'it nice to have',\
              'yoghurt':'pretty good for children',\
              'meet':'is a source of power',}
text = input('Enter name of product: ')


if text in dictionary:
    print(f'{text}: {dictionary[text]}')
else:
    print(f"{text} wasn't found in fridge.")