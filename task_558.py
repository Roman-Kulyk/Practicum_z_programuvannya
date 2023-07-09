# 558. Вводиться кількість слів у словнику. Словник складається з пар слів. 
# Кожне слово є синонімом іншого слова. Всі слова в словнику різні. 
# Після введення словника вводиться ще одне слово. Знайти синонім для нього.
'''
Вхідні дані:
3
amazing extraordinary
beautiful magnificent
delicious savory
extraordinary

Вихідні дані:
amazing
'''
words = {}
n = int(input("Enter your number: "))
for word in range(n):
    word1, word2 = input("Enter your words through the spacebar: ").split()
words[word1] = word2
words[word2] = word1
#words.update({"word1","word2"})
print(words)

search_word = input("Enter a word:")
if search_word in words:
    synonym = words[search_word]
    print(synonym)