# 577.Дано послідовність слів, розділених комами. Надрукуйте унікальні слова у 
# лексикографічному порядку як у вихідних даних.
"""
Вхідні дані:
abc,abc,bac,aca

Вихідні дані:
abc,aca,bac
"""
input_sequence = input("Enter your sequence: ")

words = [word.strip() for word in input_sequence.split(',')]

unique_words = sorted(set(words))

print(', '.join(unique_words))
