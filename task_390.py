# 390. Дано слово, що складається лише з малих англійських літер. Визначте, яку найменшу 
# кількість літер потрібно дописати до цього слова праворуч так, щоб воно стало паліндромом.
"""
Вхідні дані:
NASA
Mars
Webb

Вихідні дані:
1
3
2
"""

def min_chars_to_make_palindrom(word):
    reversed_word = word[::-1]
    for i in range(len(word)):
        print(word[i:])
        print(reversed_word[:len(word)- i])
        if word[i:] == reversed_word[:len(word)- i]:
            
            return i
        
word = "Mars"
min_chars_needed = min_chars_to_make_palindrom(word)
print(f"Minimum amount of chars needed to add: {min_chars_needed}")