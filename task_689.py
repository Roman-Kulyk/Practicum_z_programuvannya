# 689. Напишіть програму, яка друкує наступний день для певної дати як у вихідних даних 
# у форматі рррр-мм-дд. Напишіть окремі функції для обробки даних, які вводить користувач і 
# використайте їх у програмі.
"""
Вхідні дані:
31 8 2019
28 2 2020

Вихідні дані:
2019-9-1
2020-2-29
"""
from datetime import datetime, timedelta

def input_date():
    user_input_date = input("Enter the date in format yyyy-mm-dd: ")
    date_obj = datetime.strptime(user_input_date, "%d-%m-%Y")
    return date_obj

def next_day(start_date):
    new_date = start_date + timedelta(days=1)
    return new_date

def main_program():
    start_date = input_date()
    result = next_day(start_date)
    print_result(start_date, result)
    
def print_result(start_date, result):
    print(f"Entered date:{start_date.strftime('%d-%m-%Y')}")
    print(f"Next day:{result.strftime('%Y-%m-%d')}")
    
main_program()