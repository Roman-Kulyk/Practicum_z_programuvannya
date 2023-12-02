# 687. Напишіть функцію для вирішення класичної давньої китайської головоломки: дано кількість 
# голів n та лап m серед курчат та кроликів на фермі. Скільки курчат і кроликів на фермі?
"""
Вхідні дані:
5 12
3 4

Вихідні дані:
4 1
NO SOLUTIONS! NO SOLUTIONS!
"""
def how_many_chickens_rabbits(a,b):
    if b / a < 2 or b % 2 != 0 or a * 4 < b:
        print("NO SOLUTIONS!")
    else:
        number_of_rabbits = b % (a * 2) / 2
        number_of_chicken = a - number_of_rabbits
        print(number_of_chicken, number_of_rabbits)

how_many_chickens_rabbits(5, 12)
how_many_chickens_rabbits(3, 4)
how_many_chickens_rabbits(9, 31)
how_many_chickens_rabbits(7, 32)