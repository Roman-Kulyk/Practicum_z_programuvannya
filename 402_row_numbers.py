#402. На вхід програми подається один рядок з цілими числами. Числа розділені пропусками. 
# Необхідно вивести суму цих чисел. Наприклад, якщо був введений рядок чисел 2 -1 9 6, 
# то результатом роботи програми буде їх сума 16.

numbers = input("Enter four numbers through the spacebar: ").split(" ")
sum_numbers = int(numbers[0]) + int(numbers[1]) + int(numbers[2]) + int(numbers[3])
print('Sum of number: {0:d}'.format(sum_numbers))