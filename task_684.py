# 684. Напишіть функцію для перевірки, чи є рядок «панграмою» чи ні. Примітка. 
# Панграма - фраза, вислів або текст в якому присутні всі літери абетки принаймні по одному разу. 
# Наприклад: «How vexingly quick daft zebras jump» (30 літер), «The five boxing wizards jump 
# quickly» (31 літера), «Cwm fjord bank glyphs vext quiz» (26 літер), «The quick brown fox jumps 
# over the lazy dog» (35 літер).
"""
Вхідні дані:
Cwm fjord bank glyphs vext quiz
How vexingly quick daft zebras jump
Mr Jock, TV quiz PhD, bags few lynx

Вихідні дані:
True
True
True
"""

def ifpangram():
    import string
    text = input("Enter the list members: ")
    set_text = (set(text.lower()))
    text = ''
    for i in sorted(set_text):
        if i.isalpha() and i not in text:
            text += i
    
    if text == string.ascii_lowercase:
        print(True)
    else:
        print(False)

ifpangram()