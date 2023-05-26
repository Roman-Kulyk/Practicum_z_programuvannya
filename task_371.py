# 371. Дано рядок. Якщо в цьому рядку певний символ зустрічається тільки один раз, 
# виведіть його індекс. Якщо він зустрічається два і більше разів, виведіть індекс 
# його першої і останньої появи. Якщо символ в цьому рядку не зустрічається, нічого 
# не виводьте.
'''
Вхідні дані:
In the centre of the room, clamped to an upright easel, stood the full-length portrait of a young man of extraordinary personal beauty, and in front of it, some little distance away, was sitting the artist himself, Basil Hallward, whose sudden disappearance some years ago caused, at the time, such public excitement and gave rise to so many strange conjectures.
m

Вихідні дані:
24 337
'''
txt = input("Enter a string: ")
char = input("Enter a character to find: ")

x_1 = txt.index(char)
x_2 = txt.rindex(char)

print(x_1,x_2)
