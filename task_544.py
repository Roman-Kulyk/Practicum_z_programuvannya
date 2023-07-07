# 544. Напишіть програму, яка підраховує і роздруковує кількість появ кожного 
# символу у введеному рядку.
'''
Вхідні дані:
abcabcdfghj

Вихідні дані:
a, 2
b, 2
c, 2
d, 1
f, 1
g, 1
h, 1
j, 1
'''
#input_string = input('Enter your text: ')#it takes a strint from user
words = list(input("Enter your string: "))#it creates a list from string
print(words)
words = [word.lower() for word in words]#it put all words in lower register
word_freq = {}#initialization of empty dictionary

for word in words:#it checks every word in entered string
        if word in word_freq:#and if word is in dictionary
               word_freq[word] += 1#it add 1 to its value
        else:#if not
              word_freq[word] = 1#it assign 1 to its value

for word,freq in sorted(word_freq.items()):#it prints every pair of items
    print(f"{word},{freq}")#in dictionary through the coma