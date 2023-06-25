# 513. Створіть словник, в кому ключі – назви днів тижня, а значення - цілі числа, 
# що позначають порядковий номер дня тижня від 0 до 6. Надрукуйте назву дня за 
# введеним порядковим номером дня. Якщо введений номер виходить за межі, програма 
# жодних повідомлень не друкує і не повідомляє про помилку.
'''
Вхідні дані:
3
0

Вихідні дані:
Wednesday
Sunday
'''
days = {'Sunday':0,\
       'Monday':1,\
       'Tuesday':2,\
       'Wednesday':3,\
       'Thursday':4,\
       'Friday':5,\
       'Saturday':6}
num = int(input("Enter your number: "))


if num in range(0,7):
    for day, day_num in days.items():
        if day_num == num:
            print(day)
        else:
            pass
