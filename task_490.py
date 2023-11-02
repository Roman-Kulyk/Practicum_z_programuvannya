# 490. Дано список з n (1 ≤ n ≤ 100000) цілих чисел і число k (|k| < 100000). Циклічно 
# посуньте список на |k| елементів вправо, якщо k - додатне і вліво, якщо від’ємне число. 
# Програма отримує на вхід список цілих чисел, потім число k. Рішення повинно мати 
# складність O(n), тобто не повинно залежати від k. 
# Додатковим списком користуватися не можна.
"""
Вхідні дані:
5 3 7 4 6
3
7 4 6 5 3
-3
Вихідні дані:
7 4 6 5 3
5 3 7 4 6
"""
def list_shift(arr, k):
    k = k % len(arr)
    if k == 0:
        return arr
    else:
        if k > 0:
            return arr[-k:] + arr[:-k]
        #else:
        #    return arr[-k:] + arr[:-k]
        
arr = input("Enter your list: ").split()#it takes list from user's input
arr = [int(num) for num in arr]
k = int(input("Enter you koef: "))
result = list_shift(arr,k)
print(result)