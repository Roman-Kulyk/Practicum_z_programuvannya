#84.Равлик повзе по вертикальній жердині висотою h метрів, піднімаючись за день
#на a метрів, а за ніч спускаючись на b метрів. На який деньравлик доповзе до
#вершини жердини? Дані вводяться у порядку h, a, b.

h = int(input('Enter a number h: '))
a = int(input('Enter a number a: '))
b = int(input('Enter a number b: '))

d = ((h-a)//(a-b))+1
print(d)


