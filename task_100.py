#100. Потрібно підрахувати, на скільки раніше буде закінчуватися k-й урок, якщо всі перерви скоротити на 5 хвилин. 
#Вводиться одне натуральне число k, не більше 7. 
#Необхідно вивести одне натуральне число - час у хвилинах.

k = int(input('Enter a number from 1 to 7: '))
earlier = (k -1) * 5
print(earlier)