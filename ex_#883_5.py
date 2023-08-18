# Створіть порожній файл guest_book.txt у текстовому редакторі. Напишіть цикл while, який 
# запитує у користувачів імена. При введенні кожного імені виведіть на екран рядок з вітанням 
# для користувача і запишіть рядок вітання у файл з ім’ям guest_book.txt. Простежте за тим, 
# щоб кожне повідомлення розміщувалося в окремому рядку файла. Передбачте вихід з циклу.


while True:
    name = input('Enter your name [type q to quit]: ')
    if name == 'q':
        break

    greeting = ('Hello, ' + name)
    print(greeting) 
        
    freading = open('ex_#883_5_guest_book.txt','at')
    print(greeting, file=freading)
    freading.close()    