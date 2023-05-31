# 424. Визначте, скільки різних слів у введеному рядку.
'''
Вхідні дані:
New Delhi New York Paris Prague Reykjavik
Happy New Year Happy New Year May we all have a vision now and then Of a world where every neighbor is a friend

Вихідні дані:
6
19
'''
lst = []
lst = [(item) for item in input("Enter the list items: ").split()]
elements = []
for i in lst:
    if i not in elements:
        elements.append(i)
    else:
        pass
print(len(elements))