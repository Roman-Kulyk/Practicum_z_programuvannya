#Виведіть вітальне повідомлення для кожного користувача після його входу на сайт. 
# Cтворіть список з кількох імен користувачів, включаючи ім’я 'Admin'. Перебираючи 
# елементи списку, виведіть повідомлення для кожного користувача. Для користувача з 
# ім’ям 'Admin' виведіть особливе повідомлення - наприклад: Hello Admin, 
# I hope you’re well.. У інших випадках виводиться універсальне привітання - 
# наприклад: Hello Alex, thank you for logging in again.. Додайте команду if, яка 
# перевірить, що список користувачів не порожній. Якщо список порожній, виведіть 
# повідомлення: We need to find some users!. Видаліть зі списку всі імена 
# користувачів і переконайтеся у тому, що програма виводить правильне повідомлення.


users_list = ['Roman','Ivan','Petro','Admin']
if users_list == []:
        print('We need to find some users!')

for user in users_list:
    if user == 'Admin':
        print("Hello Admin, I hope you’re well.")
    else:
        print("Hello " + user +", thank you for logging in again.")

