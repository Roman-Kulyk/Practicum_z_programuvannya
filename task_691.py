# 691. Магічний квадрат - це квадратна таблиця n x n, заповнена цілими числами таким чином, 
# що сума чисел у кожному рядку, кожному стовпчику і на обох діагоналях однакова. Напишіть 
# функцію, яка отримує послідовність чисел у форматі як у вхідних даних, з яких утворюється 
# двовимірна таблиця (список списків) цілочисельних елементів і перевірте чи є вона магічним 
# квадратом. Результатом має бути True чи False відповідно.
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


    #it checks sums in rows
    row_sums = [sum(row) for row in matrix]
    if len(set(row_sums)) != 1:
        return False
    

    #it check sums in columns
    col_sums = [sum(col) for col in matrix]
    if len(set(col_sums)) != 1:
        return False
    
    #it checks sums on main diagonal
    main_diag_sum = sum(matrix[i][i] for i in range(n))
    if main_diag_sum != row_sums[0]:
        return False
    
    #it checks sums on additional diagonal
    anti_diag_sums = sum(matrix[i][n - i -1] for i in range(n))
    if anti_diag_sums !=row_sums[0]:
        return False
    
    return True

input_sequence = input("Enter your list numbers: ")
#it creates a matrix from sequence
matrix = [list(map(int, row.split())) for row in input_sequence.split(",")]

#it checks if matrix is a magic square
result = is_magic_square(matrix)
print(result)
                        