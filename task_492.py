# 492. Вводиться рядок слів, розділених пропусками. Знайти найдовше слово і вивести його 
# на екран. Розглянути випадок, коли найдовших неоднакових слів може бути кілька.
"""
Вхідні дані:
Sparse is better than dense
Readability counts
Long time Pythoneer Tim Peters succinctly channels the BDFL's guiding principles for Python's design into 20 aphorisms

Вихідні дані:
Sparse better
Readability
succinctly principles
"""
# initialize list 
test_list = input("Enter your list: ").split()
 
# printing original list 
print("The original list : " + str(test_list))
 
# Longest String in list
# using loop
max_len = -1
#print(max_len)
max_el_list = []
for ele in test_list:
    
    if len(ele) >= max_len:
        max_len = len(ele)
        res = ele
        max_el_list.append(res)
 
# printing result
for i in max_el_list:
    print(i, sep= ' ', end = ' ')
print()