#404. Необхідно зчитати рядок з 5 цифр, розділених пропусками, і зберегти кожну цифру у список. 
# Створіть копію списку із впорядкованими елементами у зворотному порядку. 
# Виведіть число, яке утворюється об’єднанням елементів нового списку.


numbers = input("Enter five numbers through the spacebar: ").split(" ")
print(numbers)
reverse_numbers = numbers[::-1]
print(reverse_numbers)

sum_numbers = int(reverse_numbers[0]) + int(reverse_numbers[1]) + int(reverse_numbers[2]) + int(reverse_numbers[3]) + int(reverse_numbers[4])
print('New number: {0:}'.format(''.join(reverse_numbers)))
