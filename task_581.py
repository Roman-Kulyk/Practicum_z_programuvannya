# 581. Дано рядок тексту, в якому слова розділені пррпусками. Надрукуйте всі слова, які зустрічаються в тексті, та їхні частоти як у вихідних даних.
"""
Вхідні дані:
one two three one four five seven ten seven one

Вихідні дані:
('one', 3) ('four', 1) ('seven', 2) ('ten', 1) ('three', 1) ('two', 1) ('five', 1)
"""
text = input("Enter your string: ").split()

string = []
dictionary = {}
for i in text:
    
    if i not in string:
        string.append(i)
        number = text.count(i)
        dictionary.update({i:number})
    else:
        continue
for key,value in dictionary.items():
    print((f"('{key}',{value})"),end = ' ')
print()
