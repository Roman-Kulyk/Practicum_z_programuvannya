# Реалізуйте програму, яка зчитує ціле число, що вводиться з командного рядка, і записує у 
# текстовий файл інформацію, щодо парності або непарності числа.


number = int(input('Enter your number: '))
if number % 2 == 0:
    result = 'Number is even.'
else:
    result = 'Number is odd.'


freading = open('ex_#883_2_number.txt','wt')
freading.write(result)
freading.close()