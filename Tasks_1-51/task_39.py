#39.Введіть з клавіатури в окремих рядках різні типи величин: ціле число,
#текстовий рядок, дійсне число. Виведіть інформацію про типи введених даних.

number=int(input('Enter a number: '))
text= str(input('Enter a text: '))
real_number=float(input('Enter a number: '))

print(type(number))
print(type(text))
print(type(real_number))
