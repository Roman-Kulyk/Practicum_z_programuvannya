# 531. Дано місяць і рік для двох дат (наприклад, 12.2014 і 6.2019). 
# Користувач вводить ще одну дату (місяць і рік). 
# Визначити, чи належить третя дата діапазону від першої дати до другої включно. 
# Результатом роботи програми має бути повідомлення YES або NO.
'''
Вхідні дані:
2018
5

Вихідні дані:
YES
'''
dictionary = {'start':{'year':2014,'month':12},
               'end':{'year':2019,'month':5}}

date = input("Enter year and month through the spacebar: ").split(" ")

if int(date[0]) > dictionary['start']['year'] and \
   int(date[0]) < dictionary['end']['year']:
    print("YES")

elif int(date[0]) == dictionary['start']['year'] and \
   int(date[0]) <= dictionary['end']['year'] and \
   int(date[1]) >= dictionary['start']['month']:
    print("YES")

elif int(date[0]) == dictionary['end']['year'] and \
   int(date[0]) <= dictionary['end']['year'] and \
   int(date[1]) <= dictionary['end']['month']:
    print("YES")  

else:
    print("NO")
