#214. Напишіть програму, яка підраховує додатні і від’ємні числа, а також нулі, введені користувачем, 
# і виводить їхню кількість в один рядок з одним пропуском між ними.

numbers = input("Enter five numbers through the spacebar: ").split(" ")

for number in numbers:
    if int(number) % 2 == 0:
        even = []
        even.append(number)
        
    else:
        int(number) % 2 != 0
        odd = []
        odd.append(number)
        
print(even)
print(odd)