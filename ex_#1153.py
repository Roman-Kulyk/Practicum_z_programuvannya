#1153. Використайте регулярні вирази для пошуку рядків у тексті. 
# Текст, у якому відбуватиметься пошук, можна скопіювати із сайту Project Gutenberg’s
#  і зберегти у файл. 
# Імпортуйте модуль re, щоб використовувати функції регулярних виразів у Python. 
# Вивести на екран усі слова, які починаються з літери «с», 
# чотирилітерні слова, які починаються з літери c, 
# слова, які закінчуються на букву r, 
# слова, які містять чотири літери time поспіль.

import re

#s = "The TART program runs on Tuesdays and Thursdays, but it does not start until next week"

file_path ='ex_#883_8_Robinzon_Crusoe.txt'
with open('ex_#883_8_Robinzon_Crusoe.txt', 'r', encoding='utf-8') as file:
    s = file.read()

word = re.findall(r'\b[tT]\w+', s)
if word == []:
    print("no word found")
else:
    print(set(word))

    word_1 = re.findall(r'\b[tT]\w{3}\b', s)
if word_1 == []:
    print("no word found")
else:
    print(set(word_1))

word_2 = re.findall(r'\b\w*t\b', s)
if word_1 == []:
    print("no word found")
else:
    print(set(word_2))

    word_3 = re.findall(r"\b\w*next\w*\b", s)
if word_1 == []:
    print("no word found")
else:
    print(set(word_3))