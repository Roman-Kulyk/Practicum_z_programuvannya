# 362. Напишіть програму, яка зчитує рядок, введений користувачем, 
# та визначає у ньому: кількість великих літер, кількість малих літер, 
# кількість символів пропуску.
'''
Вхідні дані:
By Red Flower Bagheera meant fire, only no creature in the jungle will call fire by its proper name.

Вихідні дані:
Upper 4
Lower 76
Spaces 18
'''
txt = input("Enter a string: ")
upper = []
lower = []
spaces = []
for i in txt:
    if i.islower():
        lower.append(i)
    elif i.isupper():
        upper.append(i)
    elif i == ' ':
        spaces.append(i)
print("Upper ", len(upper))
print("Lower ", len(lower))
print("Spaces ", len(spaces))
