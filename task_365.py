# 365. Користувач вводить рядок, у якому містяться слова, знаки пунктуації, 
# причому усі слова записуються разом і перша літера кожного слова є великою. 
# Напишіть програму, яка виводить рядок, у якому введені слова розділені пропусками.
'''
Вхідні дані:
TheOldSeaDogAtTheAdmiralBenbow

Вихідні дані:
The Old Sea Dog At The Admiral Benbow
'''
word_list = input("Enter a string: ")
words = word_list.split()
print(words)
result = " ".join(word_list)
print(result)