# 724. Напишіть програму для перемішування та друку введеної послідовності. Використайте модуль random.
'''
Вхідні дані:
Yellow Pink Green Red Black White

Вихідні дані:
Pink Yellow White Green Black Red
'''
import random
txt = 'Yellow Pink Green Red Black White'.split()
txt_shuffled = ' '.join(random.sample(txt,len(txt)))
print(txt_shuffled)