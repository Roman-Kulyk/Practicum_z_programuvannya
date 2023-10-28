# 487. Напишіть програму, на вхід якої подається список чисел одним рядком. Програма 
# повинна для кожного елемента цього списку вивести суму двох його сусідів. Для елементів 
# списку, які є крайніми, одним із сусідів вважається елемент, що знаходить на протилежному 
# кінці цього списку. Якщо на вхід прийшло тільки одне число, треба вивести його ж. 
# Виведення повинно містити один рядок з числами нового списку, розділеними пропусками.
"""
Вхідні дані:
1 3 5 6 10
5

Вихідні дані:
13 6 9 15 7
5
"""
   

def calculate_neighbours_sum(input_list):
    output_list = []
    if len(input_list) == 1:
        return input_list
    
    for i in range(len(input_list)):
        left_neighbor = input_list[(i - 1) % len(input_list)]
        right_neighbor = input_list[(i + 1) % len(input_list)]
        neighbor_sum = left_neighbor + right_neighbor
        output_list.append(neighbor_sum)
    return output_list

input_numbers = input("Enter your list: ").split()
input_numbers = [int(num) for num in input_numbers]
result =  calculate_neighbours_sum(input_numbers)
print(" ".join(map(str, result)))