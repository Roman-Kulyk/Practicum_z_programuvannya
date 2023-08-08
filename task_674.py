# 674. Напишіть функцію для знаходження кількість повторень елементів у 
# послідовності, які вводяться через кому в один рядок, і виведіть список пар 
# «елемент- кількість повторень» в порядку спадання кількості повторень як у вихідних 
# даних.
'''
Вхідні дані:
1,2,3,4,3,3,2,4,5,6,1,2,3,4,6,1,2,3,4,6,6

Вихідні дані:
[(3, 5), (2, 4), (4, 4), (6, 4), (1, 3), (5, 1)]
'''
def count_elements(sequence):
    elements = sequence.split(',')
    counts = {}
    for elem in elements:
        if elem in counts:
            counts[elem] += 1
        else:
            counts[elem] = 1

    sorted_counts = sorted(counts.items(),key=lambda x:x[1],reverse=True)
    return sorted_counts

input_sequence = input('Enter your sequence: ')
result = count_elements(input_sequence)
print(result)