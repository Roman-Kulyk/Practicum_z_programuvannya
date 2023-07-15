# 618.Напишіть функцію, яка до введеного рядка на початку додає рядок Is. 
# Якщо даний рядок вже починається з Is, 
# то початковий рядок виводиться без змін.
'''
Вхідні дані:
list
Is empty

Вихідні дані:
Is list
Is empty
'''
def is_list(text):
    if text.startswith('Is'):
        print(text)
    else:
        print('Is '+ text)


is_list('list')
is_list("Is empty")