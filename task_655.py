# 655. Напишіть функцію, яка приймає слово у нижньому регістрі і повертає слово 
# з першою великою буквою. Введіть рядок слів через пропуск у нижньому регістрі і 
# застосуйте створену функцію для отримання результату як у вихідних даних.
'''
Вхідні дані:
jived fox nymph grabs quick waltz

Вихідні дані:
Jived Fox Nymph Grabs Quick Waltz
'''
def title_func(*words):
    for word in words:
        word = word.title()
        return word

text = input("Enter your words through the spacebar: ").split
for word in text():
    print(title_func(word), end = ' ')
print()
    
