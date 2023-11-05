# 500. Вводиться послідовність цілих чисел у вигляді як у вхідних даних і перетвоюється у 
# список списків, тобто у список, кожен елемент якого також є списком. Впорядкуйте цей список 
# по другому елементу кожного списку і виведіть впорядкований список.
"""
Вхідні дані:
1 2 3,2 1 3,4 0 1

Вихідні дані:
[[1, 2, 3], [2, 1, 3], [4, 0, 1]]
[[4, 0, 1], [2, 1, 3], [1, 2, 3]]
"""
def sort_list_by_second_element(input_string):
    input_lines = input_string.strip().split(',')
    nested_lists = []

    for line in input_lines:
        nested_lists.append(list(map(int,line.split())))
        sorted_list = sorted(nested_lists, key = lambda x: x[1])
        return sorted_list
    
input_data = "1 2 3,2 1 3,4 0 1"
sorted_list = sort_list_by_second_element(input_data)
print(sorted_list)