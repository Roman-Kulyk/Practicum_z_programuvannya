#Напишіть програму, на вхід якої подається назва місяця, а програма виводить кількість днів у ньому. 
#Врахуйте те, що місяць «Лютий» може мати 28 або 29 днів.


month = input('Enter a month name: ')
if month == ("January" or "March" or "May" or "July" or "August" or "October" or "December"):
    print(f'{month} has 31 days.')



elif month == ("April" or "June" or "September" or "November"):
    print(f'{month} has 30 days.')



elif month == "February":
    print(f'{month} has 28 or 29 days.')
else:
    print('Enter a correct name.')