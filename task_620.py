# 620. Напишіть функцію для створення позначок тегів HTML навколо введених рядків. 
# Функція отримує назву тега HTML і рядок, який необхідно помістити у відповідні теги.
'''
Вхідні дані:
strong Python

Вихідні дані:
<strong>Python</strong>
'''
def is_tag(tag, text):
    print('<'+tag+'>'+ text + '</' + tag + '>')


is_tag('strong','Python')
is_tag('light','Java')