# 637. Напишіть функцію, яка отримує рядок слів, розділених пропуском. 
# Надрукуйте рядок слів у звороному порядку.
'''
Вхідні дані:
one two three

Вихідні дані:
three two one
'''
def reverse_string(sentence):
    words = sentence.split()
    reverse_words = words[::-1]
    reversed_sentence = ' '.join(reverse_words)
    print(reversed_sentence)
    

sentence = 'one two three'
reverse_string(sentence)