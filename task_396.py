# 396. У заданому рядку знайти найкоротше слово, вивести це слово і його розмір у символах. 
# Слова можуть бути розділені пропусками, декількома пропусками, знаками пунктуації, цифрами 
# тощо. Якщо найкоротших слів є кілька, вивести лише перше з них. Рядок слів гарантовано 
# закінчується крапкою.
"""
Вхідні дані:
He lives in house number 4.
Now is better than never.
Tom Tells the Truth.

Вихідні дані:
He 2
is 2
Tom 3
"""

string = input("Enter your string: ")
words = string.split()
min_word_len = min(words,key = lambda x: len([ char for char in x if char.isalpha()]))

print(f"{min_word_len} {len(min_word_len)}")