# 661. На стадіоні є три категорії місць для сидіння: 
# місця класу A коштують a грошових одиниць, 
# місця класу B коштують b грошових одиниць, 
# а місця класу C - c грошових одиниць. 
# Напишіть першу функцію, 
# яка запитує скільки продано квитків на кожний клас місць, 
# і другу функцію, 
# яка відображає суму отриманого доходу від продажу квитків на кожен клас окремо і 
# загалом. Формати введення і виведення такі, як у вхідних і вихідних даних.
'''
Вхідні дані:
A
20.50
45
B
15.75
30
C
10.55
15

Вихідні дані:
({'A': 922.5, 'B': 472.5, 'C': 158.25}, 1553.25)
'''
def how_many_per_class():
    
    A = int(input("Enter how many sold for A class: "))
    B = int(input("Enter how many sold for B class: "))
    C = int(input("Enter how many sold for C class: "))
    return A,B,C

def revenue(A,B,C):
    price_A = float(input("How much one ticket for A:"))
    price_B = float(input("How much one ticket for B:"))
    price_C = float(input("How much one ticket for C:"))
    revenue = A * price_A + B * price_B + C * price_C

    #print(A * price_A)
    #print(B * price_B)
    #print(C * price_C)
    #print(revenue)
    revenue_dict = {}
    revenue_dict['A'] = price_A*A
    revenue_dict['B'] = price_B*B
    revenue_dict['C'] = price_C*C
    print(f'({revenue_dict},{revenue})')

A,B,C = how_many_per_class()
revenue(A,B,C)