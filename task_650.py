# 650. Напишіть функцію для підрахунку входжень кожного слова в певному реченні.
'''
Вхідні дані:
the quick brown fox jumps over the lazy dog

Вихідні дані:
{'the': 2, 'quick': 1, 'brown': 1, 'fox': 1, 'jumps': 1, 'over': 1, 'lazy': 1, 'dog': 1}
'''
def vocab_func():
    vocab_dict = {}
    text = input("Enter you text: ").split()
    for i in text:
        if i not in vocab_dict:
            vocab_dict[i] = 1
        else:
            vocab_dict[i] += 1
    print(vocab_dict)

vocab_func()