# 563. Вводиться текст в одному рядку. Для кожного слова тексту підрахуйте 
# кількість його входжень перед ним.
'''
Вхідні дані:
one two one two three two four three

Вихідні дані:
0 0 1 1 0 2 0 1
'''
text = input("Enter your text: ")
words = text.split()
count = {}

for i in range(len(words)):
    word = words[i]
    count[word] = words[:i].count(word)

output = " ".join(str(count[word]) for word in words)
print(output)
