# Як відомо, День програміста припадає на 256 день року, у невисокосний рік це 13 
# вересня, а у високосний - 12. Дізнайтеся число і номер місяця, що припадають на 
# день, за номером n, який вводиться користувачем, у невисокосному 2017 році.

def what_date():
    n = int(input("Enter n: "))
    n -= 1 
    month,day = divmod(n,31)
    if day < 12:
        month += 1
        day += 1
        print(day)
        print(month)
what_date()