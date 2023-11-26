# 600.Дано текст в рядку. Виведіть слово, яке в цьому тексті зустрічається найчастіше. 
# Якщо таких слів кілька, виведіть те, яке менше в лексикографічному порядку.
"""
Вхідні дані:
Tokyo Seoul London Sofia Tokyo Sydney London

Вихідні дані:
London
"""
text = input("Enter your row: ")


word_count = {}
for word in text.split():
    word_count[word] = word_count.get(word, 0)

max_occurences = max(word_count.values())
most_frequent_words = [word for word, count in word_count.items() if count == max_occurences]


result = min(most_frequent_words)

print(result)