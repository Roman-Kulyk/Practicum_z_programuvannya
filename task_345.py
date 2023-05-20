# 345. Напишіть програму, яка друкує введений користувачем рядок у верхньому 
# регістрі для перших n символів у рядку.
'''
Вхідні дані:
It was early on a fine summer's day, near the end of the eighteenth century, when a young man, of genteel appearance, journeying towards the north-east of Scotland
36
Вихідні дані:
IT WAS EARLY ON A FINE SUMMER'S DAY, near the end of the eighteenth century, when a young man, of genteel appearance, journeying towards the north-east of Scotland
'''
txt = input("Enter a string: ")
n = int(input("Enter amount of symbol to capitalize: "))

frag_1 = txt[:n]#it splits string into two part, first one will ber uppered/
frag_2 = txt[n:]#it splits string into two part, second one will ber printed without any changes

print(frag_1.upper()+frag_2) 
