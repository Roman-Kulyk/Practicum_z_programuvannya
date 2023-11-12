# 505. Магічний квадрат - це квадратна таблиця n x n, заповнена цілими числами таким чином, 
# що сума чисел у кожному рядку, кожному стовпчику і на обох діагоналях однакова. 
# Напишіть програму, яка отримує послідовність чисел у форматі як у вхідних даних, 
# з яких утворюється двовимірна таблиця (список списків) цілочисельних елементів і 
# перевірте чи є вона магічним квадратом. Програма має вивести True чи False відповідно.
"""
Вхідні дані:
1 2 3,4 5 6,7 8 9
4 9 2,3 5 7,8 1 6
7 12 1 14,2 13 8 11,16 3 10 5,9 6 15 4
23 28 21,22 24 26,27 20 25
16 23 17,78 32 21,17 16 15
4 3 8,9 5 1,2 7 6

Вихідні дані:
False
True
True
True
False
True
"""
def is_magic_square(matrix):
    n = len(matrix)

    row_sums = [sum(row) for row in matrix]
    col_sums = [sum(matrix[i][j] for i in range(n)) for j in range(n)]
    if row_sums != col_sums:
        return False
    
    main_diag_sum = sum(matrix[i][i] for i in range(n))
    if main_diag_sum != row_sums[0]:
        return False
    
    anti_diagram_sum = sum(matrix[i][n - 1 - i] for i in range(n))
    if anti_diagram_sum != row_sums[0]:
        return False
    return True
    
input_data = input("Enter your data: ")
rows = input_data.split(',')
matrix = [list(map(int, row.split())) for row in rows]
print(is_magic_square(matrix))
