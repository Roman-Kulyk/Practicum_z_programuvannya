# 658. Напишіть функцію, яка отримує значення середньомісячної кількості опадів 
# по місяцях (в мм) і повертає загальний обсяг опадів протягом року, середньорічну 
# кількість опадів, назви місяців та значення з найвищим та найменшим числом опадів 
# протягом року.
'''
Вхідні дані:
22 22 24 49 72 98 101 82 51 40 36 24

Вихідні дані:
(621.0, 51.75, (101.0, 'July'), (22.0, 'January'))
'''
def humidity():
    humidity_list = [int(item) for item in input("Enter the list items : ").split()]
    months_list = ['January','February','March','April','May','June','July','August',\
                   'September','October','November','December']
    
    all_year = sum(humidity_list)
    aver_mon = all_year/12
    max_mon = max(humidity_list)
    max_month = months_list[humidity_list.index(max_mon)]#it assign max index from =>
    #humidity_list item to months_list item so they correspond to each other

    min_mon = min(humidity_list)
    min_month = months_list[humidity_list.index(min_mon)]  #it assign min index from => 
    #humidity_list item to months_list item so they correspond to each other
    print(f"({all_year},{aver_mon},{(max_mon, max_month)},{(min_mon,min_month)})")

humidity()
