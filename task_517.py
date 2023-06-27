# 517. Створіть словник, у якому ключі - імена відомих програмістів, а значення - 
# їхні дати народження у форматі dd/mm/yyyy. Напишіть програму, яка за введеним ім’ям 
# відомого інформатика друкує його дату народження або у відсутності такого - 
# відповідне повідомлення як у вихідних даних.
'''
Вхідні дані:
Ada Lovelace
Jack Dorsey

Вихідні дані:
Ada Lovelace's birthday is 10/12/1815.
Sadly, we don't have Jack Dorsey's birthday.
'''
dictionary = {'Ada Lovelace':'10/12/1815',\
              'Dima Sytnyk':'01/03/1982',\
              'Roman Kulyk':'14/02/1980'}
text = input('Enter name of person: ')

if text in dictionary:
    print(f'{text} was born {dictionary[text]}')
else:
    print(f"Sadly, we don't have {text}'s birthday.")