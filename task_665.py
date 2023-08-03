# 665. Напишіть функцію для сортування рядка в порядку, протилежному алфавітному, 
# без врахування регістру літер.
'''
Вхідні дані:
Ruby

Вихідні дані:
yuRb
'''
def reverse_sortString():
    return "".join(sorted(str, key = lambda x:x.lower(),reverse = True))
     
str = input('Enter your text: ')
print(reverse_sortString())
