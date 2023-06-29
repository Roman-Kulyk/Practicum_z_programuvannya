# 520. Напишіть програму, яка приймає рядок символів, 
# і обчислює кількість великих та малих літер.
'''
Вхідні дані:
The quick brown FOX jumps over a lazy DOG

Вихідні дані:
UPPER CASE 7
LOWER CASE 26
'''

text = input("Enter a text: ")

upper = 0
lower = 0

for i in text:
    if i.isupper():
        upper +=1
    elif i.islower():
        lower +=1

print('UPPER CASE', upper)
print('LOWER CASE', lower)