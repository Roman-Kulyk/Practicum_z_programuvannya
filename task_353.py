# 353. Користувач вводить рядок і певний номер n символа у ньому. 
# Напишіть програму для видалення n-го символу з не порожнього рядка. 
# Цикли і вказівку «якщо» для розв’язування задачі використовувати не можна.
'''
Вхідні дані:
Poirot stopped for a moment, and gazed sorrowfully over the beautiful expanse of park, still glittering with morning dew.
27

Вихідні дані:
Poirot stopped for a moment and gazed sorrowfully over the beautiful expanse of 
park, still glittering with morning dew.
'''
txt = input("Enter a string: ")
char = int(input("Enter a symbol: "))
print(txt[:char]+txt[char+1:])