#102.Напишіть програму, в якій користувач вводить пароль і якщо він співпадає із наперед визначеним паролем для 
#цього користувача, то виводиться повідомлення Password accepted.. У іншому випадку повідомлення буде Sorry, that 
#is the wrong password..

password = input('Enter your password: ')
if password == 'PassworD':
    print('Password accepted.')
else:
    print('Sorry, that is the wrong password.')