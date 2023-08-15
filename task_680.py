# 680.Напишіть функцію, яка приймає три рядки в якості аргументів: start_message, error_message, 
# end_message. 
#Функція повинна запитувати у користувача введення до тих пір, 
#поки не буде введено ціле число (рядок, який конвертується функцією int без помилок). 

#Перед першим запитом введення повинен бути виведене значення start_message, 
# після кожного помилкового введення потрібно виводити значення рядка error_message 
# і при вдалому введенні потрібно вивести рядок end_message і 
# повернути отримане ціле число з функції. Кожне повідомлення повинно знаходитися на 
# окремому рядку. 
#Гарантовано, що в якийсь момент користувачем буде введено ціле число.
'''
Input int number:
five
Wrong value. Input int number:
5

Вихідні дані:
5
Thank you.
'''
def get_integer(start_message, error_message, end_message):
    print(start_message)
    while True:
        try:
            user_input = int(input())
            print(end_message)
            return user_input
        except ValueError:
            print(error_message)

start_message = 'Enter an integer:'
end_message = 'Thanks, an integer accepted!'
error_message = 'Wrong value. Input int number:'
number = get_integer(start_message, error_message,end_message)
print("You entered number:", number)