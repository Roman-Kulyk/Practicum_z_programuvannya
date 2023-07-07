# 543. Напишіть програму для обчислення частоти слів у введеному рядку. 
# Виведення має бути у порядку, що зворотний буквенно-цифровому порядку.
'''
Вхідні дані:
The five boxing wizards jump quickly

Вихідні дані:
wizards: 1
quickly: 1
jump: 1
five: 1
boxing: 1
The: 1
'''
input_string = input('Enter your text: ')#it takes a strint from user
words = input_string.split()#and split in by every single words

words = [word.lower() for word in words]#it put all words in lower register
word_freq = {}#initialization of empty dictionary

for word in words:#it checks every word in entered string
        if word in word_freq:#and if word is in dictionary
               word_freq[word] += 1#it add 1 to its value
        else:#if not
              word_freq[word] = 1#it assign 1 to its value

for word,freq in sorted(word_freq.items(), reverse=True):#it prints every pair of items
    print(f"{word}:{freq}")#in dictionary in reverse order
    