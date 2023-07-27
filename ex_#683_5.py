# Зчитайте назву місяця від користувача як рядок і виведіть кількість днів у 
# вказаному місяці. Врахувати те, що «February» може мати 28 або 29 днів.
def month_func():
    month = input("Enter a month: ")
    list_31 = ['January','March',"May",'July','August','Octover','December']
    list_30 = ['April','June','September','November']
    if month in list_31:
        print(31)
    elif month in list_30:
        print(30)
    elif month == 'February':
        print(28,29)

month_func()