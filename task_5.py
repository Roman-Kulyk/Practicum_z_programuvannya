#Напишіть програму, яка зчитує ціле число, і друкує попереднє та наступне числа
#відносно введеного.


number = int (input('Please enter a number:'))
next_num = number + 1
previous_num = number - 1

print(f'The next number {number} is {next_num}.')
print(f'The previous number for the number {number} is {previous_num}.')
