# 575. Дано ціле число n, за яким слідують n рядків тексту. Надрукуйте кількість різних 
# слів, які з’являються у тексті. Для цього ми визначаємо, що слово - це послідовність 
# символів, що не містить пропусків. Слова розділені одним або декількома пропусками або 
# символами нового рядка. Знаки пунктуації є частиною слова в цьому визначенні.
"""
Вхідні дані:
3
A fool is a person who thinks he's smarter than me.
Yet wolves are more noble sheep, it is difficult for them to imagine their life without the latter. And the sheep?! It's shame to say!
Only when he left the chariot, everyone understood that it was a coachman.

Вихідні дані:
43
"""
n = int(input("Enter your rows number: "))
unique_words = set()
for _ in range(n):
    line = input("Enter your string: ").split()
    unique_words.update(line)
print(len(unique_words))
