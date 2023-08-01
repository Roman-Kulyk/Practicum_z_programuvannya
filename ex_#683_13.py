# Створіть таблицю множення. Розмірність таблиці (кількість рядків і стовпців) 
# вводиться з клавіатури.
def multiplication_table(m,n):
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            print(("{:3d}".format(i * j,)), end='')
        print()


multiplication_table(10,10)
#multiplication_table(5,7)