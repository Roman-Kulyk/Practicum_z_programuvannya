# 672. Напишіть функцію для перевертання кожного слова у введеному тексті.
'''
Вхідні дані:
poT tops
oN ,nomel on nolem

Вихідні дані:
Top spot
No lemon, no melon
'''
def reverse_order():
    text = input("Enter your text: ").split()
    reverse_text = []
    for i in text:
        reverse_text.append(i[::-1])
    for i in reverse_text:
        print(i,end = ' ')
    print()

reverse_order()