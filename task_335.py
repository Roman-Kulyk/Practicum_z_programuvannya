# 335. Дано рядок, який, можливо, містить пропуски. 
# «Витягніть» з цього рядка всі символи, які є цифрами і складіть з них новий рядок.
'''
Вхідні дані:
3+3=6
2 * 3 = 6
Вихідні дані:
336
236
'''

input_str = input("Enter a row: ")
result = []
for char in input_str:
    if char.isdigit():
        result.append(char)
print("".join(result))