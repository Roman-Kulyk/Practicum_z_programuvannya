# 352. Користувач вводить рядок і один символ. 
# Напишіть програму для підрахунку кількості входження символа в рядок. 
# У випадку, якщо введений символ є літерою, великі і малі букви розрізняються.
'''
Вхідні дані:
Poirot shook his head energetically. He was now arranging his moustache with exquisite care.
w

Вихідні дані:
3
'''
txt = input("Enter a string: ")
char = input("Enter a symbol: ")
x = txt.count(char)

print(x) 