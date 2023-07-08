# 556. Дано словник, що складається з пар слів. Кожне слово є синонімом до парного 
# йому слова. Всі слова в словнику різні. Для даного слова визначте його синонім. 
# Програма отримує на вхід кількість пар синонімів n. Далі йде n рядків, кожен рядок 
# містить рівно два слова-синоніми. Після цього вводиться одне слово. Програма повинна 
# вивести синонім до даного слова.
'''
Вхідні дані:
3
Solar Heliac
Day Daytime
Arrive Occur
Heliac

Вихідні дані:
Solar
'''
words = {}
n = int(input("Enter your number: "))
for _ in range(n):
    word1, word2 = input("Enter your words through the spacebar: ").split()
words[word1] = word2
words[word2] = word1

search_word = input("Enter a word:")
if search_word in words:
    synonym = words[search_word]
    print(synonym)