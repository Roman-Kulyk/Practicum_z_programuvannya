# 392. Дано рядок. Знайдіть в цьому рядку найдовше слово і виведіть його. 
# Якщо в рядку кілька слів однакової максимальної довжини, виведіть перше з них.
"""
Вхідні дані:
The Lord of the Rings: The Two Towers (Adventure, Drama, Fantasy) [2002].
The Matrix (Action, Sci-Fi) [1999].
WALL-E (Animation, Adventure, Family) [2008].

Вихідні дані:
Adventure
Matrix
Animation
"""
string = input("Enter your string: ")
words = string.split()
max_word_len = max(words,key = lambda x: len([ char for char in x if char.isalpha()]))
print(max_word_len)