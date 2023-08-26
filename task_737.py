# 737. Напишіть програму для перевірки, чи містить введений рядок усі літери англійського алфавіту. 
# Використайте модуль string, для отримання рядкових констант.
'''
Вхідні дані:
The quick brown fox jumps over the lazy dog

Вихідні дані:
True
'''
import string
text = 'The quick brown fox jumps over the lazy dog'
text = text.lower()

for i in string.ascii_lowercase:
    
    if i in text:
        result = True
    else:
        result = False
        break
print(result)