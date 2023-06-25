# 516. Напишіть програму для створення словника із введеного рядка символів для 
# підрахунку кількості символів.
'''
Вхідні дані:
Lorem ipsum dolor sit amet

Вихідні дані:
{'L': 1, 'o': 3, 'r': 2, 'e': 2, 'm': 3, ' ': 4, 'i': 2, 'p': 1, 
's': 2, 'u': 1, 'd': 1, 'l': 1, 't': 2, 'a': 1}
'''
text = input("Enter a text: ")

dictionary = {}

for i in text:
    if i in dictionary:
        dictionary[i] +=1
    else:
        dictionary[i] = 1
'''
for key, value in dictionary.items():
    print(key + ":" + str(value))
'''
print(dictionary)