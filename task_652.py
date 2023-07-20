# 652. Напишіть функцію, яка друкує усі слова із списку, довжина яких перевищує n.
'''
Вхідні дані:

Denmark England Estonia France Greece Romania Ukraine
6

Вихідні дані:
Denmark England Estonia Romania Ukraine
'''
def vocab_func():
    text = input("Enter you countries: ").split()
    size = int(input("Enter number: "))
    country_list = []
    for country in text:
        if len(country) > size:
            country_list.append(country)
        else:
            continue
    for country in country_list:
        print(country, end = ' ')
    print()

vocab_func()