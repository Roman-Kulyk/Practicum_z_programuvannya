# Чи є рядок «паліндромом»? Рядок є паліндромом, якщо він однаково читається зліва 
# направо та справа наліво. Наприклад, слова Level, Noon, Anna є паліндромами, 
# незалежно від регістру літер. Рядки, які треба перевірити, вводяться користувачем. 
# Введення даних можна перервати, якщо ввести слово escape. Програма повинна вивести 
# результат перевірки у вигляді повідомлення is a palindrome або is not a palindrome.

def if_palindrome():
    while True:
        text = input('Enter your text: ')
        x = text.lower()
        if text == 'escape':
            break
        elif x == x[::-1]:
            print('is a palindrome')
        else:
            print('is not a palindrome')

if_palindrome()




