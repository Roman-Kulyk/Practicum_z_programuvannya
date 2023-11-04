# 496. Напишіть програму, яка приймає на вхід список чисел і число (в окремих рядках), 
# після чого виводить всі позиції через пропуск, на яких це число зустрічається в переданому 
# списку (позиції у списку нумеруються з 1). Позиції повинні бути виведені в порядку 
# зростання. Якщо число не знайдено в списку, потрібно вивести рядок None (без лапок, 
# з великої літери).
"""
Вхідні дані:
5 7 3 4 9 8 4 7 4
4

Вихідні дані:
4 7 9

arr = [int(num) for num in input("Enter your list: ").split()]
num = int(input("Enter your number: "))
print(arr, num)
for i in arr:
    if i == num:
        print(arr.index(i))
    else:
        print(None)
"""
def find_positions(numbers, target):
    positions = [str(i + 1) for i, num in enumerate(numbers) if num == target]
    if positions:
        return ' '.join(positions)
    else:
        return None
    
numbers = [int(num) for num in input("Enter your list: ").split()]
target = int(input("Input your number: "))
result = find_positions(numbers, target)
print(result)