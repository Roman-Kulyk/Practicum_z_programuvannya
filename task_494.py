# 494. Дано список цілих чисел. Потрібно стиснути його, перемістивши всі ненульові елементи 
# в ліву частину списку, не змінюючи їх порядок, а всі нулі - в праву частину. Порядок 
#  елементів змінювати не можна, додатковий список використовувати не можна, 
# завдання потрібно виконати за один прохід по списку. Роздрукуйте отриманий список.
"""
Вхідні дані:
6 0 3 0 5 0 0 4

Вихідні дані:
6 3 5 4 0 0 0 0
"""

def compress_list(arr):
    left = 0
    right = len(arr) - 1
    
    while left < right:
        while arr[left] != 0:
            left += 1
        while arr[right] == 0:
            right -= 1
        
        if left < right:
            arr[left], arr[right] = arr[right],arr[left]
    return arr

arr = [int(num) for num in input("Enter your list: ").split()]
result = compress_list(arr)
print(result)
for i in result:
    print(i, sep= ' ', end = ' ')
print()