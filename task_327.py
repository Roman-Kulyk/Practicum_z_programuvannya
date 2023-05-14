# 327. Дано рядок. Замініть у цьому рядку усі входження певної літери 
# англійського алфавіту, яку вводить користувач у нижньому регістрі, 
# на відповідну літеру у верхньому регістрі. Спочатку вводиться літера, 
# а потім рядок, у якому треба виконати заміну.
'''
Вхідні дані:

a
"Curiouser and curiouser!" cried Alice (she was so much surprised that for the moment she quite forgot how to speak good English).

Вихідні дані:

"Curiouser And curiouser!" cried Alice (she wAs so much surprised thAt for the moment she quite forgot how to speAk good English).

'''
letter = input("Enter a letter: ")
sentence = input("Enter a sentence: ")

print(sentence.replace("a","A"))
