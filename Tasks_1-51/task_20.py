#20.Напишіть програму, яка зчитує значення двох змінних a і b, потім змінює їх
#значення місцями (тобто в змінній a має бути записано те, щораніше зберігалося
#в b, а в змінній b записано те, що раніше зберігалося в a). Потім виведіть
#значення змінних. Виконайте подане завдання без використання третьої змінної.
#У якому порядку значення змінних були введені, у тому ж порядку повинні і
#виводитися.
var_1=input('Enter your variable_1: ')
var_2=input('Enter your variable_2: ')
var_1,var_2=var_2,var_1
print('variable_1 is now equal to:',var_1)
print('variable_2 is now equal to:,',var_2)

var_1,var_2=var_2,var_1
print('variable_1 is now again equal to:',var_1)
print('variable_1 is now again equal to:',var_2)
