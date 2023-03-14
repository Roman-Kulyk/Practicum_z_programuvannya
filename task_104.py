#104.Напишіть програму, яка виводить назви введених чисел. Користувач вводить ціле число. 
#Якщо це число або 1 або 2 або 3, то виводиться повідомлення - назва числа, відповідно, One, Two, Three. 
#В усіх інших випадках виводиться слово Unknown.

num = int(input('Enter a number: '))
if num ==1:
    print('One')
elif num == 2:
    print('Two')
elif num == 3:
    print('Three')
else:
    print('Unknown')
