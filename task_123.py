#123. Дано ціле число a. Знайти значення виразу: a/(|a|-10). Врахувати у програмі випадок, 
#коли відбувається ділення на нуль.

a = int(input('Enter a number: '))

if a == 10:
    print('You are not allowed divide by zero.')
else:
    num = a/(abs(a)-10)
    print(num)