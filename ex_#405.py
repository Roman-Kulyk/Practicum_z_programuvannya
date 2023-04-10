#405. Створіть список, який називається languages і містить елементи 'Georgian', 'Estonian' і 'Ukrainian'.
# Напишіть останній елемент списку languages з малої літери, потім «переверніть» його і напишіть з 
# великої літери.


languages = ['Georgian','Estonian','Ukrainian']
print(languages[-1].lower())
print(languages)
print(languages[-1][::-1].upper())