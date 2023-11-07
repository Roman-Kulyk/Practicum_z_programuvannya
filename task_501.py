# 501. У трьох автобусах розсадили дітей так, що їх кількість в різних автобусах різна. 
# Яку найменшу кількість дітей потрібно пересадити, щоб у кожному автобусі їх було порівно? 
# У першому рядку задано три натуральних числа, не більших за 100 - кількість дітей у 
# першому, другому та третьому автобусах. Виведіть одне число - найменшу кількість дітей, 
# яких потрібно пересадити. Якщо це зробити не можливо, то виведіть NO SOLUTIONS.
"""
Вхідні дані:
9 10 10
2 5 8

Вихідні дані:
NO SOLUTIONS
3
"""
def min_children_to_move(bus1, bus2,bus3):
    total_children = [bus1,bus2,bus3]
    max_children = max(total_children)
    min_children = min(total_children)

    if (max_children - min_children)% 2 == 0:
        return (max_children - min_children) // 2
    else:
        return "No Solutios"
bus1 = int(input("Enter your number for bus1: "))
bus2 = int(input("Enter your number for bus2: "))
bus3 = int(input("Enter your number for bus3: "))

result = min_children_to_move(bus1,bus2,bus3)
print(result)