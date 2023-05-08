# 317. Дано два слова. Скласти програму, яка визначає, 
# чи перше слово починається на ту ж букву, на яку закінчується друге слово.
'''
Вхідні дані:

Python
Ruby

Вихідні дані:

False

'''
word_1 = input("Enter  a word: ")
word_2 = input("Enter another word: ")
if word_1[0]==word_2[-1]:
    print(True)
else:
    print(False)