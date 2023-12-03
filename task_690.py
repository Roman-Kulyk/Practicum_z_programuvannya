# 690. Напишіть програму, яка друкує попередній день для певної дати як у вихідних даних у 
# форматі рррр-мм-дд. Напишіть окремі функції для обробки даних, які вводить користувач і 
# використайте їх у програмі.
"""
Вхідні дані:
1 3 2019
1 1 2020
1 9 2019

Вихідні дані:
2019-2-28
2019-12-31
2019-8-31
"""
from datetime import datetime, timedelta

def input_date():
    user_input_date = input("Enter the date in format dd-mm-yyyy: ")
    date_obj = datetime.strptime(user_input_date, "%d-%m-%Y")
    return date_obj

def next_day(start_date):
    new_date = start_date - timedelta(days=1)
    return new_date

def main_program():
    start_date = input_date()
    result = next_day(start_date)
    print_result(start_date, result)
    
def print_result(start_date, result):
    print(f"Entered date:{start_date.strftime('%d-%m-%Y')}")
    print(f"Next day:{result.strftime('%Y-%m-%d')}")
    
main_program()