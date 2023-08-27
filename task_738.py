# 738. Напишіть програму, яка відкриває вказаний текстовий файл, а потім відображає список всіх унікальних слів, 
# знайдених у файлі.
'''
Вхідні дані:
input.txt

Вихідні дані:
Список унікальних слів з файлу input.txt
'''
freading = open('task_738_input.txt', 'rt' )
poem = freading.read()
freading.close()


unique_word = poem.split(' ')

unique_word_list = []
for i in unique_word:
    if i not in unique_word_list:
        unique_word_list.append(i)
print(unique_word_list)

