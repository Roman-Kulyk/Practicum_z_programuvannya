# 617. Напишіть функцію, яка перевіряє, чи подана послідовність порожня чи ні.
'''
Вхідні дані:
Різні типи послідовностей (список, кортеж, словник)

Вихідні дані:
True чи False
'''
def is_empty(text):
    if len(text) == 0:
        result = True
    else:
        result = False
    #return result
    print(result)

is_empty((2,3,4,))
is_empty([1,2,3,])
is_empty({})
